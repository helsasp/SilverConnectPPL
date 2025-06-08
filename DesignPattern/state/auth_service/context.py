from auth_service.states import (
    LoginState, SignupState, OnboardingState, ForgotPasswordState, ProfileSetupState
)

class AuthContext:
    def __init__(self, username=None, password=None, confirm_password=None, email=None, full_name=None):
        self.username = username
        self.password = password
        self.confirm_password = confirm_password
        self.email = email
        self.full_name = full_name
        self.mode = None
        self.hobbies = []
        self.story = ""
        self.profile_completed = False

        self.signup_state = SignupState(self)
        self.login_state = LoginState(self)
        self.onboarding_state = OnboardingState(self)
        self.forgot_password_state = ForgotPasswordState(self)
        self.profile_setup_state = ProfileSetupState(self)

        self.state = None

    def set_state(self, state):
        self.state = state

    def request(self):
        if self.state:
            self.state.handle()
        else:
            print("[Auth] Tidak ada state yang aktif.")
