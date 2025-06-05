# config.py
# Konfigurasi dan elemen UI untuk SilverConnect

# =============================================================================
# UI ELEMENTS & EMOJIS
# =============================================================================

class UIElements:
    """Koleksi emoji dan elemen UI untuk customization"""
    
    # Main Icons
    WELCOME = "👋"
    SUCCESS = "✅"
    ERROR = "❌"
    INFO = "ℹ️"
    WARNING = "⚠️"
    CELEBRATION = "🎉"
    
    # Separators & Layout
    SECTION_SEPARATOR = "=" * 60
    SUBSECTION_SEPARATOR = "-" * 40
    
    # Profile & User
    PROFILE = "👤"
    ELDERLY = "👴👵"
    NAME = "📝"
    AGE = "🎂"
    INTERESTS = "❤️"
    
    # Community
    COMMUNITY = "🏘️"
    MEMBERS = "👥"
    DISCUSSION = "💬"
    CATEGORY = "🏷️"
    JOIN = "🤝"
    
    # Activities
    ACTIVITY = "🎯"
    TIME = "🕒"
    LOCATION = "📍"
    CALENDAR = "📅"
    BOOKING = "📋"
    FITNESS = "💪"
    HOBBY = "🎨"
    EDUCATION = "📚"
    
    # Dashboard
    DASHBOARD = "📊"
    NOTIFICATIONS = "🔔"
    SUMMARY = "📄"
    STATS = "📈"
    
    # Actions
    SEARCH = "🔍"
    BROWSE = "👀"
    SELECT = "👆"
    CONFIRM = "✔️"
    CANCEL = "❌"
    QUESTION_MARK = "❓"
    
    # Status
    ACTIVE = "🟢"
    INACTIVE = "🔴"
    PENDING = "🟡"
    
    # Special
    SPARKLE = "✨"
    HEART = "💖"
    STAR = "⭐"
    THUMBS_UP = "👍"

class Messages:
    """Template pesan untuk berbagai situasi"""
    
    WELCOME_MESSAGES = [
        "Selamat datang di SilverConnect!",
        "Halo! Mari bergabung dengan komunitas senior yang hangat",
        "Selamat bergabung di platform khusus untuk Anda"
    ]
    
    SUCCESS_MESSAGES = [
        "Berhasil! Anda telah terdaftar",
        "Sukses! Akun Anda sudah siap",
        "Selamat! Pendaftaran berhasil"
    ]
    
    ERROR_MESSAGES = {
        "empty_username": "Username tidak boleh kosong",
        "empty_password": "Password tidak boleh kosong", 
        "user_exists": "Username sudah digunakan",
        "user_not_found": "Pengguna tidak ditemukan",
        "invalid_choice": "Pilihan tidak valid, silakan coba lagi"
    }
    
    ENCOURAGEMENT = [
        "Jangan khawatir, Anda bisa mencoba lagi!",
        "Tidak apa-apa, mari kita coba sekali lagi",
        "Santai saja, kita akan bantu Anda"
    ]

