from .states import NotificationState, ReceiveNotificationState

class NotificationContext:
    def __init__(self):
        self.state = ReceiveNotificationState()

    def set_state(self, state: NotificationState):
        self.state = state

    def process(self):
        while self.state:
            current_state = self.state
            self.state = None
            current_state.handle(self)
