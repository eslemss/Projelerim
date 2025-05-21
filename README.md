🎬 Film ve Dizi İzleme Uygulaması

Kullanıcı ve Geliştirici Dokümantasyonu

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

Dosya/Modül Açıklama

app.py Ana uygulama. Tüm işlemleri başlatır ve içerik kontrolünü sağlar.

init_db.py SQLite veritabanı kurulum işlemlerini yapar.

update_db.py Yeni içerikler ya da değişiklikler veritabanına yazılır.

check_db.py Mevcut içerikleri doğrular ya da listeler.

add_wednesday.py Örnek içerik olarak "Wednesday" dizisini ekler.

check_wednesday.py Wednesday dizisi için özel kontrol veya listeleme işlemleri.

fix_image_paths.py, fix_delibal_image.py Görsel yollarını düzenler veya düzeltir.

list_all_content.py Tüm içerikleri terminale basar.

requirements.txt Gerekli bağımlılıkları listeler (örn. sqlite3, os, pillow vb.).

💻 Kullanım Adımları Ortam Kurulumu

bash Kopyala Düzenle pip install -r requirements.txt Veritabanını Başlat

bash Kopyala Düzenle python init_db.py İçerik Ekleme / Güncelleme

bash Kopyala Düzenle python add_wednesday.py python update_db.py İçerikleri Görüntüleme

bash Kopyala Düzenle python list_all_content.py Veritabanı Kontrol

bash Kopyala Düzenle python check_db.py

📸 Örnek Ekran Çıktıları

--Ana Sayfa--
![Ekran görüntüsü 2025-05-21 122405](https://github.com/user-attachments/assets/82e398d5-a95e-4cb5-ae18-d9aea83dd0e2)

 --Giriş Yap--
 
 ![Ekran görüntüsü 2025-05-21 122436](https://github.com/user-attachments/assets/86680218-f58e-4625-8b7a-19c90c7d7c7d)

 --Kayıt Ol-- 

 ![Ekran görüntüsü 2025-05-21 122447](https://github.com/user-attachments/assets/a813b006-a42b-4bbc-a77f-8fcad09a06f2)

 
 --İzleme Listesi Ekleme--

 ![Ekran görüntüsü 2025-05-21 122539](https://github.com/user-attachments/assets/36f59516-efa8-446e-9ae3-0dc3e7bedb1f)


 --İzleme Listesi Silme--

 ![Ekran görüntüsü 2025-05-21 122850](https://github.com/user-attachments/assets/c8bf2906-bd25-4ffc-b732-c3902ecf7bba)



💻Hazırlayan: Ayşe Eslem Gökhan

📚 Kütüphane Yönetim Sistemi

– Kullanıcı ve Geliştirici Dokümantasyonu


📌 Proje Tanımı

Bu web tabanlı sistem, kitapların ve kullanıcıların yönetimini sağlayan basit bir Kütüphane Yönetim Sistemi'dir. Kullanıcılar kitapları listeleyebilir, yeni kitap ekleyebilir ve sistem üzerindeki kitapları arayabilir.

🧱 Uygulama Mimarisi

📄 Ana Bileşenler

Dosya	Açıklama

index.html	Ana kullanıcı arayüzü. Kitap listeleme, ekleme ve arama işlemleri burada gerçekleşir.

style.css	Web sayfası tasarımı ve görsel biçimlendirme işlemleri.

app.js	Kitap ekleme, silme, filtreleme gibi işlemleri yöneten temel JavaScript dosyası.

logo.png	Proje logosu.

.git/	Proje git ile sürüm kontrolüne alınmış. Geliştirici geçmişi burada tutulur.


💻 Kullanıcı Arayüzü Özellikleri

📋 Kitap Listesi Görüntüleme: Var olan tüm kitapları tabloda gösterir.


➕ Yeni Kitap Ekleme: Form aracılığıyla başlık, yazar ve kategori bilgileri girilerek kitap eklenebilir.


🔍 Kitap Arama/Filtreleme: Anahtar kelimeye göre filtreleme yapılabilir.


🗑️ Kitap Silme: Listeden kitap silme işlevi mevcuttur (eğer uygulanmışsa).


🎨 Responsive Tasarım: Stil dosyası sayesinde farklı cihazlarda uyumlu görüntüleme.


⚙️ Kurulum ve Kullanım

Projeyi Açmak İçin


Tüm dosyaları bir klasöre çıkartın.


index.html dosyasını çift tıklayarak tarayıcıda açın.


Kitap Ekleme Adımları


Kitap adı, yazarı ve kategorisini girin.


"Kitap Ekle" butonuna tıklayın.


Liste otomatik güncellenecektir.


Arama Yapma


Sayfanın üst kısmındaki arama kutusuna metin girin.


Liste anlık olarak filtrelenir.



📸 Örnek Ekran Çıktıları


--Anasayfa--

![image](https://github.com/user-attachments/assets/8b8bbac8-fdcb-4c42-bd52-920ee67ad4b3)

![image](https://github.com/user-attachments/assets/3bf3d6ad-448d-4cbd-aa2b-e75617af0b54)

![image](https://github.com/user-attachments/assets/d7eb8086-802a-4f91-b08f-697b33bd6465)

--Log In--

![image](https://github.com/user-attachments/assets/500666e4-e1bf-4568-9faf-782a91a26366)

--Admin Paneli--

![image](https://github.com/user-attachments/assets/826f1e4e-4f7a-4350-9274-ed0c3d9453d0)


--Kitap Ekle--

![image](https://github.com/user-attachments/assets/b43a827b-e7da-4361-b97a-83cdccea62bd)

--Kitap Ara--

![image](https://github.com/user-attachments/assets/a097b32b-dba2-4d8f-be54-70f8a95681e8)

--Üye Ekle--

![image](https://github.com/user-attachments/assets/b76990fb-8a06-4ab5-a9a2-27e0d173a9c6)







