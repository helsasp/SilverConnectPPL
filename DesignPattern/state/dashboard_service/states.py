from abc import ABC, abstractmethod

class DashboardState(ABC):
    def __init__(self, context):
        self.context = context

    @abstractmethod
    def handle(self):
        pass

class ViewDashboardState(DashboardState):
    def handle(self):
        print(f"\n👋 Halo, {self.context.username.capitalize()}! Selamat datang di SilverConnect 🌿")
        print("Dasbor personal Anda untuk kesejahteraan lansia dan koneksi sosial:\n")

        # Tombol atas
        print("🔘 [ Komunitas ]    🔘 [ Aktivitas ]    🔘 [ Teman ]\n")

        # Daftar milik pengguna
        print("🧑‍🤝‍🧑 Komunitas Anda:")
        print("- Klub Berkebun")
        print("- Kelompok Baca Buku")
        print("- Teman Jalan Kaki Lokal\n")

        print("🎯 Aktivitas Anda:")
        print("- Yoga Pagi jam 08.00")
        print("- Aerobik Kursi jam 10.00")
        print("- Permainan Memori Online\n")

        print("👥 Teman Anda:")
        print("- Bibi May")
        print("- Kakek Joe")
        print("- Nenek Lily\n")

        # Opsi
        print("📋 Opsi:")
        print("[1] Perbarui Profil")

class ViewProfileState(DashboardState):
    def handle(self):
        print(f"[Dasbor] Menampilkan profil pengguna '{self.context.username}'")
        print(f"👤 Nama Lengkap: {self.context.full_name}")
        print(f"📅 Tanggal Lahir: {self.context.dob}")
        print(f"📸 URL Foto: {self.context.photo_url}")
        print(f"🎨 Hobi: {', '.join(self.context.hobbies)}")

        choice = input("Apakah Anda ingin mengedit profil? (y/n): ").lower()
        if choice == "y":
            self.context.full_name = input("Masukkan nama lengkap: ") or self.context.full_name
            self.context.dob = input("Masukkan tanggal lahir (YYYY-MM-DD): ") or self.context.dob
            self.context.photo_url = input("Masukkan URL foto: ") or self.context.photo_url
            hobbies = input("Masukkan hobi, pisahkan dengan koma: ")
            if hobbies:
                self.context.hobbies = [h.strip() for h in hobbies.split(",")]
            print("[✓] Profil berhasil diperbarui.")

class SettingsState(DashboardState):
    def handle(self):
        print(f"[Dasbor] Pengguna '{self.context.username}' sedang memperbarui pengaturan")
