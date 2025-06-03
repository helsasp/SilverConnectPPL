from abc import ABC, abstractmethod

class NotificationState(ABC):
    def __init__(self, context):
        self.context = context

    @abstractmethod
    def handle(self):
        pass

class CheckNotificationState(NotificationState):
    def handle(self):
        print(f"[Notifications] Checking notifications for user '{self.context.username}'")
        self.context.notifications = ["You have 3 new messages", "Your activity was approved"]
        print(f"[Notifications] Notifications: {', '.join(self.context.notifications)}")
