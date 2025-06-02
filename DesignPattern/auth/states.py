class AuthState:
    def handle(self, context):
        pass

class SignUpState(AuthState):
    def handle(self, context):
        print("📘 State: SignUp")
        context.set_state(SignInState())

class SignInState(AuthState):
    def handle(self, context):
        print("📘 State: SignIn")
        context.set_state(OnboardingState())

class OnboardingState(AuthState):
    def handle(self, context):
        print("📘 State: Onboarding")
        print("✅ Auth Flow Selesai")
