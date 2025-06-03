from auth_service.states import LoginState, OnboardingState, SignupState, ForgotPasswordState

class AuthContext:
    def __init__(self, username="", password="", email="", full_name=""):
        self.username = username
        self.password = password
        self.email = email
        self.full_name = full_name
        self.profile_completed = False

        self.login_state = LoginState(self)
        self.onboarding_state = OnboardingState(self)
        self.signup_state = SignupState(self)
        self.forgot_password_state = ForgotPasswordState(self)

        self.state = self.login_state  # default state

    def set_state(self, state):
        self.state = state

    def request(self):
        self.state.handle()
