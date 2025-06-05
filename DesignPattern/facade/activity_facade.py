# activity_facade.py
# Modul facade untuk manajemen aktivitas dan booking

import time
import random
from typing import Dict, List, Optional
from config import UIElements, Messages, AppConfig

class ActivityFacade:
    """Facade untuk sistem aktivitas dan booking"""
    
    def __init__(self):
        self.activities_db = AppConfig.DEFAULT_ACTIVITIES.copy()
        self.user_bookings = {}
        self.activity_schedule = {}
        self.ui = UIElements()
        self.messages = Messages()
        print(f"[ActivityFacade] {self.ui.SUCCESS} Sistem aktivitas siap")
    
    def interactive_find_and_book(self, username: str, activity_level: str = "sedang", 
                                  user_interests: List[str] = None) -> Dict:
        """Cari dan booking aktivitas secara interaktif"""
        
        print(f"\n{self.ui.SECTION_SEPARATOR}")
        print(f"{self.ui.ACTIVITY} PENCARI AKTIVITAS UNTUK {username.upper()} {self.ui.ACTIVITY}")
        print(f"{self.ui.SECTION_SEPARATOR}")
        
        print(f"{self.ui.SEARCH} Mencari aktivitas yang sesuai untuk Anda...")
        print(f"Level aktivitas: {activity_level}")
        if user_interests:
            print(f"Berdasarkan minat: {', '.join(user_interests)}")
        print()
        
        # Filter aktivitas berdasarkan level dan minat
        suitable_activities = self._filter_activities_by_level(activity_level)
        
        if user_interests:
            recommended_activities = self._get_recommended_activities(user_interests, suitable_activities)
            if recommended_activities:
                print(f"{self.ui.SPARKLE} Rekomendasi khusus untuk Anda:")
                for activity in recommended_activities[:2]:
                    emoji = activity.get("emoji", self.ui.ACTIVITY)
                    available_spots = activity.get('max_participants', 20) - activity.get('participants', 0)
                    print(f"  ⭐ {emoji} {activity['name']} - {activity['time']} | {available_spots} tempat tersisa")
                print()
        
        # Tampilkan semua aktivitas yang sesuai dengan detail lengkap
        print(f"{self.ui.BROWSE} Aktivitas Tersedia Hari Ini:")
        print()
        
        for i, activity in enumerate(suitable_activities, 1):
            emoji = activity.get("emoji", self.ui.ACTIVITY)
            booking_status = self._get_booking_status(username, activity["id"])
            status_icon = self.ui.SUCCESS if booking_status == "booked" else ""
            
            available_spots = activity.get('max_participants', 20) - activity.get('participants', 0)
            price = activity.get('price', 'Gratis')
            instructor = activity.get('instructor', 'TBA')
            
            print(f"[{i}] {emoji} {activity['name']} {status_icon}")
            print(f"    🕒 Waktu: {activity['time']} | 📍 Lokasi: {activity['location']}")
            print(f"    👨‍🏫 Instruktur: {instructor} | 💰 Biaya: {price}")
            print(f"    👥 {activity['participants']}/{activity.get('max_participants', 20)} peserta | ⚡ Level: {activity['difficulty']}")
            print(f"    📝 {activity['description']}")
            
            if available_spots <= 0:
                print(f"    🚫 Penuh - tidak ada tempat tersisa")
            elif available_spots <= 3:
                print(f"    ⚠️  Hampir penuh - {available_spots} tempat tersisa")
            else:
                print(f"    ✅ Tersedia - {available_spots} tempat tersisa")
                
            if booking_status == "booked":
                print(f"    {self.ui.SUCCESS} Anda sudah booking aktivitas ini")
            
            print()
        
        # Input pilihan aktivitas dengan validasi
        while True:
            choice = input(f"{self.ui.SELECT} Pilih aktivitas untuk melihat detail (1-{len(suitable_activities)}) atau 'q' untuk keluar: ").strip()
            
            if choice.lower() == 'q':
                return {"success": False, "message": "User membatalkan pemilihan aktivitas"}
            
            try:
                choice_num = int(choice)
                if 1 <= choice_num <= len(suitable_activities):
                    selected_activity = suitable_activities[choice_num - 1]
                    break
                else:
                    print(f"{self.ui.WARNING} Pilihan tidak valid. Masukkan angka 1-{len(suitable_activities)} atau 'q'")
            except ValueError:
                print(f"{self.ui.WARNING} Masukkan angka yang valid atau 'q' untuk keluar")
        
        # Tampilkan detail dan booking
        return self._show_activity_details_and_book(username, selected_activity)
    
    def show_user_schedule(self, username: str) -> Dict:
        """Tampilkan jadwal aktivitas user"""
        
        user_bookings = self.user_bookings.get(username, [])
        
        if not user_bookings:
            print(f"{self.ui.INFO} Anda belum memiliki aktivitas yang dibooking")
            return {"success": False, "message": "Belum ada booking"}
        
        print(f"\n{self.ui.CALENDAR} Jadwal Aktivitas Anda:")
        print()
        
        # Urutkan berdasarkan waktu
        sorted_bookings = sorted(user_bookings, key=lambda x: x["activity_time"])
        
        for booking in sorted_bookings:
            emoji = self._get_activity_emoji(booking.get("category", ""))
            status_color = self.ui.SUCCESS if booking["status"] == "confirmed" else self.ui.PENDING
            
            print(f"{emoji} {booking['activity_name']}")
            print(f"    {self.ui.TIME} {booking['activity_time']} | {self.ui.LOCATION} {booking['activity_location']}")
            print(f"    {self.ui.BOOKING} Status: {status_color} {booking['status']}")
            print(f"    {self.ui.CALENDAR} Dibooking: {booking['booking_date']}")
            print()
        
        return {"success": True, "bookings": user_bookings}
    
    def interactive_manage_bookings(self, username: str) -> Dict:
        """Kelola booking aktivitas"""
        
        user_bookings = self.user_bookings.get(username, [])
        if not user_bookings:
            print(f"{self.ui.WARNING} Anda belum memiliki booking aktivitas")
            return {"success": False, "message": "Belum ada booking"}
        
        print(f"\n{self.ui.BOOKING} KELOLA BOOKING AKTIVITAS")
        print("Pilih aksi yang ingin dilakukan:")
        print(f"[1] {self.ui.BROWSE} Lihat semua booking")
        print(f"[2] {self.ui.CANCEL} Batalkan booking")
        print(f"[3] {self.ui.TIME} Reschedule booking")
        print(f"[4] {self.ui.SUMMARY} Lihat detail aktivitas")
        print(f"[5] {self.ui.CANCEL} Kembali")
        
        choice = input(f"{self.ui.SELECT} Pilihan Anda: ").strip()
        
        if choice == "1":
            return self.show_user_schedule(username)
        elif choice == "2":
            return self._cancel_booking(username)
        elif choice == "3":
            return self._reschedule_booking(username)
        elif choice == "4":
            return self._view_booking_details(username)
        else:
            return {"success": False, "message": "Kembali ke menu utama"}
    
    def get_activity_recommendations(self, username: str, user_data: Dict) -> Dict:
        """Berikan rekomendasi aktivitas personal"""
        
        print(f"\n{self.ui.SPARKLE} REKOMENDASI AKTIVITAS PERSONAL")
        
        interests = user_data.get("interests", [])
        activity_level = user_data.get("activity_level", "sedang")
        preferences = user_data.get("preferences", {})
        
        # Filter berdasarkan preferensi waktu
        preferred_time = preferences.get("preferred_time", "pagi")
        time_filtered_activities = self._filter_by_time_preference(preferred_time)
        
        # Filter berdasarkan level aktivitas
        level_filtered = self._filter_activities_by_level(activity_level)
        
        # Gabungkan dan ranking
        recommended = []
        for activity in self.activities_db:
            score = self._calculate_recommendation_score(activity, interests, activity_level, preferences)
            if score > 0.3:  # Threshold minimum
                recommended.append((activity, score))
        
        # Urutkan berdasarkan score
        recommended.sort(key=lambda x: x[1], reverse=True)
        
        print(f"\n{self.ui.STAR} Top 3 Rekomendasi untuk Anda:")
        for i, (activity, score) in enumerate(recommended[:3], 1):
            emoji = activity.get("emoji", self.ui.ACTIVITY)
            match_percentage = int(score * 100)
            print(f"[{i}] {emoji} {activity['name']} - {match_percentage}% cocok")
            print(f"    {activity['description']}")
            print(f"    {self.ui.TIME} {activity['time']} | {self.ui.LOCATION} {activity['location']}")
            print()
        
        return {"success": True, "recommendations": [r[0] for r in recommended[:3]]}
    
    # Private methods
    
    def _filter_activities_by_level(self, activity_level: str) -> List[Dict]:
        """Filter aktivitas berdasarkan level kesulitan"""
        
        level_mapping = {
            "ringan": ["mudah"],
            "sedang": ["mudah", "sedang"], 
            "aktif": ["mudah", "sedang", "sulit"]
        }
        
        allowed_difficulties = level_mapping.get(activity_level, ["mudah"])
        
        return [activity for activity in self.activities_db 
                if activity["difficulty"] in allowed_difficulties]
    
    def _get_recommended_activities(self, user_interests: List[str], activities: List[Dict]) -> List[Dict]:
        """Dapatkan aktivitas yang sesuai dengan minat user"""
        
        interest_mapping = {
            "berkebun": ["hobi"],
            "memasak": ["hobi"],
            "yoga": ["olahraga", "kesehatan"],
            "seni": ["kreatif"],
            "jalan kaki": ["olahraga"],
            "olahraga": ["olahraga"]
        }
        
        recommended_categories = set()
        for interest in user_interests:
            categories = interest_mapping.get(interest, [])
            recommended_categories.update(categories)
        
        return [activity for activity in activities 
                if activity["category"] in recommended_categories]
    
    def _get_booking_status(self, username: str, activity_id: int) -> str:
        """Cek status booking user untuk aktivitas tertentu"""
        
        user_bookings = self.user_bookings.get(username, [])
        for booking in user_bookings:
            if booking.get("activity_id") == activity_id:
                return "booked"
        return "not_booked"
    
    def _get_activity_choice(self, max_choice: int) -> Optional[Dict]:
        """Input pilihan aktivitas dari user"""
        
        while True:
            choice = input(f"{self.ui.SELECT} Pilih aktivitas untuk detail (1-{max_choice}) atau 'q' untuk keluar: ").strip()
            
            if choice.lower() == 'q':
                return None
            
            try:
                choice_num = int(choice)
                if 1 <= choice_num <= max_choice:
                    return self.activities_db[choice_num - 1]
                else:
                    print(f"{self.ui.WARNING} Pilihan tidak valid. Coba lagi.")
            except ValueError:
                print(f"{self.ui.WARNING} Masukkan angka atau 'q' untuk keluar")
    
    def _show_activity_details_and_book(self, username: str, activity: Dict) -> Dict:
        """Tampilkan detail aktivitas dan opsi booking"""
        
        emoji = activity.get("emoji", self.ui.ACTIVITY)
        print(f"\n{self.ui.SUMMARY} Detail Lengkap Aktivitas:")
        print(f"\n{emoji} {activity['name']}")
        print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        # Informasi dasar
        print(f"📝 Deskripsi: {activity['description']}")
        print(f"🕒 Waktu: {activity['time']} WIB")
        print(f"📍 Lokasi: {activity['location']}")
        print(f"👨‍🏫 Instruktur: {activity.get('instructor', 'TBA')}")
        print(f"💰 Biaya: {activity.get('price', 'Gratis')}")
        print(f"🎯 Level: {activity['difficulty']}")
        print(f"🏷️ Kategori: {activity['category']}")
        
        # Informasi kapasitas
        current_participants = activity.get('participants', 0)
        max_participants = activity.get('max_participants', 20)
        available_spots = max_participants - current_participants
        
        print(f"👥 Peserta: {current_participants}/{max_participants} orang")
        
        if available_spots <= 0:
            print(f"🚫 Status: PENUH - Tidak ada tempat tersisa")
        elif available_spots <= 3:
            print(f"⚠️  Status: Hampir penuh - {available_spots} tempat tersisa")
        else:
            print(f"✅ Status: Tersedia - {available_spots} tempat tersisa")
        
        # Informasi tambahan
        equipment = activity.get('equipment', 'Tidak ada informasi khusus')
        print(f"🎒 Perlengkapan: {equipment}")
        
        # Tampilkan manfaat aktivitas
        benefits = self._get_activity_benefits(activity["category"])
        if benefits:
            print(f"\n{self.ui.HEART} Manfaat mengikuti aktivitas ini:")
            for benefit in benefits[:3]:  # Tampilkan 3 manfaat teratas
                print(f"  • {benefit}")
        
        # Cek apakah sudah dibooking
        if self._get_booking_status(username, activity["id"]) == "booked":
            print(f"\n{self.ui.SUCCESS} Anda sudah booking aktivitas ini!")
            return {"success": True, "message": "Sudah dibooking", "already_booked": True}
        
        # Cek jika aktivitas penuh
        if available_spots <= 0:
            print(f"\n{self.ui.ERROR} Maaf, aktivitas ini sudah penuh!")
            alternative_choice = input("Ingin melihat aktivitas lain? (y/n): ").strip().lower()
            return {"success": False, "message": "Aktivitas penuh", "try_again": alternative_choice == 'y'}
        
        print(f"\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        # Konfirmasi booking
        while True:
            print(f"\nApakah Anda ingin booking '{activity['name']}'?")
            print(f"[1] {self.ui.CONFIRM} Ya, saya ingin booking")
            print(f"[2] {self.ui.CANCEL} Tidak, lihat aktivitas lain")
            print(f"[3] {self.ui.INFO} Tanyakan sesuatu dulu")
            
            choice = input(f"\n{self.ui.SELECT} Pilihan Anda (1-3): ").strip()
            
            if choice == "1":
                return self._book_activity(username, activity)
            elif choice == "2":
                print(f"{self.ui.INFO} Tidak apa-apa! Anda bisa booking aktivitas lain.")
                return {"success": False, "message": "User memilih tidak booking", "try_again": True}
            elif choice == "3":
                self._show_activity_faq(activity)
                continue  # Kembali ke pilihan booking
            else:
                print(f"{self.ui.WARNING} Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
    
    def _show_activity_faq(self, activity: Dict):
        """Tampilkan FAQ tentang aktivitas"""
        
        print(f"\n{self.ui.INFO} FAQ - {activity['name']}")
        print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        faq_items = [
            {
                "q": "Apakah aktivitas ini cocok untuk pemula?",
                "a": f"Ya! Aktivitas ini berLevel {activity['difficulty']} dan instruktur akan membantu peserta pemula."
            },
            {
                "q": "Apa yang harus saya bawa?",
                "a": f"{activity.get('equipment', 'Tidak ada persyaratan khusus')}. Sebaiknya bawa air minum dan datang 15 menit lebih awal."
            },
            {
                "q": "Bagaimana jika saya ingin membatalkan?",
                "a": "Anda bisa membatalkan booking hingga 2 jam sebelum aktivitas dimulai tanpa dikenakan biaya."
            },
            {
                "q": "Apakah ada batasan usia?",
                "a": "Aktivitas ini dirancang khusus untuk senior (50+ tahun) dengan mempertimbangkan keselamatan dan kenyamanan."
            }
        ]
        
        for i, faq in enumerate(faq_items, 1):
            print(f"\n{i}. {faq['q']}")
            print(f"   💡 {faq['a']}")
        
        input(f"\n{self.ui.INFO} Tekan Enter untuk kembali ke pilihan booking...")
    
    def _book_activity(self, username: str, activity: Dict) -> Dict:
        """Proses booking aktivitas"""
        
        # Generate booking ID
        booking_id = f"BK_{username}_{activity['id']}_{int(time.time())}"
        
        # Buat booking record
        booking = {
            "booking_id": booking_id,
            "activity_id": activity["id"],
            "activity_name": activity["name"],
            "activity_time": activity["time"],
            "activity_location": activity["location"],
            "category": activity["category"],
            "status": "confirmed",
            "booking_date": time.strftime("%Y-%m-%d"),
            "booking_time": time.strftime("%H:%M:%S")
        }
        
        # Simpan booking
        if username not in self.user_bookings:
            self.user_bookings[username] = []
        
        self.user_bookings[username].append(booking)
        
        # Update jumlah peserta (simulasi)
        activity["participants"] += 1
        
        print(f"\n{self.ui.CELEBRATION} Berhasil! Anda telah booking '{activity['name']}'!")
        print(f"{self.ui.CALENDAR} Jadwal: {activity['name']} pada {activity['time']} di {activity['location']}")
        print(f"{self.ui.BOOKING} ID Booking: {booking_id}")
        print(f"{self.ui.INFO} Jangan lupa datang 10 menit sebelum aktivitas dimulai!")
        
        return {
            "success": True,
            "message": f"Berhasil booking {activity['name']}",
            "activity": activity,
            "booking": booking
        }
    
    def _get_activity_benefits(self, category: str) -> List[str]:
        """Dapatkan manfaat berdasarkan kategori aktivitas"""
        
        benefits_map = {
            "olahraga": [
                "Meningkatkan kebugaran dan stamina",
                "Menjaga kesehatan jantung",
                "Memperkuat otot dan tulang",
                "Meningkatkan keseimbangan"
            ],
            "hobi": [
                "Mengembangkan kreativitas",
                "Mengurangi stress dan relaksasi",
                "Bersosialisasi dengan teman sebaya",
                "Mempelajari keterampilan baru"
            ],
            "kreatif": [
                "Melatih konsentrasi dan fokus",
                "Mengekspresikan diri secara artistik",
                "Meningkatkan kepercayaan diri",
                "Menstimulasi fungsi otak"
            ],
            "kesehatan": [
                "Meningkatkan kualitas hidup",
                "Menjaga kesehatan mental",
                "Membantu mengelola stress",
                "Meningkatkan fleksibilitas"
            ]
        }
        
        return benefits_map.get(category, ["Aktivitas yang menyenangkan dan bermanfaat"])
    
    def _filter_by_time_preference(self, preferred_time: str) -> List[Dict]:
        """Filter aktivitas berdasarkan preferensi waktu"""
        
        time_ranges = {
            "pagi": ["07:00", "08:00", "09:00", "10:00"],
            "siang": ["10:00", "11:00", "12:00", "13:00", "14:00"],
            "sore": ["14:00", "15:00", "16:00", "17:00", "18:00"]
        }
        
        preferred_times = time_ranges.get(preferred_time, [])
        
        return [activity for activity in self.activities_db 
                if any(time in activity["time"] for time in preferred_times)]
    
    def _calculate_recommendation_score(self, activity: Dict, interests: List[str], 
                                      activity_level: str, preferences: Dict) -> float:
        """Hitung score rekomendasi untuk aktivitas"""
        
        score = 0.0
        
        # Score berdasarkan minat (40%)
        interest_categories = {
            "berkebun": ["hobi"], "memasak": ["hobi"], "yoga": ["olahraga"],
            "seni": ["kreatif"], "olahraga": ["olahraga"]
        }
        
        for interest in interests:
            if activity["category"] in interest_categories.get(interest, []):
                score += 0.4
                break
        
        # Score berdasarkan level aktivitas (30%)
        level_match = {
            "ringan": {"mudah": 0.3, "sedang": 0.15},
            "sedang": {"mudah": 0.2, "sedang": 0.3},
            "aktif": {"mudah": 0.1, "sedang": 0.2, "sulit": 0.3}
        }
        
        score += level_match.get(activity_level, {}).get(activity["difficulty"], 0)
        
        # Score berdasarkan preferensi waktu (20%)
        preferred_time = preferences.get("preferred_time", "pagi")
        time_match = {
            "pagi": ["07:00", "08:00", "09:00", "10:00"],
            "siang": ["10:00", "11:00", "12:00", "13:00", "14:00"],
            "sore": ["14:00", "15:00", "16:00", "17:00", "18:00"]
        }
        
        if any(time in activity["time"] for time in time_match.get(preferred_time, [])):
            score += 0.2
        
        # Score berdasarkan preferensi grup (10%)
        prefers_group = preferences.get("prefers_group_activities", True)
        if prefers_group and activity["participants"] >= 8:
            score += 0.1
        elif not prefers_group and activity["participants"] < 8:
            score += 0.1
        
        return min(score, 1.0)  # Cap at 1.0
    
    def _get_activity_emoji(self, category: str) -> str:
        """Dapatkan emoji berdasarkan kategori aktivitas"""
        
        emoji_map = {
            "olahraga": self.ui.FITNESS,
            "hobi": self.ui.HOBBY,
            "kreatif": "🎨",
            "kesehatan": "💚",
            "edukasi": self.ui.EDUCATION
        }
        
        return emoji_map.get(category, self.ui.ACTIVITY)
    
    def _cancel_booking(self, username: str) -> Dict:
        """Batalkan booking aktivitas"""
        
        user_bookings = self.user_bookings.get(username, [])
        if not user_bookings:
            return {"success": False, "message": "Tidak ada booking"}
        
        print(f"\n{self.ui.CANCEL} Pilih booking yang ingin dibatalkan:")
        for i, booking in enumerate(user_bookings, 1):
            print(f"[{i}] {booking['activity_name']} - {booking['activity_time']}")
        
        choice = input("Pilih nomor booking: ").strip()
        try:
            choice_num = int(choice) - 1
            if 0 <= choice_num < len(user_bookings):
                cancelled_booking = user_bookings.pop(choice_num)
                print(f"{self.ui.SUCCESS} Booking '{cancelled_booking['activity_name']}' berhasil dibatalkan")
                return {"success": True, "cancelled": cancelled_booking}
        except ValueError:
            pass
        
        return {"success": False, "message": "Pilihan tidak valid"}
    
    def _reschedule_booking(self, username: str) -> Dict:
        """Reschedule booking aktivitas"""
        
        print(f"{self.ui.INFO} Fitur reschedule akan segera tersedia!")
        return {"success": False, "message": "Fitur dalam pengembangan"}
    
    def _view_booking_details(self, username: str) -> Dict:
        """Lihat detail booking"""
        
        return self.show_user_schedule(username)