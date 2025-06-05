from activities_service.states import FindActivityState, BookActivityState

class ActivityContext:
    def __init__(self, username=""):
        self.username = username
        self.activities = []
        self.selected_activity = None
        self.booked = False

        self.find_activity_state = FindActivityState(self)
        self.book_activity_state = BookActivityState(self)

        self.state = self.find_activity_state

    def set_state(self, state):
        self.state = state

    def request(self):
        self.state.handle()