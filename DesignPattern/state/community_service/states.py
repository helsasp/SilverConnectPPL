from abc import ABC, abstractmethod

class DashboardState(ABC):
    def __init__(self, context):
        self.context = context

    @abstractmethod
    def handle(self):
        pass

class BrowseCommunityState(DashboardState):
    def handle(self):
        print("\n🧑‍🤝‍🧑 Jelajahi Komunitas:\n")
        self.context.communities = [
            {
                "id": 1,
                "name": "Klub Berkebun",
                "photo": "🌱",
                "description": "Tempat untuk para pecinta tanaman berbagi tips dan cerita.",
                "members": 12
            },
            {
                "id": 2,
                "name": "Kelompok Baca Buku",
                "photo": "📚",
                "description": "Bergabung dengan sesama pembaca dan diskusikan buku favoritmu.",
                "members": 8
            },
            {
                "id": 3,
                "name": "Teman Jalan Kaki",
                "photo": "🚶",
                "description": "Cari teman jalan kaki di sekitar lingkunganmu.",
                "members": 15
            }
        ]

        for idx, community in enumerate(self.context.communities, 1):
            print(f"[{idx}] {community['photo']} {community['name']} - {community['members']} anggota")

        choice = input("\nPilih komunitas untuk lihat detail (1-3): ")
        if choice.isdigit() and 1 <= int(choice) <= len(self.context.communities):
            selected = self.context.communities[int(choice) - 1]
            self.context.selected_community = selected
            self.context.set_state(self.context.join_community_state)
        else:
            print("❗ Pilihan tidak valid, kembali ke dashboard.")

class JoinCommunityState(DashboardState):
    def handle(self):
        community = self.context.selected_community
        print(f"\n📄 Detail Komunitas:\n")
        print(f"{community['photo']} {community['name']}")
        print(f"📃 Deskripsi: {community['description']}")
        print(f"👥 Jumlah Anggota: {community['members']}")

        join = input("\nApakah kamu ingin bergabung dengan komunitas ini? (y/n): ").lower()
        if join == "y":
            if not self.context.joined:
                self.context.joined = True
                print(f"✅ Kamu berhasil bergabung dengan {community['name']}!")
                print("💬 Masuk ke obrolan grup komunitas...\n")

                # Simulasi obrolan grup
                print(f"[Grup {community['name']}]")
                print("👤 Admin: Selamat datang di grup!")
                print("👵 Nenek Sue: Tidak sabar membagikan tips berkebun saya!")
                print("👴 Kakek Rick: Ayo tanam tomat bersama 🌿")
            else:
                print("⚠️ Kamu sudah bergabung dengan komunitas.")
        else:
            print("↩️ Kembali tanpa bergabung.")
