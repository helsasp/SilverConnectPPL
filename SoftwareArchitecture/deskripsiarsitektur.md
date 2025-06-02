Deskripsi Arsitektur Microservices Silverconnect

Silverconnect adalah aplikasi sosial untuk lansia yang fokus membantu mereka menemukan teman, komunitas, dan aktivitas, serta menyediakan fitur pendukung seperti onboarding, profil, dan emergency.

Untuk mengakomodasi skalabilitas, fleksibilitas, dan maintenance yang mudah, Silverconnect dirancang dengan arsitektur microservices yang terdiri dari beberapa layanan utama berikut:
1. Authentication Service

    Bertanggung jawab mengelola proses sign up, sign in, lupa password, dan manajemen sesi.

    Melakukan validasi kredensial dan mengeluarkan token akses (JWT/OAuth).

    Menghubungkan onboarding untuk profil dasar.

2. User Profile Service

    Mengelola data profil lansia, termasuk data pribadi, preferensi, kontak darurat, dan data onboarding gamified.

    Menyimpan dan memperbarui data profil sesuai input pengguna.

3. Friends Service

    Menyediakan fitur pencarian teman berdasarkan minat.

    Mengelola permintaan pertemanan dan riwayat chat antar pengguna.

    Integrasi dengan Notification Service untuk notifikasi pesan.

4. Community Service

    Mengelola komunitas yang ada: pembuatan komunitas, pencarian komunitas, bergabung, dan interaksi grup.

    Memfasilitasi obrolan grup komunitas.

    Berintegrasi dengan Notification Service untuk update komunitas.

5. Activity Service

    Mengelola daftar aktivitas, pemesanan slot aktivitas, dan konfirmasi pemesanan.

    Memastikan ketersediaan slot dan pengelolaan pembatalan.

    Memberikan update terkait jadwal ke Dashboard dan Notification Service.

6. Dashboard Service

    Mengkonsolidasi data dari Friends, Community, Activity, dan Profile Services untuk menampilkan ringkasan personalisasi pada dashboard lansia.

    Menampilkan notifikasi dan jadwal harian.

7. Settings Service

    Mengelola preferensi pengguna seperti tema, ukuran font, dan notifikasi.

    Menyimpan dan menyediakan pengaturan ke front-end.

8. Notification Service

    Mengelola pengiriman notifikasi push dan email untuk pesan, aktivitas, pertemanan, dll.

    Bisa berkomunikasi dengan semua service lain untuk trigger notifikasi.

9. Admin Service

    Memfasilitasi fungsi admin sistem seperti monitoring, manajemen user, komunitas, dan aktivitas.

    Memberikan hak khusus untuk pengelolaan konten dan pengguna.

Komunikasi Antar Microservices

    Semua microservices saling berkomunikasi menggunakan protokol HTTP REST API atau event-driven architecture (misal: message broker seperti Kafka/RabbitMQ) untuk notifikasi dan update data.

    Frontend berinteraksi dengan API Gateway yang meneruskan request ke service yang relevan.

    Database bisa dipisah per service agar terisolasi dan scalable (Database per Service Pattern).