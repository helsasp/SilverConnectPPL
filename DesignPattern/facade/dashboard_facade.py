# dashboard_facade.py
# Modul facade untuk dashboard dan summary personal

import time
import random
from typing import Dict, List, Optional
from config import UIElements, Messages, AppConfig

class DashboardFacade:
    """Facade untuk dashboard personal dan statistik"""
    
    def __init__(self):
        self.ui = UIElements()
        self.messages = Messages()
        print(f"[DashboardFacade] {self.ui.SUCCESS} Sistem dashboard siap")
    
    def show_personalized_summary(self, username: str, user_data: Dict,
                                 communities: List[Dict] = None,
                                 activities: List[Dict] = None) -> Dict:
        """Tampilkan ringkasan dashboard yang dipersonalisasi"""
        
        print(f"\n{self.ui.SECTION_SEPARATOR}")
        print(f"{self.ui.DASHBOARD} DASHBOARD PERSONAL - {username.upper()} {self.ui.DASHBOARD}")
        print(f"{self.ui.SECTION_SEPARATOR}")
        
        # Header dengan sambutan personal
        full_name = user_data.get("full_name", username)
        current_time = time.strftime("%H:%M")
        greeting = self._get_time_based_greeting(current_time)
        
        print(f"\n{self.ui.WELCOME} {greeting}, {full_name}!")
        print(f"Selamat datang di dashboard SilverConnect Anda")
        print(f"{self.ui.TIME} {time.strftime('%A, %d %B %Y - %H:%M')}")
        print()
        
        # Quick stats overview
        self._show_quick_stats(user_data, communities, activities)
        
        # Profile section dengan detail yang lebih kaya
        self._show_enhanced_profile_summary(user_data)
        
        # Communities section dengan aktivitas real
        self._show_enhanced_communities_summary(communities, username)
        
        # Activities section dengan detail booking
        self._show_enhanced_activities_summary(activities)
        
        # Personalized recommendations berdasarkan aktivitas user
        self._show_personalized_recommendations(user_data, communities, activities)
        
        # Notifications yang lebih smart
        self._show_smart_notifications(username, user_data, communities, activities)
        
        # Quick actions yang relevan
        self._show_contextual_quick_actions(user_data, communities, activities)
        
        # Health tips berdasarkan aktivitas user
        self._show_personalized_daily_tips(user_data, activities)
        
        return {
            "success": True,
            "message": "Dashboard berhasil ditampilkan",
            "summary": {
                "user": full_name,
                "communities_count": len(communities) if communities else 0,
                "activities_count": len(activities) if activities else 0,
                "profile_completion": self._calculate_profile_completion(user_data),
                "engagement_score": self._calculate_engagement_score(user_data, communities, activities)
            }
        }
    
    def _show_enhanced_profile_summary(self, user_data: Dict):
        """Tampilkan ringkasan profil yang lebih kaya"""
        
        print(f"{self.ui.PROFILE} Profil Anda:")
        print(f"  {self.ui.NAME} Nama: {user_data.get('full_name', 'Belum diisi')}")
        print(f"  {self.ui.AGE} Usia: {user_data.get('age', 'Belum diisi')} tahun")
        
        # Display interests dengan emoji dan grouping
        interests = user_data.get('interests', [])
        if interests:
            print(f"  {self.ui.INTERESTS} Minat & Hobi Anda:")
            
            # Group interests by category
            interest_categories = {
                'Aktivitas Fisik': ['jalan kaki', 'yoga', 'olahraga ringan'],
                'Kreatif & Seni': ['seni', 'musik', 'fotografi', 'menulis', 'crafting'],
                'Rumah & Hobi': ['berkebun', 'memasak', 'berkebun vertikal', 'memasak kue'],
                'Sosial & Intelektual': ['membaca', 'teknologi', 'bahasa asing', 'bermain kartu', 'catur'],
                'Keluarga & Rekreasi': ['berkumpul dengan keluarga', 'menonton film', 'travelling']
            }
            
            categorized_interests = {}
            uncategorized = []
            
            for interest in interests:
                found_category = False
                for category, category_interests in interest_categories.items():
                    if interest.lower() in category_interests:
                        if category not in categorized_interests:
                            categorized_interests[category] = []
                        categorized_interests[category].append(interest)
                        found_category = True
                        break
                if not found_category:
                    uncategorized.append(interest)
            
            # Display categorized interests
            for category, cat_interests in categorized_interests.items():
                interest_list = ', '.join([f"{self._get_interest_emoji(i)} {i.title()}" for i in cat_interests])
                print(f"    • {category}: {interest_list}")
            
            # Display uncategorized interests
            if uncategorized:
                uncategorized_list = ', '.join([f"{self._get_interest_emoji(i)} {i.title()}" for i in uncategorized])
                print(f"    • Lainnya: {uncategorized_list}")
        
        # Activity level and preferences
        if user_data.get('activity_level'):
            level_emoji = {"ringan": "🟡", "sedang": "🟢", "aktif": "🔴"}.get(user_data['activity_level'], "🟢")
            print(f"  {self.ui.FITNESS} Level Aktivitas: {level_emoji} {user_data['activity_level'].title()}")
        
        # Preferences
        preferences = user_data.get('preferences', {})
        if preferences:
            preferred_time = preferences.get('preferred_time', '')
            time_emoji = {"pagi": "🌅", "siang": "☀️", "sore": "🌇"}.get(preferred_time, "")
            if preferred_time:
                print(f"  ⏰ Waktu Favorit: {time_emoji} {preferred_time.title()}")
            
            if preferences.get('prefers_group_activities') is not None:
                group_pref = "👥 Suka aktivitas berkelompok" if preferences['prefers_group_activities'] else "👤 Lebih suka aktivitas individual"
                print(f"  {group_pref}")
        
        print()
    
    def _show_enhanced_communities_summary(self, communities: List[Dict], username: str):
        """Tampilkan ringkasan komunitas yang lebih detail"""
        
        print(f"{self.ui.COMMUNITY} Komunitas Anda:")
        if communities:
            for community in communities:
                community_name = community.get('community_name', 'Komunitas')
                joined_date = community.get('joined_date', 'Baru-baru ini')
                
                # Simulasi aktivitas dalam komunitas
                activity_count = random.randint(2, 8)
                interaction_level = random.choice(['🔥 Sangat Aktif', '✨ Aktif', '💙 Moderate'])
                
                print(f"  {self.ui.JOIN} {community_name}")
                print(f"    📅 Bergabung: {joined_date}")
                print(f"    📊 Status: {interaction_level}")
                print(f"    💬 {activity_count} interaksi bulan ini")
        else:
            print(f"  {self.ui.INFO} Belum bergabung dengan komunitas")
            print(f"  {self.ui.SPARKLE} Tip: Bergabung komunitas untuk memperluas pertemanan!")
        print()
    
    def _show_enhanced_activities_summary(self, activities: List[Dict]):
        """Tampilkan ringkasan aktivitas yang lebih detail"""
        
        print(f"{self.ui.ACTIVITY} Aktivitas & Jadwal Anda:")
        if activities:
            # Sort activities by time
            sorted_activities = sorted(activities, key=lambda x: x.get('activity_time', '00:00'))
            
            for activity in sorted_activities[:5]:  # Show max 5 upcoming
                activity_name = activity.get('activity_name', 'Aktivitas')
                activity_time = activity.get('activity_time', 'TBD')
                activity_location = activity.get('activity_location', 'TBD')
                status = activity.get('status', 'confirmed')
                
                status_emoji = {
                    'confirmed': self.ui.SUCCESS,
                    'pending': self.ui.PENDING,
                    'cancelled': self.ui.ERROR
                }.get(status, self.ui.SUCCESS)
                
                print(f"  {self.ui.CALENDAR} {activity_name}")
                print(f"    🕒 {activity_time} | 📍 {activity_location}")
                print(f"    {status_emoji} Status: {status.title()}")
            
            if len(activities) > 5:
                print(f"  {self.ui.INFO} dan {len(activities) - 5} aktivitas lainnya...")
                
            # Weekly summary
            weekly_activities = len([a for a in activities if a.get('booking_date', '') >= time.strftime('%Y-%m-%d', time.gmtime(time.time() - 7*24*3600))])
            print(f"  📈 {weekly_activities} aktivitas minggu ini")
        else:
            print(f"  {self.ui.INFO} Belum ada aktivitas terjadwal")
            print(f"  {self.ui.SPARKLE} Tip: Book aktivitas untuk menjaga rutinitas sehat!")
        print()
    
    def _show_personalized_recommendations(self, user_data: Dict, communities: List[Dict], activities: List[Dict]):
        """Tampilkan rekomendasi yang dipersonalisasi"""
        
        interests = user_data.get('interests', [])
        activity_level = user_data.get('activity_level', 'sedang')
        
        print(f"{self.ui.SPARKLE} Rekomendasi Personal:")
        
        # Community recommendations based on interests
        if len(communities or []) < 3:
            if 'teknologi' in interests:
                print(f"  🆕 Tech Savvy Seniors - Belajar smartphone dan internet")
            if 'seni' in interests or 'crafting' in interests:
                print(f"  🎨 Kreasi Seni Senior - Workshop kerajinan dan melukis")
            if 'membaca' in interests:
                print(f"  📖 Klub Buku Sastra - Diskusi novel dan biografi")
        
        # Activity recommendations
        if len(activities or []) < 3:
            if 'memasak' in interests:
                print(f"  👨‍🍳 Workshop Masak Rendang - Chef Indra, Rp 75.000")
            if 'yoga' in interests or activity_level == 'ringan':
                print(f"  🧘‍♀️ Yoga Sunrise - Gratis, setiap pagi di Taman Menteng")
            if 'berkebun' in interests:
                print(f"  🌱 Urban Gardening - Belajar hidroponik, Rp 100.000")
        
        # Wellness recommendations
        age = user_data.get('age', 65)
        if age >= 70:
            print(f"  💚 Senam Kursi Ceria - Olahraga aman sambil duduk")
        
        print()
    
    def _show_smart_notifications(self, username: str, user_data: Dict, communities: List[Dict], activities: List[Dict]):
        """Tampilkan notifikasi yang lebih cerdas"""
        
        print(f"{self.ui.NOTIFICATIONS} Notifikasi & Update:")
        
        notifications = []
        
        # Profile completion notifications
        if not user_data.get('profile_completed'):
            notifications.append("💡 Lengkapi profil untuk rekomendasi yang lebih akurat")
        
        # Activity-based notifications
        if activities:
            next_activity = min(activities, key=lambda x: x.get('activity_time', '23:59'))
            notifications.append(f"⏰ Jangan lupa: {next_activity.get('activity_name')} hari ini jam {next_activity.get('activity_time')}")
        
        # Community notifications
        if communities:
            notifications.append(f"💬 {random.randint(2,5)} diskusi baru di komunitas Anda")
        
        # Engagement notifications
        engagement_score = self._calculate_engagement_score(user_data, communities, activities)
        if engagement_score >= 0.8:
            notifications.append("🎉 Luar biasa! Anda sangat aktif minggu ini")
        elif engagement_score < 0.5:
            notifications.append("🌟 Ada aktivitas menarik menunggu Anda!")
        
        # Health reminders
        notifications.extend([
            "💧 Reminder: Minum air dan istirahat secukupnya",
            "🌞 Cuaca cerah hari ini, cocok untuk aktivitas outdoor"
        ])
        
        # Show 4 most relevant notifications
        for notification in notifications[:4]:
            print(f"  {self.ui.NOTIFICATIONS} {notification}")
        
        print()
    
    def _show_contextual_quick_actions(self, user_data: Dict, communities: List[Dict], activities: List[Dict]):
        """Tampilkan aksi cepat yang kontekstual"""
        
        print(f"{self.ui.SPARKLE} Aksi Cepat Hari Ini:")
        
        actions = []
        
        # Based on current status
        if not communities:
            actions.append("🤝 Bergabung dengan komunitas pertama")
        elif len(communities) < 2:
            actions.append("🔍 Jelajahi komunitas baru")
        
        if not activities:
            actions.append("🎯 Book aktivitas pertama")
        elif len(activities) < 3:
            actions.append("📅 Tambah aktivitas ke jadwal")
        
        # Based on interests
        interests = user_data.get('interests', [])
        if 'teknologi' in interests:
            actions.append("📱 Ikut kelas digital literacy")
        if 'memasak' in interests:
            actions.append("👨‍🍳 Coba workshop masak baru")
        
        # General actions
        actions.extend([
            "💬 Lihat update komunitas",
            "📊 Cek progress mingguan",
            "🏥 Tips kesehatan hari ini"
        ])
        
        # Show 4 most relevant actions
        for i, action in enumerate(actions[:4], 1):
            print(f"  [{i}] {action}")
        
        print()
    
    def _show_personalized_daily_tips(self, user_data: Dict, activities: List[Dict]):
        """Tampilkan tips harian yang dipersonalisasi"""
        
        age = user_data.get('age', 65)
        activity_level = user_data.get('activity_level', 'sedang')
        interests = user_data.get('interests', [])
        
        print(f"{self.ui.HEART} Tips Personal Hari Ini:")
        
        # Age-based tips
        if age >= 75:
            tips_pool = [
                "Lakukan peregangan ringan setiap 2 jam untuk menjaga fleksibilitas",
                "Pastikan asupan kalsium cukup untuk kesehatan tulang",
                "Tidur 7-8 jam berkualitas sangat penting di usia Anda"
            ]
        elif age >= 65:
            tips_pool = [
                "Jalan kaki 30 menit sehari dapat mengurangi risiko penyakit jantung",
                "Latih memory dengan puzzle atau permainan strategi",
                "Konsumsi makanan tinggi omega-3 untuk kesehatan otak"
            ]
        else:
            tips_pool = [
                "Mulai investasi kesehatan sejak dini dengan olahraga teratur",
                "Bangun rutinitas mindfulness untuk mengurangi stress",
                "Perbanyak aktivitas sosial untuk kesehatan mental optimal"
            ]
        
        # Activity level tips
        if activity_level == 'ringan':
            tips_pool.append("Mulai dengan aktivitas ringan dan tingkatkan secara bertahap")
        elif activity_level == 'aktif':
            tips_pool.append("Jaga keseimbangan antara aktivitas dan istirahat")
        
        # Interest-based tips
        if 'berkebun' in interests:
            tips_pool.append("Berkebun 15 menit sehari dapat meningkatkan mood dan mengurangi stress")
        if 'yoga' in interests:
            tips_pool.append("Kombinasikan yoga dengan meditasi untuk manfaat maksimal")
        if 'memasak' in interests:
            tips_pool.append("Masak dengan rempah segar untuk manfaat antioksidan yang lebih tinggi")
        
        # Activity-based tips
        if activities:
            has_morning_activity = any('06:' in a.get('activity_time', '') or '07:' in a.get('activity_time', '') for a in activities)
            if has_morning_activity:
                tips_pool.append("Sarapan ringan 30 menit sebelum aktivitas pagi untuk energi optimal")
        
        # Select and display tip
        selected_tip = random.choice(tips_pool)
        print(f"  {self.ui.SPARKLE} {selected_tip}")
        
        # Add a health fact
        health_facts = [
            "Tertawa 15 menit sehari dapat meningkatkan sistem imun",
            "Berjemur 10-15 menit pagi hari membantu produksi vitamin D",
            "Minum air hangat dengan lemon di pagi hari baik untuk pencernaan",
            "Mendengarkan musik dapat menurunkan tekanan darah"
        ]
        
        health_fact = random.choice(health_facts)
        print(f"  💡 Tahukah Anda? {health_fact}")
        
        print()
    
    def _calculate_engagement_score(self, user_data: Dict, communities: List[Dict], activities: List[Dict]) -> float:
        """Hitung skor engagement yang lebih akurat"""
        
        score = 0.0
        
        # Profile completion (30%)
        profile_fields = ['full_name', 'age', 'interests', 'activity_level', 'preferences']
        completed_fields = sum(1 for field in profile_fields if user_data.get(field))
        profile_score = completed_fields / len(profile_fields)
        score += profile_score * 0.3
        
        # Community engagement (40%)
        community_count = len(communities) if communities else 0
        optimal_communities = 2  # Optimal number of communities
        community_score = min(community_count / optimal_communities, 1.0)
        score += community_score * 0.4
        
        # Activity participation (30%)
        activity_count = len(activities) if activities else 0
        optimal_activities = 3  # Optimal number of weekly activities
        activity_score = min(activity_count / optimal_activities, 1.0)
        score += activity_score * 0.3
        
        return min(score, 1.0)
    
    def _get_interest_emoji(self, interest: str) -> str:
        """Dapatkan emoji untuk minat tertentu dengan mapping yang lebih lengkap"""
        
        emoji_map = {
            "berkebun": "🌱", "memasak": "👨‍🍳", "membaca": "📚",
            "jalan kaki": "🚶‍♂️", "yoga": "🧘‍♀️", "seni": "🎨",
            "musik": "🎵", "fotografi": "📸", "menulis": "✍️",
            "bermain kartu": "🃏", "catur": "♟️", "berkumpul dengan keluarga": "👨‍👩‍👧‍👦",
            "menonton film": "🎬", "crafting": "🎭", "teknologi": "📱",
            "travelling": "✈️", "olahraga ringan": "🏃‍♂️", "berkebun vertikal": "🪴",
            "memasak kue": "🧁", "bahasa asing": "🗣️"
        }
        
        return emoji_map.get(interest.lower(), self.ui.HEART)
    
    def show_weekly_report(self, username: str, user_data: Dict,
                          weekly_data: Dict = None) -> Dict:
        """Tampilkan laporan aktivitas mingguan"""
        
        print(f"\n{self.ui.STATS} LAPORAN MINGGUAN")
        print(f"{self.ui.SUBSECTION_SEPARATOR}")
        
        # Simulasi data mingguan jika tidak ada
        if not weekly_data:
            weekly_data = self._generate_sample_weekly_data()
        
        print(f"{self.ui.CALENDAR} Periode: {weekly_data.get('period', 'Minggu ini')}")
        print()
        
        # Statistik aktivitas
        print(f"{self.ui.ACTIVITY} Aktivitas Mingguan:")
        activities_completed = weekly_data.get('activities_completed', 0)
        activities_planned = weekly_data.get('activities_planned', 0)
        completion_rate = (activities_completed / activities_planned * 100) if activities_planned > 0 else 0
        
        print(f"  • Aktivitas diselesaikan: {activities_completed} dari {activities_planned}")
        print(f"  • Tingkat penyelesaian: {completion_rate:.1f}%")
        print()
        
        # Interaksi sosial
        print(f"{self.ui.COMMUNITY} Interaksi Sosial:")
        print(f"  • Diskusi komunitas: {weekly_data.get('community_posts', 0)} postingan")
        print(f"  • Komentar diberikan: {weekly_data.get('comments_made', 0)}")
        print(f"  • Teman baru: {weekly_data.get('new_connections', 0)} orang")
        print()
        
        # Achievement badges
        achievements = weekly_data.get('achievements', [])
        if achievements:
            print(f"{self.ui.STAR} Pencapaian Minggu Ini:")
            for achievement in achievements:
                print(f"  {self.ui.CELEBRATION} {achievement}")
            print()
        
        return {"success": True, "weekly_data": weekly_data}
    
    def show_health_dashboard(self, username: str, user_data: Dict) -> Dict:
        """Dashboard khusus kesehatan dan wellness"""
        
        print(f"\n{self.ui.FITNESS} DASHBOARD KESEHATAN & WELLNESS")
        print(f"{self.ui.SUBSECTION_SEPARATOR}")
        
        age = user_data.get('age', 65)
        activity_level = user_data.get('activity_level', 'sedang')
        
        # Health metrics (simulasi)
        health_data = self._generate_health_metrics(age, activity_level)
        
        print(f"{self.ui.HEART} Status Kesehatan Umum:")
        print(f"  • Usia: {age} tahun")
        print(f"  • Level aktivitas: {activity_level}")
        print(f"  • Skor wellness: {health_data['wellness_score']}/100")
        print()
        
        # Rekomendasi kesehatan
        recommendations = self._get_health_recommendations(age, activity_level)
        print(f"{self.ui.SPARKLE} Rekomendasi Kesehatan:")
        for rec in recommendations:
            print(f"  • {rec}")
        print()
        
        # Weekly goals
        print(f"{self.ui.STAR} Target Minggu Ini:")
        goals = [
            f"Aktivitas fisik: {health_data['activity_goal']} menit/hari",
            f"Interaksi sosial: {health_data['social_goal']} aktivitas",
            f"Istirahat: {health_data['rest_goal']} jam/malam",
            f"Hidrasi: {health_data['water_goal']} gelas/hari"
        ]
        
        for goal in goals:
            completion = random.randint(60, 95)
            status = self.ui.SUCCESS if completion >= 80 else self.ui.PENDING
            print(f"  {status} {goal} ({completion}% tercapai)")
        
        return {"success": True, "health_data": health_data}
    
    def show_social_connections(self, username: str, communities: List[Dict] = None) -> Dict:
        """Dashboard koneksi sosial dan komunitas"""
        
        print(f"\n{self.ui.COMMUNITY} KONEKSI SOSIAL & KOMUNITAS")
        print(f"{self.ui.SUBSECTION_SEPARATOR}")
        
        if not communities:
            print(f"{self.ui.INFO} Anda belum bergabung dengan komunitas apapun")
            print(f"{self.ui.SPARKLE} Mari mulai dengan bergabung di komunitas yang sesuai minat Anda!")
            return {"success": False, "message": "Belum ada komunitas"}
        
        print(f"{self.ui.MEMBERS} Ringkasan Koneksi:")
        total_connections = sum(random.randint(8, 25) for _ in communities)
        print(f"  • Total koneksi: {total_connections} teman")
        print(f"  • Komunitas aktif: {len(communities)}")
        print()
        
        # Community engagement
        print(f"{self.ui.DISCUSSION} Keterlibatan Komunitas:")
        for community in communities:
            engagement_score = random.randint(70, 95)
            activity_level = "Tinggi" if engagement_score >= 85 else "Sedang" if engagement_score >= 70 else "Rendah"
            
            print(f"  • {community.get('community_name', 'Komunitas')}: {engagement_score}% ({activity_level})")
        print()
        
        # Recent interactions
        print(f"{self.ui.SPARKLE} Interaksi Terbaru:")
        interactions = [
            "Bu Sari menyukai postingan Anda tentang resep sehat",
            "Pak Budi mengundang Anda ke sesi jalan pagi",
            "3 anggota baru bergabung di Klub Berkebun",
            "Diskusi tentang 'Tips hidup sehat' mendapat 12 tanggapan"
        ]
        
        for interaction in interactions[:3]:
            print(f"  {self.ui.HEART} {interaction}")
        
        return {"success": True, "social_data": {"connections": total_connections, "communities": len(communities)}}
    
    # Private methods
    
    def _show_quick_stats(self, user_data: Dict, communities: List[Dict], activities: List[Dict]):
        """Tampilkan statistik cepat di bagian atas"""
        
        print(f"{self.ui.STATS} Ringkasan Cepat:")
        print(f"  {self.ui.PROFILE} Profil: {self._get_completion_status(user_data.get('profile_completed', False))}")
        print(f"  {self.ui.COMMUNITY} Komunitas: {len(communities) if communities else 0} bergabung")
        print(f"  {self.ui.ACTIVITY} Aktivitas: {len(activities) if activities else 0} terjadwal")
        print(f"  {self.ui.HEART} Status: {self._get_activity_status(user_data)}")
        print()
    
    def _show_profile_summary(self, user_data: Dict):
        """Tampilkan ringkasan profil"""
        
        print(f"{self.ui.PROFILE} Profil Anda:")
        print(f"  {self.ui.NAME} Nama: {user_data.get('full_name', 'Belum diisi')}")
        print(f"  {self.ui.AGE} Usia: {user_data.get('age', 'Belum diisi')} tahun")
        
        if user_data.get('interests'):
            interests_str = ', '.join(user_data['interests'][:3])
            if len(user_data['interests']) > 3:
                interests_str += f" dan {len(user_data['interests']) - 3} lainnya"
            print(f"  {self.ui.INTERESTS} Minat: {interests_str}")
        
        if user_data.get('activity_level'):
            print(f"  {self.ui.FITNESS} Level Aktivitas: {user_data['activity_level']}")
        
        print()
    
    def _show_communities_summary(self, communities: List[Dict]):
        """Tampilkan ringkasan komunitas"""
        
        print(f"{self.ui.COMMUNITY} Komunitas Anda:")
        if communities:
            for community in communities:
                community_name = community.get('community_name', 'Komunitas')
                joined_date = community.get('joined_date', 'Baru-baru ini')
                print(f"  {self.ui.JOIN} {community_name} - Bergabung: {joined_date}")
        else:
            print(f"  {self.ui.INFO} Belum bergabung dengan komunitas")
            print(f"  {self.ui.SPARKLE} Tip: Bergabung dengan komunitas untuk bersosialisasi!")
        print()
    
    def _show_activities_summary(self, activities: List[Dict]):
        """Tampilkan ringkasan aktivitas"""
        
        print(f"{self.ui.ACTIVITY} Aktivitas Terjadwal:")
        if activities:
            for activity in activities[:3]:  # Tampilkan maksimal 3
                activity_name = activity.get('activity_name', 'Aktivitas')
                activity_time = activity.get('activity_time', 'Waktu TBD')
                print(f"  {self.ui.CALENDAR} {activity_name} - {activity_time}")
            
            if len(activities) > 3:
                print(f"  {self.ui.INFO} dan {len(activities) - 3} aktivitas lainnya...")
        else:
            print(f"  {self.ui.INFO} Belum ada aktivitas terjadwal")
            print(f"  {self.ui.SPARKLE} Tip: Booking aktivitas untuk menjaga kesehatan!")
        print()
    
    def _show_notifications(self, username: str, user_data: Dict):
        """Tampilkan notifikasi terbaru"""
        
        print(f"{self.ui.NOTIFICATIONS} Notifikasi Terbaru:")
        
        # Generate notifikasi dinamis
        notifications = []
        
        if not user_data.get('profile_completed'):
            notifications.append("Lengkapi profil Anda untuk rekomendasi yang lebih baik")
        
        notifications.extend([
            "Selamat! Anda telah aktif 3 hari berturut-turut",
            "Ada diskusi baru di komunitas Anda",
            "Jangan lupa minum air dan tetap terhidrasi",
            "Tips hari ini: Lakukan peregangan ringan setiap 2 jam"
        ])
        
        # Tampilkan 3 notifikasi teratas
        for notification in notifications[:3]:
            print(f"  {self.ui.NOTIFICATIONS} {notification}")
        print()
    
    def _show_quick_actions(self):
        """Tampilkan aksi cepat yang bisa dilakukan"""
        
        print(f"{self.ui.SPARKLE} Aksi Cepat:")
        actions = [
            "Cari aktivitas baru untuk hari ini",
            "Bergabung dengan komunitas baru",
            "Lihat diskusi terbaru di komunitas",
            "Update profil dan preferensi",
            "Undang teman untuk bergabung"
        ]
        
        for i, action in enumerate(actions[:3], 1):
            print(f"  [{i}] {action}")
        print()
    
    def _show_daily_tips(self, user_data: Dict):
        """Tampilkan tips harian yang relevan"""
        
        age = user_data.get('age', 65)
        activity_level = user_data.get('activity_level', 'sedang')
        
        tips_pool = [
            "Minum 8 gelas air setiap hari untuk menjaga hidrasi",
            "Lakukan peregangan ringan selama 10 menit setiap pagi",
            "Bersosialisasi dengan teman dapat meningkatkan mood",
            "Tidur 7-8 jam setiap malam penting untuk kesehatan",
            "Konsumsi makanan bervariasi dengan banyak sayur dan buah",
            "Jalan kaki 30 menit sehari baik untuk jantung",
            "Latih otak dengan puzzle atau permainan kata",
            "Berjemur di pagi hari untuk mendapat vitamin D"
        ]
        
        # Pilih tips berdasarkan profil
        daily_tip = random.choice(tips_pool)
        
        print(f"{self.ui.HEART} Tips Hari Ini:")
        print(f"  {self.ui.SPARKLE} {daily_tip}")
        print()
    
    def _get_time_based_greeting(self, current_time: str) -> str:
        """Dapatkan sapaan berdasarkan waktu"""
        
        hour = int(current_time.split(':')[0])
        
        if 5 <= hour < 12:
            return "Selamat pagi"
        elif 12 <= hour < 15:
            return "Selamat siang"
        elif 15 <= hour < 18:
            return "Selamat sore"
        else:
            return "Selamat malam"
    
    def _get_completion_status(self, is_completed: bool) -> str:
        """Status completion dengan emoji"""
        return f"{self.ui.SUCCESS} Lengkap" if is_completed else f"{self.ui.PENDING} Perlu dilengkapi"
    
    def _get_activity_status(self, user_data: Dict) -> str:
        """Status aktivitas user"""
        activity_level = user_data.get('activity_level', 'sedang')
        
        status_map = {
            'ringan': f"{self.ui.PENDING} Santai",
            'sedang': f"{self.ui.SUCCESS} Aktif",
            'aktif': f"{self.ui.CELEBRATION} Sangat aktif"
        }
        
        return status_map.get(activity_level, f"{self.ui.INFO} Normal")
    
    def _calculate_profile_completion(self, user_data: Dict) -> int:
        """Hitung persentase kelengkapan profil"""
        
        required_fields = ['full_name', 'age', 'interests', 'activity_level', 'profile_completed']
        completed_fields = sum(1 for field in required_fields if user_data.get(field))
        
        return int((completed_fields / len(required_fields)) * 100)
    
    def _generate_sample_weekly_data(self) -> Dict:
        """Generate data mingguan sampel"""
        
        return {
            'period': 'Minggu ini (1-7 Juni 2025)',
            'activities_completed': random.randint(4, 7),
            'activities_planned': 7,
            'community_posts': random.randint(2, 8),
            'comments_made': random.randint(5, 15),
            'new_connections': random.randint(1, 4),
            'achievements': [
                "Aktif 5 hari berturut-turut",
                "Membuat postingan pertama di komunitas",
                "Menyelesaikan semua aktivitas yoga minggu ini"
            ]
        }
    
    def _generate_health_metrics(self, age: int, activity_level: str) -> Dict:
        """Generate metrik kesehatan"""
        
        base_score = 75
        if activity_level == 'aktif':
            base_score += 15
        elif activity_level == 'ringan':
            base_score -= 10
        
        return {
            'wellness_score': min(base_score + random.randint(-5, 10), 100),
            'activity_goal': 30 if activity_level == 'aktif' else 20 if activity_level == 'sedang' else 15,
            'social_goal': 3,
            'rest_goal': 8,
            'water_goal': 8
        }
    
    def _get_health_recommendations(self, age: int, activity_level: str) -> List[str]:
        """Rekomendasi kesehatan berdasarkan profil"""
        
        recommendations = [
            "Lakukan pemeriksaan kesehatan rutin setiap 6 bulan",
            "Konsumsi makanan kaya kalsium untuk kesehatan tulang",
            "Jaga berat badan ideal sesuai usia"
        ]
        
        if activity_level == 'ringan':
            recommendations.extend([
                "Mulai dengan aktivitas ringan seperti jalan santai",
                "Lakukan peregangan setiap hari"
            ])
        elif activity_level == 'aktif':
            recommendations.extend([
                "Pertahankan rutinitas olahraga yang sudah baik",
                "Jangan lupa istirahat yang cukup setelah aktivitas"
            ])
        
        return recommendations[:4]  # Batasi 4 rekomendasi