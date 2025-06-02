from .states import ActivityState, FindActivityState

class ActivityContext:
    def __init__(self):
        self.state = FindActivityState()

    def set_state(self, state: ActivityState):
        self.state = state

    def process(self):
        while self.state:
            current_state = self.state
            self.state = None
            current_state.handle(self)
