from dashboard_service.states import ViewDashboardState, ViewProfileState, SettingsState

class DashboardContext:
    def __init__(self, username=""):
        self.username = username

        self.dashboard_state = ViewDashboardState(self)
        self.profile_state = ViewProfileState(self)
        self.settings_state = SettingsState(self)

        self.state = self.dashboard_state

    def set_state(self, state):
        self.state = state

    def request(self):
        self.state.handle()
