from friends_service.states import SearchFriendsState, ChatState

class FriendContext:
    def __init__(self, username=""):
        self.username = username
        self.friends = []

        self.search_friends_state = SearchFriendsState(self)
        self.chat_state = ChatState(self)

        self.state = self.search_friends_state

    def set_state(self, state):
        self.state = state

    def request(self):
        self.state.handle()
