# community_facade.py
# Modul facade untuk manajemen komunitas dan membership

import time
from typing import Dict, List, Optional
from config import UIElements, Messages, AppConfig

class CommunityFacade:
    """Facade untuk sistem komunitas dan membership"""
    
    def __init__(self):
        self.communities_db = AppConfig.DEFAULT_COMMUNITIES.copy()
        self.user_memberships = {}
        self.community_posts = {}
        self.ui = UIElements()
        self.messages = Messages()
        print(f"[CommunityFacade] {self.ui.SUCCESS} Sistem komunitas siap")
    
    def interactive_browse_and_join(self, username: str, user_interests: List[str] = None) -> Dict:
        """Jelajahi dan bergabung dengan komunitas secara interaktif"""
        
        print(f"\n{self.ui.SECTION_SEPARATOR}")
        print(f"{self.ui.COMMUNITY} JELAJAHI KOMUNITAS UNTUK {username.upper()} {self.ui.COMMUNITY}")
        print(f"{self.ui.SECTION_SEPARATOR}")
        
        # Rekomendasikan komunitas berdasarkan minat
        if user_interests:
            recommended = self._get_recommended_communities(user_interests)
            if recommended:
                print(f"{self.ui.SPARKLE} Rekomendasi berdasarkan minat Anda ({', '.join(user_interests)}):")
                for i, community in enumerate(recommended[:3], 1):
                    emoji = community.get("emoji", self.ui.COMMUNITY)
                    print(f"  {i}. {emoji} {community['name']} - {community['members']} anggota")
                print()
        
        # Tampilkan semua komunitas dengan detail lengkap
        print(f"{self.ui.BROWSE} Komunitas Yang Tersedia:")
        print()
        
        for i, community in enumerate(self.communities_db, 1):
            emoji = community.get("emoji", self.ui.COMMUNITY)
            status = self._get_membership_status(username, community["id"])
            status_icon = self.ui.SUCCESS if status == "joined" else ""
            
            print(f"[{i}] {emoji} {community['name']} {status_icon}")
            print(f"    📍 Lokasi: {community.get('location', 'TBA')}")
            print(f"    🗓️  Jadwal: {community.get('meeting_schedule', 'Fleksibel')}")
            print(f"    👥 {community['members']} anggota | 🏷️ {community['category']}")
            print(f"    💭 {community['description']}")
            if status == "joined":
                print(f"    {self.ui.SUCCESS} Anda sudah bergabung")
            print()
        
        # Input pilihan user dengan validasi
        while True:
            choice = input(f"{self.ui.SELECT} Pilih komunitas untuk melihat detail (1-{len(self.communities_db)}) atau 'q' untuk keluar: ").strip()
            
            if choice.lower() == 'q':
                return {"success": False, "message": "User membatalkan pemilihan komunitas"}
            
            try:
                choice_num = int(choice)
                if 1 <= choice_num <= len(self.communities_db):
                    selected_community = self.communities_db[choice_num - 1]
                    break
                else:
                    print(f"{self.ui.WARNING} Pilihan tidak valid. Masukkan angka 1-{len(self.communities_db)} atau 'q'")
            except ValueError:
                print(f"{self.ui.WARNING} Masukkan angka yang valid atau 'q' untuk keluar")
        
        # Tampilkan detail komunitas dan opsi bergabung
        return self._show_community_details_and_join(username, selected_community)
    
    def show_user_communities(self, username: str) -> Dict:
        """Tampilkan komunitas yang sudah diikuti user"""
        
        user_communities = self.user_memberships.get(username, [])
        
        if not user_communities:
            print(f"{self.ui.INFO} Anda belum bergabung dengan komunitas apapun")
            return {"success": False, "message": "Belum ada komunitas"}
        
        print(f"\n{self.ui.COMMUNITY} Komunitas Anda:")
        for membership in user_communities:
            community = self._get_community_by_id(membership["community_id"])
            if community:
                emoji = community.get("emoji", self.ui.COMMUNITY)
                print(f"  {emoji} {community['name']} - Bergabung: {membership['joined_date']}")
        
        return {"success": True, "communities": user_communities}
    
    def interactive_community_activities(self, username: str) -> Dict:
        """Aktivitas dalam komunitas - diskusi, posting, dll"""
        
        user_communities = self.user_memberships.get(username, [])
        if not user_communities:
            print(f"{self.ui.WARNING} Bergabunglah dengan komunitas terlebih dahulu")
            return {"success": False, "message": "Belum ada komunitas"}
        
        print(f"\n{self.ui.DISCUSSION} AKTIVITAS KOMUNITAS")
        print("Pilih aktivitas yang ingin dilakukan:")
        print(f"[1] {self.ui.BROWSE} Lihat diskusi terbaru")
        print(f"[2] {self.ui.SPARKLE} Buat postingan baru")
        print(f"[3] {self.ui.MEMBERS} Lihat anggota komunitas")
        print(f"[4] {self.ui.CANCEL} Kembali")
        
        choice = input(f"{self.ui.SELECT} Pilihan Anda: ").strip()
        
        if choice == "1":
            return self._view_community_discussions(username)
        elif choice == "2":
            return self._create_community_post(username)
        elif choice == "3":
            return self._view_community_members(username)
        else:
            return {"success": False, "message": "Kembali ke menu utama"}
    
    def leave_community(self, username: str, community_id: int) -> Dict:
        """Keluar dari komunitas"""
        
        if username not in self.user_memberships:
            return {"success": False, "message": "Tidak ada membership"}
        
        # Cari dan hapus membership
        memberships = self.user_memberships[username]
        for i, membership in enumerate(memberships):
            if membership["community_id"] == community_id:
                community_name = membership["community_name"]
                del memberships[i]
                print(f"{self.ui.SUCCESS} Anda telah keluar dari {community_name}")
                return {"success": True, "message": f"Keluar dari {community_name}"}
        
        return {"success": False, "message": "Membership tidak ditemukan"}
    
    # Private methods
    
    def _get_recommended_communities(self, user_interests: List[str]) -> List[Dict]:
        """Dapatkan rekomendasi komunitas berdasarkan minat"""
        
        interest_mapping = {
            "berkebun": ["Klub Berkebun"],
            "memasak": ["Pecinta Masakan"],
            "membaca": ["Kelompok Baca Buku"],
            "jalan kaki": ["Teman Jalan Kaki"],
            "yoga": ["Kelas Yoga Senior"],
            "olahraga": ["Teman Jalan Kaki", "Kelas Yoga Senior"]
        }
        
        recommended = []
        for interest in user_interests:
            community_names = interest_mapping.get(interest, [])
            for community in self.communities_db:
                if community["name"] in community_names:
                    recommended.append(community)
        
        return list({c["id"]: c for c in recommended}.values())  # Remove duplicates
    
    def _get_membership_status(self, username: str, community_id: int) -> str:
        """Cek status membership user di komunitas tertentu"""
        
        user_memberships = self.user_memberships.get(username, [])
        for membership in user_memberships:
            if membership["community_id"] == community_id:
                return "joined"
        return "not_joined"
    
    def _get_community_choice(self, max_choice: int) -> Optional[Dict]:
        """Input pilihan komunitas dari user"""
        
        while True:
            choice = input(f"{self.ui.SELECT} Pilih komunitas untuk detail (1-{max_choice}) atau 'q' untuk keluar: ").strip()
            
            if choice.lower() == 'q':
                return None
            
            try:
                choice_num = int(choice)
                if 1 <= choice_num <= max_choice:
                    return self.communities_db[choice_num - 1]
                else:
                    print(f"{self.ui.WARNING} Pilihan tidak valid. Coba lagi.")
            except ValueError:
                print(f"{self.ui.WARNING} Masukkan angka atau 'q' untuk keluar")
    
    def _show_community_details_and_join(self, username: str, community: Dict) -> Dict:
        """Tampilkan detail komunitas dan opsi bergabung"""
        
        emoji = community.get("emoji", self.ui.COMMUNITY)
        print(f"\n{self.ui.SUMMARY} Detail Lengkap Komunitas:")
        print(f"\n{emoji} {community['name']}")
        print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        # Informasi dasar
        print(f"📝 Deskripsi: {community['description']}")
        print(f"📍 Lokasi Pertemuan: {community.get('location', 'Lokasi akan diberitahu kemudian')}")
        print(f"🗓️  Jadwal Pertemuan: {community.get('meeting_schedule', 'Jadwal fleksibel')}")
        print(f"👥 Jumlah Anggota: {community['members']} orang")
        print(f"🏷️ Kategori: {community['category']}")
        
        # Informasi aktivitas komunitas
        activities = self._get_community_sample_activities(community["category"])
        if activities:
            print(f"\n{self.ui.SPARKLE} Aktivitas di komunitas ini:")
            for activity in activities:
                print(f"  • {activity}")
        
        # Simulasi anggota aktif
        sample_members = [
            {"name": "Pak Budi", "since": "2024-01", "posts": 23},
            {"name": "Bu Sari", "since": "2024-02", "posts": 45},
            {"name": "Pak Joko", "since": "2024-01", "posts": 12},
            {"name": "Bu Dewi", "since": "2024-03", "posts": 18}
        ]
        
        print(f"\n👥 Beberapa anggota aktif:")
        for member in sample_members[:3]:
            print(f"  • {member['name']} - Bergabung sejak {member['since']} ({member['posts']} kontribusi)")
        
        # Cek apakah sudah bergabung
        if self._get_membership_status(username, community["id"]) == "joined":
            print(f"\n{self.ui.SUCCESS} Anda sudah menjadi anggota komunitas ini!")
            
            # Opsi untuk anggota yang sudah join
            print(f"\nSebagai anggota, Anda bisa:")
            print(f"[1] {self.ui.DISCUSSION} Lihat diskusi terbaru")
            print(f"[2] {self.ui.SPARKLE} Buat postingan baru") 
            print(f"[3] {self.ui.MEMBERS} Lihat semua anggota")
            print(f"[4] {self.ui.CANCEL} Kembali")
            
            choice = input(f"\n{self.ui.SELECT} Pilihan Anda (1-4): ").strip()
            
            if choice == "1":
                self._view_community_discussions(username)
            elif choice == "2":
                self._create_community_post(username)
            elif choice == "3":
                self._view_community_members(username)
            
            return {"success": True, "message": "Already member - accessed community features", "already_member": True}
        
        print(f"\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        # Konfirmasi bergabung
        while True:
            print(f"\nApakah Anda ingin bergabung dengan '{community['name']}'?")
            print(f"[1] {self.ui.JOIN} Ya, saya ingin bergabung")
            print(f"[2] {self.ui.CANCEL} Tidak, lihat komunitas lain")
            print(f"[3] {self.ui.INFO} Tanyakan sesuatu dulu")
            
            choice = input(f"\n{self.ui.SELECT} Pilihan Anda (1-3): ").strip()
            
            if choice == "1":
                return self._join_community(username, community)
            elif choice == "2":
                print(f"{self.ui.INFO} Tidak apa-apa! Anda bisa bergabung kapan saja.")
                return {"success": False, "message": "User memilih tidak bergabung", "try_again": True}
            elif choice == "3":
                self._show_community_faq(community)
                continue  # Kembali ke pilihan bergabung
            else:
                print(f"{self.ui.WARNING} Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
    
    def _show_community_faq(self, community: Dict):
        """Tampilkan FAQ tentang komunitas"""
        
        print(f"\n{self.ui.INFO} FAQ - {community['name']}")
        print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        faq_items = [
            {
                "q": "Apakah ada biaya untuk bergabung?",
                "a": "Tidak ada biaya untuk bergabung. Komunitas ini gratis untuk semua anggota."
            },
            {
                "q": "Apakah saya harus datang ke setiap pertemuan?",
                "a": "Tidak wajib! Anda bisa berpartisipasi sesuai waktu dan kemampuan. Fleksibilitas adalah prioritas kami."
            },
            {
                "q": "Bagaimana cara berinteraksi dengan anggota lain?",
                "a": "Anda bisa diskusi online, datang ke pertemuan, atau ikut aktivitas grup yang diselenggarakan."
            },
            {
                "q": "Bisakah saya keluar jika tidak cocok?",
                "a": "Tentu saja! Anda bebas keluar kapan saja tanpa ada konsekuensi apapun."
            },
            {
                "q": "Apakah ada persyaratan khusus?",
                "a": f"Hanya semangat untuk berbagi dan belajar dalam bidang {community['category']}. Semua level welcome!"
            }
        ]
        
        for i, faq in enumerate(faq_items, 1):
            print(f"\n{i}. {faq['q']}")
            print(f"   💡 {faq['a']}")
        
        input(f"\n{self.ui.INFO} Tekan Enter untuk kembali ke pilihan bergabung...")
    
    def _join_community(self, username: str, community: Dict) -> Dict:
        """Proses bergabung dengan komunitas"""
        
        # Buat membership record
        membership = {
            "community_id": community["id"],
            "community_name": community["name"],
            "joined_date": time.strftime("%Y-%m-%d"),
            "status": "active",
            "role": "member"
        }
        
        # Simpan membership
        if username not in self.user_memberships:
            self.user_memberships[username] = []
        
        self.user_memberships[username].append(membership)
        
        # Update jumlah anggota (simulasi)
        community["members"] += 1
        
        print(f"\n{self.ui.CELEBRATION} Selamat! Anda berhasil bergabung dengan {community['name']}!")
        print(f"{self.ui.DISCUSSION} Sekarang Anda bisa berpartisipasi dalam diskusi dan kegiatan")
        print(f"{self.ui.HEART} Mari berkenalan dengan anggota lain!")
        
        return {
            "success": True,
            "message": f"Berhasil bergabung dengan {community['name']}",
            "community": community,
            "membership": membership
        }
    
    def _get_community_sample_activities(self, category: str) -> List[str]:
        """Dapatkan contoh aktivitas berdasarkan kategori komunitas"""
        
        activity_samples = {
            "hobi": [
                "Berbagi tips dan trik", 
                "Workshop mingguan", 
                "Kompetisi ramah"
            ],
            "edukasi": [
                "Diskusi buku bulanan", 
                "Sharing pengetahuan", 
                "Kelas pembelajaran"
            ],
            "olahraga": [
                "Sesi latihan bersama", 
                "Jalan sehat mingguan", 
                "Tips kesehatan"
            ],
            "kesehatan": [
                "Tips hidup sehat", 
                "Sesi latihan bersama", 
                "Konsultasi kesehatan"
            ]
        }
        
        return activity_samples.get(category, ["Diskusi dan sharing", "Kegiatan bersama"])
    
    def _view_community_discussions(self, username: str) -> Dict:
        """Lihat diskusi dalam komunitas"""
        
        print(f"\n{self.ui.DISCUSSION} Diskusi Terbaru:")
        
        # Simulasi diskusi
        discussions = [
            {"author": "Pak Budi", "topic": "Tips berkebun musim hujan", "replies": 5},
            {"author": "Bu Sari", "topic": "Resep masakan sehat untuk diabetes", "replies": 12},
            {"author": "Pak Joko", "topic": "Rekomendasi buku biografi", "replies": 8}
        ]
        
        for i, discussion in enumerate(discussions, 1):
            print(f"[{i}] {discussion['topic']}")
            print(f"    oleh {discussion['author']} • {discussion['replies']} balasan")
        
        return {"success": True, "discussions": discussions}
    
    def _create_community_post(self, username: str) -> Dict:
        """Buat postingan baru di komunitas"""
        
        print(f"\n{self.ui.SPARKLE} Buat Postingan Baru:")
        
        topic = input("Judul topik: ").strip()
        content = input("Isi postingan: ").strip()
        
        if topic and content:
            print(f"\n{self.ui.SUCCESS} Postingan '{topic}' berhasil dibuat!")
            print(f"{self.ui.DISCUSSION} Anggota lain bisa melihat dan merespon postingan Anda")
            return {"success": True, "topic": topic, "content": content}
        else:
            print(f"{self.ui.WARNING} Judul dan isi tidak boleh kosong")
            return {"success": False, "message": "Input tidak lengkap"}
    
    def _view_community_members(self, username: str) -> Dict:
        """Lihat anggota komunitas"""
        
        print(f"\n{self.ui.MEMBERS} Anggota Komunitas:")
        
        # Simulasi daftar anggota
        members = [
            {"name": "Pak Budi", "joined": "2024-01-15", "posts": 23},
            {"name": "Bu Sari", "joined": "2024-02-03", "posts": 45},
            {"name": "Pak Joko", "joined": "2024-01-28", "posts": 12},
            {"name": username, "joined": "2024-06-05", "posts": 1}
        ]
        
        for member in members:
            print(f"  {self.ui.PROFILE} {member['name']} - Bergabung: {member['joined']} ({member['posts']} postingan)")
        
        return {"success": True, "members": members}
    
    def _get_community_by_id(self, community_id: int) -> Optional[Dict]:
        """Cari komunitas berdasarkan ID"""
        
        for community in self.communities_db:
            if community["id"] == community_id:
                return community
        return None