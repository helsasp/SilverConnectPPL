from .states import FriendState, FindFriendState

class FriendContext:
    def __init__(self):
        self.state = FindFriendState()

    def set_state(self, state: FriendState):
        self.state = state

    def process(self):
        while self.state:
            current_state = self.state
            self.state = None
            current_state.handle(self)
