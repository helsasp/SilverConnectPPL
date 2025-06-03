from notifications_service.states import CheckNotificationState

class NotificationContext:
    def __init__(self, username=""):
        self.username = username
        self.notifications = []

        self.check_notification_state = CheckNotificationState(self)

        self.state = self.check_notification_state

    def set_state(self, state):
        self.state = state

    def request(self):
        self.state.handle()
