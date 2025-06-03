from abc import ABC, abstractmethod

class AuthState(ABC):
    def __init__(self, context):
        self.context = context

    @abstractmethod
    def handle(self):
        pass

class LoginState(AuthState):
    def handle(self):
        print(f"[Auth] User '{self.context.username}' login attempt...")
        if self.context.username == "elder1" and self.context.password == "pass123":
            print("[Auth] Login successful!")
            self.context.set_state(self.context.onboarding_state)
        else:
            print("[Auth] Login failed!")

class OnboardingState(AuthState):
    def handle(self):
        print(f"[Auth] Onboarding user '{self.context.username}'...")
        self.context.profile_completed = True
        print(f"[Auth] Onboarding completed for user '{self.context.username}'")

class SignupState(AuthState):
    def handle(self):
        print(f"[Auth] Signing up user '{self.context.email}'...")
        # Simulasi penyimpanan akun
        if self.context.email and self.context.password and self.context.full_name:
            print(f"[Auth] Account created for '{self.context.email}' with name '{self.context.full_name}'")
            self.context.set_state(self.context.login_state)
        else:
            print("[Auth] Signup failed: Missing information.")

class ForgotPasswordState(AuthState):
    def handle(self):
        print(f"[Auth] Password reset requested for '{self.context.email}'...")
        if self.context.email:
            print(f"[Auth] Confirmation email sent to '{self.context.email}'")
            # Simulasi email confirmation dan reset
            self.context.password = "new_password_123"
            print(f"[Auth] Password has been reset to '{self.context.password}' (for simulation only)")
            self.context.set_state(self.context.login_state)
        else:
            print("[Auth] No email provided. Cannot reset password.")
