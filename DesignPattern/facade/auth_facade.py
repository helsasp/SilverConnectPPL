# auth_facade.py
# Modul facade untuk autentikasi dan manajemen profil

import hashlib
import time
from typing import Dict, List, Optional
from config import UIElements, Messages, AppConfig

class AuthFacade:
    """Facade untuk sistem autentikasi dan profil pengguna"""
    
    def __init__(self):
        self.users_db = AppConfig.DEFAULT_USERS.copy()
        self.ui = UIElements()
        self.messages = Messages()
        print(f"[AuthFacade] {self.ui.SUCCESS} Sistem autentikasi siap")
    
    def interactive_signup(self) -> Dict:
        """Proses pendaftaran interaktif dengan UI yang ramah senior"""
        
        print(f"\n{self.ui.SECTION_SEPARATOR}")
        print(f"{self.ui.PROFILE} PROSES PENDAFTARAN {self.ui.PROFILE}")
        print(f"{self.ui.SECTION_SEPARATOR}")
        
        # Input username dengan validasi
        username = self._get_username()
        if not username:
            return self._create_error_response("Username tidak valid")
        
        # Input password dengan validasi
        password = self._get_password()
        if not password:
            return self._create_error_response("Password tidak valid")
        
        # Input data profil
        profile_data = self._get_profile_data()
        
        print(f"\n{self.ui.INFO} Membuat akun untuk '{username}'...")
        
        # Cek apakah username sudah ada
        if username in self.users_db:
            error_msg = self.messages.ERROR_MESSAGES["user_exists"]
            print(f"{self.ui.ERROR} {error_msg}")
            return self._create_error_response(error_msg)
        
        # Buat user baru
        self.users_db[username] = {
            "password_hash": self._hash_password(password),
            "profile_completed": False,
            "full_name": profile_data["full_name"],
            "age": profile_data["age"],
            "created_at": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        success_msg = f"Akun berhasil dibuat untuk {profile_data['full_name']}!"
        print(f"\n{self.ui.SUCCESS} {success_msg}")
        print(f"{self.ui.SPARKLE} Selamat bergabung di SilverConnect!")
        
        return {
            "success": True,
            "message": success_msg,
            "username": username,
            "user_data": self.users_db[username]
        }
    
    def interactive_profile_setup(self, username: str) -> Dict:
        """Setup profil lengkap dengan minat dan preferensi"""
        
        if username not in self.users_db:
            return self._create_error_response(self.messages.ERROR_MESSAGES["user_not_found"])
        
        print(f"\n{self.ui.SECTION_SEPARATOR}")
        print(f"{self.ui.SPARKLE} SETUP PROFIL UNTUK {username.upper()} {self.ui.SPARKLE}")
        print(f"{self.ui.SECTION_SEPARATOR}")
        print("Mari lengkapi profil Anda untuk mendapatkan rekomendasi yang tepat:")
        
        # Input minat/hobi
        interests = self._get_user_interests()
        
        # Input level aktivitas
        activity_level = self._get_activity_level()
        
        # Input preferensi tambahan
        additional_prefs = self._get_additional_preferences()
        
        # Update profil
        self.users_db[username].update({
            "profile_completed": True,
            "interests": interests,
            "activity_level": activity_level,
            "preferences": additional_prefs,
            "profile_updated_at": time.strftime("%Y-%m-%d %H:%M:%S")
        })
        
        print(f"\n{self.ui.SUCCESS} Profil berhasil dilengkapi!")
        print(f"{self.ui.INTERESTS} Minat: {', '.join(interests)}")
        print(f"{self.ui.FITNESS} Level Aktivitas: {activity_level}")
        print(f"{self.ui.HEART} Terima kasih! Sekarang kami bisa memberikan rekomendasi terbaik")
        
        return {
            "success": True,
            "message": "Profil berhasil dilengkapi!",
            "interests": interests,
            "activity_level": activity_level,
            "preferences": additional_prefs
        }
    
    def login(self, username: str, password: str) -> Dict:
        """Login sederhana untuk demo"""
        if username in self.users_db:
            stored_hash = self.users_db[username]["password_hash"]
            if stored_hash == self._hash_password(password):
                print(f"{self.ui.SUCCESS} Selamat datang kembali, {self.users_db[username]['full_name']}!")
                return {
                    "success": True,
                    "message": "Login berhasil",
                    "user_data": self.users_db[username]
                }
        
        return self._create_error_response("Username atau password salah")
    
    def get_user_data(self, username: str) -> Optional[Dict]:
        """Ambil data user"""
        return self.users_db.get(username)
    
    # Private methods untuk input validation dan formatting
    
    def _get_username(self) -> str:
        """Input username dengan validasi"""
        while True:
            username = input(f"{self.ui.PROFILE} Masukkan username: ").strip()
            if username:
                return username
            print(f"{self.ui.WARNING} Username tidak boleh kosong. Silakan coba lagi.")
    
    def _get_password(self) -> str:
        """Input password dengan validasi"""
        while True:
            password = input(f"{self.ui.CONFIRM} Masukkan password: ").strip()
            if len(password) >= 4:
                return password
            print(f"{self.ui.WARNING} Password minimal 4 karakter. Silakan coba lagi.")
    
    def _get_profile_data(self) -> Dict:
        """Input data profil dasar"""
        print(f"\n{self.ui.INFO} Mari lengkapi profil dasar Anda:")
        
        full_name = input(f"{self.ui.NAME} Nama lengkap: ").strip()
        if not full_name:
            full_name = "Pengguna Baru"
        
        while True:
            age_input = input(f"{self.ui.AGE} Usia: ").strip()
            if age_input.isdigit() and 40 <= int(age_input) <= 100:
                age = int(age_input)
                break
            else:
                print(f"{self.ui.WARNING} Masukkan usia antara 40-100 tahun")
        
        return {"full_name": full_name, "age": age}
    
    def _get_user_interests(self) -> List[str]:
        """Input minat/hobi pengguna dengan pilihan yang lebih lengkap"""
        print(f"\n{self.ui.INTERESTS} Apa minat dan hobi Anda?")
        print("Pilih dengan mengetik nomor (pisahkan dengan koma untuk pilihan ganda):")
        print("Contoh: 1,3,5 untuk memilih berkebun, membaca, dan yoga")
        
        available_interests = [
            ("berkebun", "🌱", "Menanam, merawat tanaman, hidroponik"),
            ("memasak", "👨‍🍳", "Masak tradisional, resep sehat, kue"),
            ("membaca", "📚", "Novel, biografi, majalah, koran"),
            ("jalan kaki", "🚶‍♂️", "Jalan santai, trekking ringan, nature walk"),
            ("yoga", "🧘‍♀️", "Yoga, meditasi, mindfulness"),
            ("seni", "🎨", "Melukis, menggambar, kerajinan tangan"),
            ("musik", "🎵", "Mendengarkan musik, bernyanyi, karaoke"),
            ("fotografi", "📸", "Foto pemandangan, portrait, smartphone photography"),
            ("menulis", "✍️", "Diary, blog, cerita, puisi"),
            ("bermain kartu", "🃏", "Remi, bridge, poker, permainan kartu"),
            ("catur", "♟️", "Catur klasik, catur online"),
            ("berkumpul dengan keluarga", "👨‍👩‍👧‍👦", "Quality time dengan cucu, family gathering"),
            ("menonton film", "🎬", "Film klasik, drama, dokumenter"),
            ("crafting", "🎭", "Rajut, sulam, origami, DIY projects"),
            ("teknologi", "📱", "Belajar gadget, internet, media sosial"),
            ("travelling", "✈️", "Wisata domestik, city tour, culinary tour"),
            ("olahraga ringan", "🏃‍♂️", "Senam, renang, badminton"),
            ("berkebun vertikal", "🪴", "Urban farming, tanaman hias indoor"),
            ("memasak kue", "🧁", "Baking, decorating cake, pastry"),
            ("bahasa asing", "🗣️", "Belajar English, Mandarin, Jepang")
        ]
        
        # Tampilkan pilihan dalam 2 kolom untuk readability
        print()
        for i in range(0, len(available_interests), 2):
            left = available_interests[i]
            left_text = f"[{i+1:2d}] {left[1]} {left[0].title():<20}"
            
            if i+1 < len(available_interests):
                right = available_interests[i+1]
                right_text = f"[{i+2:2d}] {right[1]} {right[0].title()}"
                print(f"{left_text} {right_text}")
            else:
                print(left_text)
        
        print(f"\n💡 Tip: Pilih 3-5 minat untuk mendapatkan rekomendasi terbaik!")
        
        while True:
            choices = input(f"\n{self.ui.SELECT} Pilihan Anda (contoh: 1,3,5,7): ").strip()
            
            if not choices:
                print(f"{self.ui.WARNING} Silakan pilih minimal satu minat")
                continue
                
            try:
                indices = [int(x.strip()) - 1 for x in choices.split(",")]
                selected_interests = []
                
                for i in indices:
                    if 0 <= i < len(available_interests):
                        interest_name = available_interests[i][0]
                        selected_interests.append(interest_name)
                    else:
                        print(f"{self.ui.WARNING} Pilihan {i+1} tidak valid (harus 1-{len(available_interests)})")
                        break
                else:  # Hanya execute jika tidak ada break
                    if selected_interests:
                        # Konfirmasi pilihan
                        print(f"\n{self.ui.SUCCESS} Minat yang Anda pilih:")
                        for interest in selected_interests:
                            emoji = next((item[1] for item in available_interests if item[0] == interest), "❤️")
                            description = next((item[2] for item in available_interests if item[0] == interest), "")
                            print(f"  {emoji} {interest.title()} - {description}")
                        
                        confirm = input(f"\n{self.ui.CONFIRM} Apakah pilihan sudah benar? (y/n): ").strip().lower()
                        if confirm == 'y':
                            return selected_interests
                        else:
                            print("Silakan pilih ulang:")
                            continue
                    else:
                        print(f"{self.ui.WARNING} Pilih minimal satu minat")
                        continue
                        
            except ValueError:
                print(f"{self.ui.WARNING} Format tidak valid. Gunakan angka dipisah koma (contoh: 1,3,5)")
                continue
    
    def _get_activity_level(self) -> str:
        """Input level aktivitas dengan pilihan yang jelas"""
        print(f"\n{self.ui.FITNESS} Bagaimana level aktivitas fisik yang Anda sukai?")
        print(f"[1] {self.ui.INACTIVE} Ringan (duduk, gerakan lembut)")
        print(f"[2] {self.ui.PENDING} Sedang (jalan kaki, olahraga ringan)")
        print(f"[3] {self.ui.ACTIVE} Aktif (olahraga teratur, aktivitas energik)")
        
        while True:
            choice = input(f"{self.ui.SELECT} Pilih (1-3): ").strip()
            if choice == "1":
                return "ringan"
            elif choice == "2":
                return "sedang"
            elif choice == "3":
                return "aktif"
            else:
                print(f"{self.ui.WARNING} Pilih angka 1, 2, atau 3")
    
    def _get_additional_preferences(self) -> Dict:
        """Input preferensi tambahan"""
        print(f"\n{self.ui.INFO} Beberapa pertanyaan tambahan (opsional):")
        
        # Waktu preferensi
        print("Kapan waktu terbaik untuk beraktivitas?")
        print("[1] Pagi (07:00-10:00) [2] Siang (10:00-14:00) [3] Sore (14:00-18:00)")
        time_pref = input("Pilihan waktu: ").strip()
        time_map = {"1": "pagi", "2": "siang", "3": "sore"}
        preferred_time = time_map.get(time_pref, "pagi")
        
        # Preferensi sosial
        social_pref = input("Lebih suka aktivitas berkelompok? (y/n): ").strip().lower()
        prefers_group = social_pref == "y"
        
        return {
            "preferred_time": preferred_time,
            "prefers_group_activities": prefers_group,
            "notification_enabled": True
        }
    
    def _get_interest_emoji(self, interest: str) -> str:
        """Dapatkan emoji untuk minat tertentu"""
        emoji_map = {
            "berkebun": "🌱", "memasak": "👨‍🍳", "membaca": "📚",
            "jalan kaki": "🚶‍♂️", "yoga": "🧘‍♀️", "seni": "🎨",
            "musik": "🎵", "fotografi": "📸", "menulis": "✍️",
            "bermain kartu": "🃏", "catur": "♟️", "berkumpul dengan keluarga": "👨‍👩‍👧‍👦",
            "menonton film": "🎬", "crafting/kerajinan": "🎭"
        }
        return emoji_map.get(interest, self.ui.HEART)
    
    def _hash_password(self, password: str) -> str:
        """Hash password sederhana untuk demo"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def _create_error_response(self, message: str) -> Dict:
        """Buat response error yang konsisten"""
        return {"success": False, "message": message}