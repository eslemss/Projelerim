from flask import Flask, jsonify, request, g
import sqlite3
from flask_cors import CORS
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Database connection
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('library.db')
        g.db.row_factory = sqlite3.Row
    return g.db

# Initialize database tables
def init_db():
    db = get_db()
    cursor = db.cursor()
    
    # Create tables if they don't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS kitaplar (
            kitap_id INTEGER PRIMARY KEY AUTOINCREMENT,
            ad TEXT NOT NULL,
            yazar TEXT NOT NULL,
            yayin_yili INTEGER,
            isbn TEXT UNIQUE,
            durum TEXT DEFAULT 'Rafta',
            eklenme_tarihi TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS uyeler (
            uye_id INTEGER PRIMARY KEY AUTOINCREMENT,
            ad TEXT NOT NULL,
            soyad TEXT NOT NULL,
            email TEXT UNIQUE,
            telefon TEXT,
            kayit_tarihi TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS odunc (
            odunc_id INTEGER PRIMARY KEY AUTOINCREMENT,
            kitap_id INTEGER NOT NULL,
            uye_id INTEGER NOT NULL,
            odunc_tarihi TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            iade_tarihi TIMESTAMP,
            durum TEXT DEFAULT 'Ödünçte',
            FOREIGN KEY (kitap_id) REFERENCES kitaplar (kitap_id),
            FOREIGN KEY (uye_id) REFERENCES uyeler (uye_id)
        )
    ''')
    
    db.commit()

# API Routes for Books
@app.route('/api/kitaplar', methods=['GET'])
def get_kitaplar():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM kitaplar ORDER BY ad')
    return jsonify([dict(row) for row in cursor.fetchall()])

@app.route('/api/kitaplar/search', methods=['GET'])
def search_kitaplar():
    search_query = request.args.get('search', '')
    db = get_db()
    cursor = db.cursor()
    
    # Search in both title and author
    query = '''
        SELECT * FROM kitaplar 
        WHERE ad LIKE ? OR yazar LIKE ?
        ORDER BY ad
    '''
    search_term = f'%{search_query}%'
    cursor.execute(query, (search_term, search_term))
    kitaplar = cursor.fetchall()
    return jsonify([dict(k) for k in kitaplar])

@app.route('/api/kitaplar', methods=['POST'])
def add_kitap():
    data = request.get_json()
    if not all(k in data for k in ['ad', 'yazar']):
        return jsonify({'error': 'Ad ve yazar bilgileri zorunludur'}), 400
    
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute('''
            INSERT INTO kitaplar (ad, yazar, yayin_yili, isbn, durum)
            VALUES (?, ?, ?, ?, ?)
        ''', (data['ad'], data['yazar'], data.get('yayin_yili'), 
              data.get('isbn'), data.get('durum', 'Rafta')))
        db.commit()
        return jsonify({'message': 'Kitap başarıyla eklendi', 'id': cursor.lastrowid}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Bu ISBN numarası zaten mevcut'}), 400

# API Routes for Members
@app.route('/api/uyeler', methods=['GET'])
def get_uyeler():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM uyeler ORDER BY soyad, ad')
    return jsonify([dict(row) for row in cursor.fetchall()])

@app.route('/api/uyeler', methods=['POST'])
def add_uye():
    data = request.get_json()
    if not all(k in data for k in ['ad', 'soyad', 'email']):
        return jsonify({'error': 'Ad, soyad ve email bilgileri zorunludur'}), 400
    
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute('''
            INSERT INTO uyeler (ad, soyad, email, telefon)
            VALUES (?, ?, ?, ?)
        ''', (data['ad'], data['soyad'], data['email'], data.get('telefon')))
        db.commit()
        return jsonify({'message': 'Üye başarıyla eklendi', 'id': cursor.lastrowid}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Bu email adresi zaten kayıtlı'}), 400

# API Routes for Book Loans
@app.route('/api/odunc', methods=['GET'])
def get_odunc_listesi():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        SELECT o.*, k.ad as kitap_adi, u.ad as uye_adi, u.soyad as uye_soyad 
        FROM odunc o
        JOIN kitaplar k ON o.kitap_id = k.kitap_id
        JOIN uyeler u ON o.uye_id = u.uye_id
        ORDER BY o.odunc_tarihi DESC
    ''')
    return jsonify([dict(row) for row in cursor.fetchall()])

@app.route('/api/odunc/odunc_ver', methods=['POST'])
def odunc_ver():
    data = request.get_json()
    if not all(k in data for k in ['kitap_id', 'uye_id']):
        return jsonify({'error': 'Kitap ve üye bilgileri zorunludur'}), 400
    
    db = get_db()
    cursor = db.cursor()
    
    try:
        # Check if book is available
        cursor.execute('SELECT durum FROM kitaplar WHERE kitap_id = ?', (data['kitap_id'],))
        kitap = cursor.fetchone()
        if not kitap:
            return jsonify({'error': 'Kitap bulunamadı'}), 404
        if kitap['durum'] != 'Rafta':
            return jsonify({'error': 'Kitap şu anda ödünçte veya müsait değil'}), 400
        
        # Update book status
        cursor.execute('UPDATE kitaplar SET durum = ? WHERE kitap_id = ?', 
                      ('Ödünçte', data['kitap_id']))
        
        # Create loan record
        cursor.execute('''
            INSERT INTO odunc (kitap_id, uye_id, durum)
            VALUES (?, ?, ?)
        ''', (data['kitap_id'], data['uye_id'], 'Ödünçte'))
        
        db.commit()
        return jsonify({'message': 'Kitap ödünç verildi', 'id': cursor.lastrowid}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/odunc/iade_et/<int:odunc_id>', methods=['POST'])
def iade_et(odunc_id):
    db = get_db()
    cursor = db.cursor()
    
    try:
        # Get loan info
        cursor.execute('SELECT * FROM odunc WHERE odunc_id = ?', (odunc_id,))
        odunc = cursor.fetchone()
        if not odunc:
            return jsonify({'error': 'Ödünç kaydı bulunamadı'}), 404
        if odunc['durum'] == 'İade Edildi':
            return jsonify({'error': 'Bu kitap zaten iade edilmiş'}), 400
        
        # Update book status
        cursor.execute('UPDATE kitaplar SET durum = ? WHERE kitap_id = ?', 
                      ('Rafta', odunc['kitap_id']))
        
        # Update loan record
        cursor.execute('''
            UPDATE odunc 
            SET durum = 'İade Edildi', iade_tarihi = CURRENT_TIMESTAMP 
            WHERE odunc_id = ?
        ''', (odunc_id,))
        
        db.commit()
        return jsonify({'message': 'Kitap başarıyla iade edildi'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Close database connection after each request
@app.teardown_appcontext
def close_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True, port=5000)
