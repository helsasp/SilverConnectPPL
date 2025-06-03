from dashboard_service.states import ViewDashboardState, ViewProfileState, SettingsState

class DashboardContext:
    def __init__(self, username=""):
        self.username = username

        # Default values
        self.full_name = "Unknown"
        self.dob = "1900-01-01"
        self.photo_url = "https://example.com/photo.jpg"
        self.hobbies = ["Walking", "Gardening"]

        self.dashboard_state = ViewDashboardState(self)
        self.profile_state = ViewProfileState(self)
        self.settings_state = SettingsState(self)

        self.state = self.dashboard_state

    def set_state(self, state):
        self.state = state

    def request(self):
        self.state.handle()
