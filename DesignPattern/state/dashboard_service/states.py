from abc import ABC, abstractmethod

class DashboardState(ABC):
    def __init__(self, context):
        self.context = context

    @abstractmethod
    def handle(self):
        pass

class ViewDashboardState(DashboardState):
    def handle(self):
        print(f"[Dashboard] Showing dashboard for user '{self.context.username}'")

class ViewProfileState(DashboardState):
    def handle(self):
        print(f"[Dashboard] Showing profile of user '{self.context.username}'")

class SettingsState(DashboardState):
    def handle(self):
        print(f"[Dashboard] User '{self.context.username}' updating settings")
