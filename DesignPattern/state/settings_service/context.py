from settings_service.states import FontSettingsState, ThemeSettingsState

class SettingsContext:
    def __init__(self, username=""):
        self.username = username
        self.font_size = "Medium"
        self.theme = "Light"

        self.font_state = FontSettingsState(self)
        self.theme_state = ThemeSettingsState(self)
        self.state = self.font_state

    def set_state(self, state):
        self.state = state

    def request(self):
<<<<<<< HEAD
        self.state.handle()
=======
        self.state.handle()
>>>>>>> de7dacd (new commit)
