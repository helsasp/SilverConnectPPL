from .states import AuthState, SignUpState

class AuthContext:
    def __init__(self):
        self.state = SignUpState()

    def set_state(self, state: AuthState):
        self.state = state

    def process(self):
        while self.state:
            current_state = self.state
            self.state = None
            current_state.handle(self)
