class DashboardState:
    def handle(self, context):
        pass

class ViewDashboardState(DashboardState):
    def handle(self, context):
        print("📊 Menampilkan dashboard pengguna...")
        context.set_state(ViewProfileState())

class ViewProfileState(DashboardState):
    def handle(self, context):
        print("👤 Melihat profil...")
        context.set_state(UpdateSettingsState())

class UpdateSettingsState(DashboardState):
    def handle(self, context):
        print("⚙️ Memperbarui pengaturan...")
