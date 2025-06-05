# silverconnect_main.py
# Main facade yang menggabungkan semua modul SilverConnect

import time
from typing import Dict, List, Optional

# Import semua facade modules
from config import UIElements, Messages, AppConfig
from auth_facade import AuthFacade
from community_facade import CommunityFacade
from activity_facade import ActivityFacade
from dashboard_facade import DashboardFacade

class SilverConnectFacade:
    """Main facade yang mengordinasikan semua sistem SilverConnect"""
    
    def __init__(self):
        self.ui = UIElements()
        self.messages = Messages()
        
        print(self.ui.SECTION_SEPARATOR)
        print("SILVERCONNECT PLATFORM - MODULAR FACADE PATTERN")
        print(self.ui.SECTION_SEPARATOR)
        print(f"{self.ui.SPARKLE} Menginisialisasi SilverConnect Platform...")
        print()
        
        # Initialize all facade modules
        self.auth_facade = AuthFacade()
        self.community_facade = CommunityFacade()
        self.activity_facade = ActivityFacade()
        self.dashboard_facade = DashboardFacade()
        
        # Current session data
        self.current_user = None
        self.current_user_data = None
        self.session_data = {}
        
        print(f"\n{self.ui.CELEBRATION} SilverConnect Platform siap digunakan!")
        print(f"{self.ui.HEART} Platform yang dirancang khusus untuk kesejahteraan senior")
        print()
    
    def interactive_complete_journey(self) -> Dict:
        """Journey lengkap dari signup hingga penggunaan platform"""
        
        print(f"{self.ui.WELCOME} Selamat datang di SilverConnect!")
        print("Platform sosial yang dirancang khusus untuk para senior")
        print("Mari kita mulai perjalanan Anda menuju kehidupan yang lebih aktif dan terhubung!")
        print()
        
        # Step 1: Signup Process
        print(f"{self.ui.STAR} LANGKAH 1: PENDAFTARAN AKUN")
        signup_result = self.auth_facade.interactive_signup()
        
        if not signup_result["success"]:
            print(f"{self.ui.ERROR} Pendaftaran gagal. Mari coba lagi.")
            return signup_result
        
        self.current_user = signup_result["username"]
        self.current_user_data = signup_result["user_data"]
        
        # Step 2: Profile Setup
        print(f"\n{self.ui.STAR} LANGKAH 2: SETUP PROFIL LENGKAP")
        profile_result = self.auth_facade.interactive_profile_setup(self.current_user)
        
        if profile_result["success"]:
            self.current_user_data.update({
                "interests": profile_result["interests"],
                "activity_level": profile_result["activity_level"],
                "preferences": profile_result["preferences"]
            })
        
        # Step 3: Community Exploration
        print(f"\n{self.ui.STAR} LANGKAH 3: JELAJAHI KOMUNITAS")
        print("Sekarang mari kita cari komunitas yang sesuai dengan minat Anda!")
        
        community_result = self.community_facade.interactive_browse_and_join(
            self.current_user,
            self.current_user_data.get("interests", [])
        )
        
        communities = []
        if community_result["success"]:
            communities = [community_result["membership"]]
        
        # Step 4: Activity Discovery
        print(f"\n{self.ui.STAR} LANGKAH 4: TEMUKAN AKTIVITAS")
        print("Mari temukan aktivitas yang tepat untuk Anda!")
        
        activity_result = self.activity_facade.interactive_find_and_book(
            self.current_user,
            self.current_user_data.get("activity_level", "sedang"),
            self.current_user_data.get("interests", [])
        )
        
        activities = []
        if activity_result["success"]:
            activities = [activity_result["booking"]]
        
        # Step 5: Dashboard Overview
        print(f"\n{self.ui.STAR} LANGKAH 5: DASHBOARD PERSONAL ANDA")
        
        dashboard_result = self.dashboard_facade.show_personalized_summary(
            self.current_user,
            self.current_user_data,
            communities,
            activities
        )
        
        # Completion Summary
        self._show_completion_summary(communities, activities)
        
        return {
            "success": True,
            "message": "Journey lengkap berhasil diselesaikan!",
            "user": self.current_user,
            "user_data": self.current_user_data,
            "communities": communities,
            "activities": activities,
            "dashboard": dashboard_result
        }
    
    def interactive_main_menu(self) -> Dict:
        """Menu utama interaktif untuk user yang sudah login"""
        
        if not self.current_user:
            print(f"{self.ui.WARNING} Silakan login terlebih dahulu")
            return {"success": False, "message": "User not logged in"}
        
        while True:
            print(f"\n{self.ui.SECTION_SEPARATOR}")
            print(f"{self.ui.DASHBOARD} MENU UTAMA SILVERCONNECT")
            print(f"{self.ui.SECTION_SEPARATOR}")
            print(f"Selamat datang kembali, {self.current_user_data.get('full_name', self.current_user)}!")
            print()
            
            print("Apa yang ingin Anda lakukan hari ini?")
            print(f"[1] {self.ui.DASHBOARD} Lihat Dashboard")
            print(f"[2] {self.ui.COMMUNITY} Jelajahi Komunitas")
            print(f"[3] {self.ui.ACTIVITY} Cari Aktivitas")
            print(f"[4] {self.ui.CALENDAR} Kelola Jadwal")
            print(f"[5] {self.ui.PROFILE} Update Profil")
            print(f"[6] {self.ui.STATS} Laporan Mingguan")
            print(f"[7] {self.ui.FITNESS} Dashboard Kesehatan")
            print(f"[8] {self.ui.SPARKLE} Rekomendasi Personal")
            print(f"[9] {self.ui.CANCEL} Keluar")
            
            choice = input(f"\n{self.ui.SELECT} Pilihan Anda (1-9): ").strip()
            
            if choice == "1":
                self._show_current_dashboard()
            elif choice == "2":
                self._explore_communities()
            elif choice == "3":
                self._find_activities()
            elif choice == "4":
                self._manage_schedule()
            elif choice == "5":
                self._update_profile()
            elif choice == "6":
                self._show_weekly_report()
            elif choice == "7":
                self._show_health_dashboard()
            elif choice == "8":
                self._show_recommendations()
            elif choice == "9":
                print(f"\n{self.ui.HEART} Terima kasih telah menggunakan SilverConnect!")
                print("Sampai jumpa lagi! Jaga kesehatan dan tetap aktif!")
                return {"success": True, "message": "User logged out"}
            else:
                print(f"{self.ui.WARNING} Pilihan tidak valid. Silakan pilih 1-9.")
    
    def quick_demo_mode(self) -> Dict:
        """Mode demo cepat untuk showcase"""
        
        print(f"\n{self.ui.SPARKLE} MODE DEMO CEPAT SILVERCONNECT")
        print("Demonstrasi fitur-fitur utama platform dalam mode singkat")
        print()
        
        # Simulasi user data
        demo_user = "demo_user"
        demo_data = {
            "full_name": "Pak Demo",
            "age": 68,
            "interests": ["berkebun", "jalan kaki", "memasak"],
            "activity_level": "sedang",
            "profile_completed": True
        }
        
        demo_communities = [{
            "community_id": 1,
            "community_name": "Klub Berkebun",
            "joined_date": "2025-06-01"
        }]
        
        demo_activities = [{
            "activity_name": "Yoga Pagi",
            "activity_time": "07:00",
            "activity_location": "Taman Komunitas",
            "status": "confirmed"
        }]
        
        # Demo dashboard
        print(f"{self.ui.STAR} 1. DASHBOARD PERSONAL")
        self.dashboard_facade.show_personalized_summary(
            demo_user, demo_data, demo_communities, demo_activities
        )
        
        input(f"\n{self.ui.INFO} Tekan Enter untuk melanjutkan...")
        
        # Demo recommendations
        print(f"\n{self.ui.STAR} 2. REKOMENDASI AKTIVITAS")
        self.activity_facade.get_activity_recommendations(demo_user, demo_data)
        
        input(f"\n{self.ui.INFO} Tekan Enter untuk melanjutkan...")
        
        # Demo health dashboard
        print(f"\n{self.ui.STAR} 3. DASHBOARD KESEHATAN")
        self.dashboard_facade.show_health_dashboard(demo_user, demo_data)
        
        print(f"\n{self.ui.CELEBRATION} Demo selesai! Ini adalah gambaran pengalaman SilverConnect")
        
        return {"success": True, "message": "Demo completed"}
    
    def show_facade_architecture(self):
        """Tampilkan arsitektur facade pattern yang digunakan"""
        
        print(f"\n{self.ui.SECTION_SEPARATOR}")
        print("ARSITEKTUR MODULAR FACADE PATTERN")
        print(f"{self.ui.SECTION_SEPARATOR}")
        
        print(f"\n{self.ui.SPARKLE} STRUKTUR MODULAR:")
        print("📁 SilverConnect Project")
        print("├── 📄 config.py          - Konfigurasi, UI elements, data")
        print("├── 📄 auth_facade.py     - Autentikasi & profil")
        print("├── 📄 community_facade.py- Komunitas & membership")
        print("├── 📄 activity_facade.py - Aktivitas & booking")
        print("├── 📄 dashboard_facade.py- Dashboard & laporan")
        print("└── 📄 silverconnect_main.py - Main facade coordinator")
        
        print(f"\n{self.ui.STAR} KEUNTUNGAN MODULAR:")
        print("• Setiap modul bisa dikembangkan independen")
        print("• Mudah menambah fitur baru (emoji, tema, dll)")
        print("• Code reusability tinggi")
        print("• Testing lebih mudah per modul")
        print("• Maintenance lebih efisien")
        print("• Tim bisa bekerja parallel pada modul berbeda")
        
        print(f"\n{self.ui.HEART} CUSTOMIZATION YANG MUDAH:")
        print("• Ganti emoji di config.py")
        print("• Tambah bahasa baru dengan mengubah Messages")
        print("• Modifikasi UI tanpa mengubah logic bisnis")
        print("• Tambah fitur baru tanpa merusak yang existing")
        
        print(f"\n{self.ui.CELEBRATION} PERFECT FOR SCALING:")
        print("• Bisa dipecah menjadi microservices")
        print("• Database bisa dipisah per domain")
        print("• API bisa dibuat per facade")
        print("• Mobile app bisa menggunakan facade yang sama")
    
    # Private methods untuk menu actions
    
    def _show_current_dashboard(self):
        """Tampilkan dashboard saat ini"""
        communities = self.community_facade.user_memberships.get(self.current_user, [])
        activities = self.activity_facade.user_bookings.get(self.current_user, [])
        
        self.dashboard_facade.show_personalized_summary(
            self.current_user, self.current_user_data, communities, activities
        )
    
    def _explore_communities(self):
        """Jelajahi komunitas"""
        self.community_facade.interactive_browse_and_join(
            self.current_user,
            self.current_user_data.get("interests", [])
        )
    
    def _find_activities(self):
        """Cari aktivitas baru"""
        self.activity_facade.interactive_find_and_book(
            self.current_user,
            self.current_user_data.get("activity_level", "sedang"),
            self.current_user_data.get("interests", [])
        )
    
    def _manage_schedule(self):
        """Kelola jadwal aktivitas"""
        self.activity_facade.interactive_manage_bookings(self.current_user)
    
    def _update_profile(self):
        """Update profil user"""
        print(f"\n{self.ui.PROFILE} UPDATE PROFIL")
        print("Fitur update profil akan tersedia dalam versi selanjutnya!")
        print("Untuk sekarang, Anda bisa membuat akun baru untuk mengubah profil.")
    
    def _show_weekly_report(self):
        """Tampilkan laporan mingguan"""
        self.dashboard_facade.show_weekly_report(self.current_user, self.current_user_data)
    
    def _show_health_dashboard(self):
        """Tampilkan dashboard kesehatan"""
        self.dashboard_facade.show_health_dashboard(self.current_user, self.current_user_data)
    
    def _show_recommendations(self):
        """Tampilkan rekomendasi personal"""
        print(f"\n{self.ui.SPARKLE} REKOMENDASI PERSONAL UNTUK ANDA")
        
        # Rekomendasi aktivitas
        self.activity_facade.get_activity_recommendations(self.current_user, self.current_user_data)
        
        # Rekomendasi komunitas
        print(f"\n{self.ui.COMMUNITY} Rekomendasi Komunitas:")
        interests = self.current_user_data.get("interests", [])
        if "seni" in interests:
            print(f"  {self.ui.SPARKLE} Komunitas Seni & Kreatif - Cocok untuk Anda!")
        if "membaca" in interests:
            print(f"  {self.ui.SPARKLE} Kelompok Diskusi Buku - Bergabunglah sekarang!")
        if not interests:
            print(f"  {self.ui.INFO} Lengkapi profil untuk rekomendasi yang lebih baik")
    
    def _show_completion_summary(self, communities: List[Dict], activities: List[Dict]):
        """Tampilkan ringkasan penyelesaian setup"""
        
        print(f"\n{self.ui.SECTION_SEPARATOR}")
        print(f"{self.ui.CELEBRATION} SETUP SILVERCONNECT BERHASIL! {self.ui.CELEBRATION}")
        print(f"{self.ui.SECTION_SEPARATOR}")
        
        print(f"{self.ui.SUCCESS} Yang telah Anda lakukan:")
        print(f"  {self.ui.PROFILE} Akun dibuat: {self.current_user_data.get('full_name')}")
        print(f"  {self.ui.INTERESTS} Profil dilengkapi dengan {len(self.current_user_data.get('interests', []))} minat")
        print(f"  {self.ui.COMMUNITY} Komunitas bergabung: {len(communities)}")
        print(f"  {self.ui.ACTIVITY} Aktivitas dibooking: {len(activities)}")
        print()
        
        print(f"{self.ui.SPARKLE} MANFAAT FACADE PATTERN YANG ANDA RASAKAN:")
        print("• Proses setup yang mudah dan terintegrasi")
        print("• Tidak perlu memahami kompleksitas sistem internal")
        print("• Panduan step-by-step yang ramah senior")
        print("• Error handling yang konsisten dan membantu")
        print("• Interface yang sederhana namun powerful")
        print()
        
        print(f"{self.ui.HEART} Selamat! Anda siap menikmati SilverConnect!")
        print("Platform ini akan membantu Anda tetap aktif, sehat, dan terhubung.")

