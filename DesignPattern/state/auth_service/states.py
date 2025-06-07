from abc import ABC, abstractmethod

class AuthState(ABC):
    def __init__(self, context):
        self.context = context

    @abstractmethod
    def handle(self):
        pass

class LoginState(AuthState):
    def handle(self):
        print(f"[Auth] Pengguna '{self.context.username}' mencoba masuk...")
        if self.context.username == "elder1" and self.context.password == "pass123":
            print("[Auth] Masuk berhasil!")
            self.context.set_state(self.context.onboarding_state)
        else:
            print("[Auth] Gagal masuk! Nama pengguna atau kata sandi salah.")

class OnboardingState(AuthState):
    def handle(self):
        print(f"[Auth] Menjalankan onboarding untuk pengguna '{self.context.username}'...")
        self.context.profile_completed = True
        print(f"[Auth] Onboarding selesai untuk pengguna '{self.context.username}'")

class SignupState(AuthState):
    def handle(self):
        print(f"[Auth] Mendaftarkan pengguna dengan email '{self.context.email}'...")
        # Simulasi penyimpanan akun
        if self.context.email and self.context.password and self.context.full_name:
            print(f"[Auth] Akun berhasil dibuat untuk '{self.context.email}' dengan nama '{self.context.full_name}'")
            self.context.set_state(self.context.login_state)
        else:
            print("[Auth] Gagal mendaftar: Informasi tidak lengkap.")

class ForgotPasswordState(AuthState):
    def handle(self):
        print(f"[Auth] Permintaan atur ulang kata sandi untuk '{self.context.email}'...")
        if self.context.email:
            print(f"[Auth] Email konfirmasi telah dikirim ke '{self.context.email}'")
            # Simulasi email confirmation dan reset
            self.context.password = "kata_sandi_baru_123"
            print(f"[Auth] Kata sandi telah direset ke '{self.context.password}' (hanya simulasi)")
            self.context.set_state(self.context.login_state)
        else:
            print("[Auth] Tidak ada email yang diberikan. Tidak dapat mereset kata sandi.")