class AppConfig:
    """Konfigurasi aplikasi"""
    
    # Database simulasi
    DEFAULT_USERS = {
        "elder1": {
            "password_hash": "hashed_pass123",
            "profile_completed": True,
            "full_name": "Pak Budi",
            "age": 65,
            "interests": ["berkebun", "memasak"],
            "activity_level": "moderate"
        }
    }
    
    DEFAULT_COMMUNITIES = [
        {
            "id": 1,
            "name": "Klub Berkebun Jakarta",
            "description": "Komunitas pecinta tanaman untuk berbagi tips berkebun urban dan hidroponik",
            "members": 24,
            "category": "hobi",
            "emoji": "🌱",
            "location": "Jakarta Selatan",
            "meeting_schedule": "Setiap Sabtu pagi"
        },
        {
            "id": 2,
            "name": "Kelompok Baca Sastra",
            "description": "Diskusi buku sastra Indonesia dan dunia, sharing resensi dan cerita",
            "members": 18,
            "category": "edukasi",
            "emoji": "📖",
            "location": "Perpustakaan Kemang",
            "meeting_schedule": "Minggu ke-2 dan ke-4"
        },
        {
            "id": 3,
            "name": "Sehat Bareng Walking Club",
            "description": "Jalan sehat keliling taman, olahraga ringan dan sosialisasi",
            "members": 32,
            "category": "olahraga",
            "emoji": "🚶‍♂️",
            "location": "Taman Menteng",
            "meeting_schedule": "Setiap hari Selasa & Jumat"
        },
        {
            "id": 4,
            "name": "Dapur Nusantara",
            "description": "Berbagi resep masakan tradisional dan tips memasak sehat untuk senior",
            "members": 28,
            "category": "hobi",
            "emoji": "👨‍🍳",
            "location": "Community Center Blok M",
            "meeting_schedule": "Setiap Kamis sore"
        },
        {
            "id": 5,
            "name": "Harmoni Yoga Senior",
            "description": "Kelas yoga khusus senior dengan instruktur berpengalaman",
            "members": 16,
            "category": "kesehatan",
            "emoji": "🧘‍♀️",
            "location": "Studio Yoga Senayan",
            "meeting_schedule": "Senin, Rabu, Jumat pagi"
        },
        {
            "id": 6,
            "name": "Kreasi Seni Senior",
            "description": "Workshop melukis, kerajinan tangan, dan seni untuk mengisi waktu luang",
            "members": 14,
            "category": "kreatif",
            "emoji": "🎨",
            "location": "Sanggar Seni Cikini",
            "meeting_schedule": "Setiap Sabtu sore"
        },
        {
            "id": 7,
            "name": "Tech Savvy Seniors",
            "description": "Belajar teknologi bersama: smartphone, internet, media sosial",
            "members": 12,
            "category": "edukasi",
            "emoji": "📱",
            "location": "Digital Hub PIK",
            "meeting_schedule": "Sabtu pagi"
        }
    ]
    
    DEFAULT_ACTIVITIES = [
        {
            "id": 1,
            "name": "Yoga Sunrise Session",
            "description": "Sesi yoga lembut menyambut matahari terbit dengan gerakan yang mudah",
            "time": "06:30",
            "location": "Taman Menteng",
            "participants": 8,
            "max_participants": 15,
            "difficulty": "mudah",
            "category": "olahraga",
            "emoji": "🧘‍♀️",
            "instructor": "Bu Maya",
            "price": "Gratis",
            "equipment": "Matras disediakan"
        },
        {
            "id": 2,
            "name": "Workshop Masak Rendang",
            "description": "Belajar membuat rendang authentic dengan tips dari chef berpengalaman",
            "time": "10:00",
            "location": "Dapur Komunitas Kemang",
            "participants": 6,
            "max_participants": 12,
            "difficulty": "sedang",
            "category": "hobi",
            "emoji": "👨‍🍳",
            "instructor": "Chef Indra",
            "price": "Rp 75.000",
            "equipment": "Bahan & peralatan tersedia"
        },
        {
            "id": 3,
            "name": "Terapi Lukis Mandala",
            "description": "Sesi melukis mandala untuk relaksasi dan meditasi aktif",
            "time": "14:00",
            "location": "Sanggar Seni Menteng",
            "participants": 4,
            "max_participants": 10,
            "difficulty": "mudah",
            "category": "kreatif",
            "emoji": "🎨",
            "instructor": "Mbak Sari",
            "price": "Rp 50.000", 
            "equipment": "Cat & kanvas disediakan"
        },
        {
            "id": 4,
            "name": "Senam Kursi Ceria",
            "description": "Olahraga ringan yang dilakukan sambil duduk, aman untuk semua kondisi",
            "time": "09:00",
            "location": "Balai RW 05 Menteng",
            "participants": 12,
            "max_participants": 20,
            "difficulty": "mudah",
            "category": "olahraga",
            "emoji": "💺",
            "instructor": "Pak Joko",
            "price": "Gratis",
            "equipment": "Kursi tersedia"
        },
        {
            "id": 5,
            "name": "Urban Gardening Workshop",
            "description": "Belajar berkebun di lahan sempit dengan teknik vertikultur",
            "time": "15:30",
            "location": "Roof Garden Plaza Senayan",
            "participants": 3,
            "max_participants": 8,
            "difficulty": "sedang",
            "category": "hobi",
            "emoji": "🌱",
            "instructor": "Pak Bambang",
            "price": "Rp 100.000",
            "equipment": "Bibit & pot disediakan"
        },
        {
            "id": 6,
            "name": "Digital Literacy for Seniors",
            "description": "Belajar menggunakan WhatsApp, video call, dan aplikasi berguna lainnya",
            "time": "10:30",
            "location": "Lab Komputer PIK",
            "participants": 5,
            "max_participants": 12,
            "difficulty": "mudah",
            "category": "edukasi",
            "emoji": "📱",
            "instructor": "Kak Rina",
            "price": "Rp 25.000",
            "equipment": "Tablet disediakan"
        },
        {
            "id": 7,
            "name": "Jalan Sehat Bundaran HI",
            "description": "Jalan santai keliling area Bundaran HI dilanjutkan sarapan bersama",
            "time": "06:00",
            "location": "Bundaran Hotel Indonesia",
            "participants": 15,
            "max_participants": 30,
            "difficulty": "mudah",
            "category": "olahraga",
            "emoji": "🚶‍♂️",
            "instructor": "Tim Volunteer",
            "price": "Gratis",
            "equipment": "Bawa botol air"
        },
        {
            "id": 8,
            "name": "Diskusi Buku 'Laskar Pelangi'",
            "description": "Diskusi mendalam tentang novel Laskar Pelangi dan pengalaman membaca",
            "time": "13:00",
            "location": "Perpustakaan Cikini",
            "participants": 7,
            "max_participants": 15,
            "difficulty": "mudah",
            "category": "edukasi",
            "emoji": "📚",
            "instructor": "Bu Dewi",
            "price": "Gratis",
            "equipment": "Bawa buku sendiri"
        }
    ]
    
    # Pengaturan UI
    SEPARATOR_LENGTH = 60
    SECTION_SEPARATOR = "=" * SEPARATOR_LENGTH
    SUBSECTION_SEPARATOR = "-" * 40
    
    # Pilihan aktivitas berdasarkan level
    ACTIVITY_LEVELS = {
        "ringan": ["Senam Kursi", "Terapi Seni", "Kelas Masak Sehat"],
        "sedang": ["Yoga Pagi", "Berkebun Bersama", "Jalan Santai"],
        "aktif": ["Jalan Cepat", "Senam Aerobik", "Bersepeda"]
    }
    
    # Template notifikasi
    NOTIFICATION_TEMPLATES = [
        "Selamat datang di SilverConnect! Lengkapi profil untuk rekomendasi terbaik",
        "Ada anggota baru yang bergabung di komunitas Anda",
        "Pengingat: Tetap terhidrasi dan istirahat saat beraktivitas",
        "Jangan lupa aktivitas {activity_name} hari ini pukul {time}",
        "Komunitas {community_name} mengadakan diskusi menarik!"
    ]