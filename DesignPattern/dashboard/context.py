from .states import DashboardState, ViewDashboardState

class DashboardContext:
    def __init__(self):
        self.state = ViewDashboardState()

    def set_state(self, state: DashboardState):
        self.state = state

    def process(self):
        while self.state:
            current_state = self.state
            self.state = None
            current_state.handle(self)
