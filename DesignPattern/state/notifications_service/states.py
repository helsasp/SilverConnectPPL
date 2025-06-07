from abc import ABC, abstractmethod
import random
from datetime import datetime

class NotificationState(ABC):
    def __init__(self, context):
        self.context = context

    @abstractmethod
    def handle(self):
        pass

class CheckNotificationState(NotificationState):
    def handle(self):
        print(f"\n🔔 Memeriksa notifikasi untuk pengguna '{self.context.username}'...\n")

        # Kategori notifikasi simulasi
        chat_messages = [
            "💬 Anna berkata: 'Apakah kamu akan hadir di sesi musik nanti?'",
            "💬 David: 'Selamat pagi! Jangan lupa pertemuan berkebun kita hari ini 🌿'",
            "💬 Lisa: 'Bagaimana kabarmu hari ini? Yuk ngobrol sebentar.'"
        ]

        activity_reminders = [
            "📅 Tai Chi jam 8:00 pagi di taman – jangan lupa bawa matras!",
            "🎨 Kelas Melukis jam 14:00 di Ruang B3 – kuas sudah disediakan.",
            "🧁 Workshop Membuat Kue dimulai jam 10:30 di dapur komunitas."
        ]

        community_updates = [
            "👥 Selamat datang Margaret (Usia 71) dari Apartemen Riverside ke Komunitas Kesehatan!",
            "👥 Pak Leo (Usia 68) telah bergabung dengan Klub Puisi – jangan ragu untuk menyapanya!",
            "👥 Anggota baru: Nenek Elsie (Usia 76) – beliau suka merajut dan bercerita!"
        ]

        wellness_tips = [
            "🧘 Tips Hari Ini: Peregangan ringan setiap pagi membantu meningkatkan keseimbangan.",
            "🍵 Tips Kesehatan: Tetap terhidrasi dan minum teh herbal untuk menenangkan tubuh.",
            "🌞 Jangan lupa berjemur 10 menit di bawah sinar matahari untuk Vitamin D!"
        ]

        event_announcements = [
            "🎉 Perayaan Ulang Tahun Bulanan Jumat ini jam 16:00 – bergabunglah di Aula!",
            "🎤 Malam Unjuk Bakat: Tunjukkan hobi atau keahlianmu Sabtu jam 18:00!",
            "🎶 Musik langsung di halaman besok pagi – ajak teman juga ya!"
        ]

        inspiration_quotes = [
            "🕊️ 'Kamu tidak pernah terlalu tua untuk menetapkan tujuan baru atau bermimpi lagi.' – C.S. Lewis",
            "🌟 'Usia hanyalah angka yang menunjukkan berapa lama dunia telah menikmati kehadiranmu!'",
            "❤️ 'Senyuman adalah riasan terbaik yang bisa dipakai siapa pun – terutama kamu.'"
        ]

        # Menggabungkan beberapa dari tiap kategori
        all_notifications = random.sample(chat_messages, k=1) + \
                            random.sample(activity_reminders, k=1) + \
                            random.sample(community_updates, k=1) + \
                            random.sample(wellness_tips, k=1) + \
                            random.sample(event_announcements, k=1) + \
                            random.sample(inspiration_quotes, k=1)

        self.context.notifications = all_notifications

        if not all_notifications:
            print("📭 Tidak ada notifikasi baru.")
        else:
            print("📬 Kamu memiliki notifikasi baru:\n")
            for note in all_notifications:
                print(f" - {note}")
