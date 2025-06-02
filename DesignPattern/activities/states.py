class ActivityState:
    def handle(self, context):
        pass

class FindActivityState(ActivityState):
    def handle(self, context):
        print("🧭 Mencari aktivitas...")
        context.set_state(BookActivityState())

class BookActivityState(ActivityState):
    def handle(self, context):
        print("📅 Memesan aktivitas...")
        print("✅ Aktivitas berhasil dipesan.")
