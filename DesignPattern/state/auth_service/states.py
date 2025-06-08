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
        print(f"[Auth] Mendaftarkan pengguna dengan email '{self.context.email}' dan username '{self.context.username}'...")
        
        if not (self.context.email and self.context.password and self.context.confirm_password and self.context.username and self.context.full_name):
            print("[Auth] Gagal mendaftar: Informasi tidak lengkap.")
            return
        
        if self.context.password != self.context.confirm_password:
            print("[Auth] Gagal mendaftar: Password dan konfirmasi password tidak sama.")
            return
        
        # Simulasi penyimpanan akun berhasil
        print(f"[Auth] Akun berhasil dibuat untuk '{self.context.email}' dengan username '{self.context.username}' dan nama '{self.context.full_name}'")
        self.context.set_state(self.context.profile_setup_state)

class ProfileSetupState(AuthState):
    def handle(self):
        print(f"[Auth] Silakan lengkapi profil untuk pengguna '{self.context.username}'")
        
        # Pilih mode: pertemanan / cinta
        mode = input("Pilih mode (pertemanan/cinta): ").strip().lower()
        while mode not in ['pertemanan', 'cinta']:
            print("Mode tidak valid. Pilih 'pertemanan' atau 'cinta'.")
            mode = input("Pilih mode (pertemanan/cinta): ").strip().lower()
        self.context.mode = mode

        # Input hobi (pisahkan dengan koma jika lebih dari satu)
        hobbies = input("Masukkan hobi (pisahkan dengan koma jika lebih dari satu): ").strip()
        self.context.hobbies = [h.strip() for h in hobbies.split(',') if h.strip()]

        # Cerita pengalaman
        story = input("Ceritakan pengalamanmu (singkat): ").strip()
        self.context.story = story

        print(f"[Auth] Profil lengkap dengan mode '{self.context.mode}', hobi {self.context.hobbies}, dan cerita pengalaman tersimpan.")
        # Setelah selesai, lanjut ke login
        self.context.set_state(self.context.login_state)

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
