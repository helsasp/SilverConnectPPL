from abc import ABC, abstractmethod

class SettingsState(ABC):
    def __init__(self, context):
        self.context = context

    @abstractmethod
    def handle(self):
        pass

class FontSettingsState(SettingsState):
    def handle(self):
        print(f"[Settings] Current font size: {self.context.font_size}")
        choice = input("Choose font size (Small / Medium / Large): ")
        if choice in ["Small", "Medium", "Large"]:
            self.context.font_size = choice
            print(f"[✓] Font size updated to {choice}")
        else:
            print("[!] Invalid input. No changes made.")

class ThemeSettingsState(SettingsState):
    def handle(self):
        print(f"[Settings] Current theme: {self.context.theme}")
        choice = input("Choose theme (Light / Dark): ")
        if choice in ["Light", "Dark"]:
            self.context.theme = choice
            print(f"[✓] Theme updated to {choice} mode.")
        else:
            print("[!] Invalid input. No changes made.")