# =============================================================================
# MAIN EXECUTION FUNCTION
# =============================================================================

def main():
    """Fungsi utama untuk menjalankan SilverConnect"""
    
    # Buat instance main facade
    silverconnect = SilverConnectFacade()
    
    print("Pilih mode yang ingin Anda jalankan:")
    print(f"[1] {silverconnect.ui.SPARKLE} Journey lengkap (setup dari awal)")
    print(f"[2] {silverconnect.ui.DASHBOARD} Demo cepat (preview fitur)")
    print(f"[3] {silverconnect.ui.STAR} Lihat arsitektur modular")
    print(f"[4] {silverconnect.ui.CANCEL} Keluar")
    
    choice = input(f"\n{silverconnect.ui.SELECT} Pilihan Anda: ").strip()
    
    if choice == "1":
        # Journey lengkap
        result = silverconnect.interactive_complete_journey()
        
        if result["success"]:
            # Setelah setup, masuk ke main menu
            continue_choice = input(f"\n{silverconnect.ui.SELECT} Lanjut ke menu utama? (y/n): ").strip().lower()
            if continue_choice == 'y':
                silverconnect.interactive_main_menu()
        
    elif choice == "2":
        # Demo mode
        silverconnect.quick_demo_mode()
        
    elif choice == "3":
        # Arsitektur info
        silverconnect.show_facade_architecture()
        
    else:
        print(f"\n{silverconnect.ui.HEART} Terima kasih telah menjelajahi SilverConnect!")
        print("Platform modular yang membuat hidup senior lebih terhubung dan bermakna.")

if __name__ == "__main__":
    main()