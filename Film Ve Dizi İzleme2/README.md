🎬 Film ve Dizi İzleme Uygulaması 
- Kullanıcı ve Geliştirici Dokümantasyonu

  
📌 Proje Tanımı
Bu Python tabanlı uygulama, kullanıcıların film ve dizilerini veritabanı destekli olarak yönetmesine olanak tanır. Veritabanı üzerinde içerik ekleme, listeleme, güncelleme ve özel içerik işlemleri gerçekleştirilebilir.

🧱 Uygulama Mimarisi

🎥 İçerik Modülü

Her film ya da dizi için aşağıdaki bilgiler tutulur:

Ad: İçeriğin ismi (örn. "Wednesday")

Tür: Film / Dizi

Kategori: Komedi, Aksiyon, Belgesel vb.

Görsel Yolu: İçeriğe ait görselin yolu

Veritabanı ID’si: Her içerik benzersiz ID’ye sahiptir

📂 Temel Dosya ve Modüller


Dosya/Modül	Açıklama

app.py	Ana uygulama. Tüm işlemleri başlatır ve içerik kontrolünü sağlar.

init_db.py	SQLite veritabanı kurulum işlemlerini yapar.

update_db.py	Yeni içerikler ya da değişiklikler veritabanına yazılır.

check_db.py	Mevcut içerikleri doğrular ya da listeler.

add_wednesday.py	Örnek içerik olarak "Wednesday" dizisini ekler.

check_wednesday.py	Wednesday dizisi için özel kontrol veya listeleme işlemleri.

fix_image_paths.py, fix_delibal_image.py	Görsel yollarını düzenler veya düzeltir.

list_all_content.py	Tüm içerikleri terminale basar.

requirements.txt	Gerekli bağımlılıkları listeler (örn. sqlite3, os, pillow vb.).


💻 Kullanım Adımları
Ortam Kurulumu

bash
Kopyala
Düzenle
pip install -r requirements.txt
Veritabanını Başlat

bash
Kopyala
Düzenle
python init_db.py
İçerik Ekleme / Güncelleme

bash
Kopyala
Düzenle
python add_wednesday.py
python update_db.py
İçerikleri Görüntüleme

bash
Kopyala
Düzenle
python list_all_content.py
Veritabanı Kontrol

bash
Kopyala
Düzenle
python check_db.py


📸 Örnek Ekran Çıktıları


--Ana Sayfa--
![image](https://github.com/user-attachments/assets/d312047a-1ebe-4c3b-8dbf-fd7805103f1a)
--Giriş Yap--
![image](https://github.com/user-attachments/assets/bc665416-5766-4e56-aa94-e4c4053b55c3)
--Kayıt Ol--
![image](https://github.com/user-attachments/assets/10af3cb1-03d9-49a4-906d-31aee50d686e)
--İzleme Listesi Ekleme--
![image](https://github.com/user-attachments/assets/baea7b7a-6e03-4f1e-90d9-b1387ba18a8f)
--İzleme Listesi Silme--
![image](https://github.com/user-attachments/assets/177dc329-2a78-4f57-8f60-b7cc74d1777a)



🛠️ Geliştirici Notları

Kodlar Python 3 uyumludur.

Veritabanı işlemleri sqlite3 ile gerçekleştirilir.

Görsellerin doğru görünmesi için image/ dizini yapılandırılmalıdır.

README.md otomatik üretim için list_all_content.py kullanılabilir.


💻Hazırlayan: 
Ayşe Eslem Gökhan
