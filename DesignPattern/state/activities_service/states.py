from abc import ABC, abstractmethod

class ActivityState(ABC):
    def __init__(self, context):
        self.context = context

    @abstractmethod
    def handle(self):
        pass

class FindActivityState(ActivityState):
    def handle(self):
        print(f"\n🎯 Mencari kegiatan untuk '{self.context.username}'...\n")
        self.context.activities = [
            {
                "id": 1,
                "name": "Yoga Pagi",
                "time": "07:00 WIB",
                "location": "Taman Komunitas",
                "photo": "🧘",
                "description": "Sesi yoga lembut untuk memulai hari.",
                "participants": 10
            },
            {
                "id": 2,
                "name": "Kelas Memasak",
                "time": "11:00 WIB",
                "location": "Dapur Pusat Lansia",
                "photo": "👩‍🍳",
                "description": "Belajar memasak makanan sehat bersama.",
                "participants": 8
            },
            {
                "id": 3,
                "name": "Terapi Seni",
                "time": "14:00 WIB",
                "location": "Aula Seni",
                "photo": "🎨",
                "description": "Ekspresikan emosi melalui lukisan.",
                "participants": 12
            }
        ]

        print("✨ Kegiatan yang Tersedia:\n")
        for idx, activity in enumerate(self.context.activities, 1):
            print(f"[{idx}] {activity['photo']} {activity['name']} pukul {activity['time']} - {activity['location']}")

        choice = input("\nPilih kegiatan untuk melihat detail (1-3): ")
        if choice.isdigit() and 1 <= int(choice) <= len(self.context.activities):
            self.context.selected_activity = self.context.activities[int(choice) - 1]
            self.context.set_state(self.context.book_activity_state)
        else:
            print("❗ Pilihan tidak valid.")

class BookActivityState(ActivityState):
    def handle(self):
        activity = self.context.selected_activity
        print(f"\n📄 Detail Kegiatan:\n")
        print(f"{activity['photo']} {activity['name']}")
        print(f"📍 Lokasi: {activity['location']}")
        print(f"🕒 Waktu: {activity['time']}")
        print(f"🧾 Deskripsi: {activity['description']}")
        print(f"👥 Jumlah Peserta: {activity['participants']}")

        confirm = input("\nApakah Anda ingin mendaftar kegiatan ini? (y/n): ").lower()
        if confirm == 'y':
            if not self.context.booked:
                self.context.booked = True
                print(f"\n✅ Anda berhasil mendaftar '{activity['name']}'!")
                print(f"📅 Jadwal Anda: {activity['name']} pukul {activity['time']} di {activity['location']}")
            else:
                print("⚠️ Anda sudah mendaftar kegiatan.")
        else:
            print("↩️ Pendaftaran dibatalkan.")
