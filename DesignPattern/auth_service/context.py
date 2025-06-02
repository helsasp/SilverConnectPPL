from auth_service.states import LoginState, OnboardingState

class AuthContext:
    def __init__(self, username="", password=""):
        self.username = username
        self.password = password
        self.profile_completed = False

        self.login_state = LoginState(self)
        self.onboarding_state = OnboardingState(self)

        self.state = self.login_state

    def set_state(self, state):
        self.state = state

    def request(self):
        self.state.handle()
