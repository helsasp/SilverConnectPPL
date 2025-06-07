from abc import ABC, abstractmethod

class SettingsState(ABC):
    def __init__(self, context):
        self.context = context

    @abstractmethod
    def handle(self):
        pass

class FontSettingsState(SettingsState):
    def handle(self):
        print(f"[Pengaturan] Ukuran font saat ini: {self.context.font_size}")
        choice = input("Pilih ukuran font (Kecil / Sedang / Besar): ")
        if choice in ["Kecil", "Sedang", "Besar"]:
            self.context.font_size = choice
            print(f"[✓] Ukuran font berhasil diubah menjadi {choice}")
        else:
            print("[!] Input tidak valid. Tidak ada perubahan yang dilakukan.")

class ThemeSettingsState(SettingsState):
    def handle(self):
        print(f"[Pengaturan] Tema saat ini: {self.context.theme}")
        choice = input("Pilih tema (Terang / Gelap): ")
        if choice in ["Terang", "Gelap"]:
            self.context.theme = choice
            print(f"[✓] Tema berhasil diubah ke mode {choice}.")
        else:
            print("[!] Input tidak valid. Tidak ada perubahan yang dilakukan.")
