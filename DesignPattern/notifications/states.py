class NotificationState:
    def handle(self, context):
        pass

class ReceiveNotificationState(NotificationState):
    def handle(self, context):
        print("🔔 Menerima notifikasi dari sistem...")
