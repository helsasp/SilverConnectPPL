from .states import CommunityState, FindCommunityState

class CommunityContext:
    def __init__(self):
        self.state = FindCommunityState()

    def set_state(self, state: CommunityState):
        self.state = state

    def process(self):
        while self.state:
            current_state = self.state
            self.state = None
            current_state.handle(self)
