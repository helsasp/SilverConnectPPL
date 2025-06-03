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
