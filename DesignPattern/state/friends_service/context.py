from friends_service.states import SearchFriendsState, ChatState, FriendDetailState

class FriendContext:
    def __init__(self, username=""):
        self.username = username
        self.friends = ["Alice", "Bob"]
        self.potential_friends = [
            {
                "name": "Charlie",
                "photo": "charlie.jpg",
                "interest": ["Gaming", "Reading"],
                "description": "A passionate gamer and bookworm.",
                "age": 25
            },
            {
                "name": "Diana",
                "photo": "diana.jpg",
                "interest": ["Cooking", "Yoga"],
                "description": "Loves healthy living and great food.",
                "age": 28
            },
            {
                "name": "Eve",
                "photo": "eve.jpg",
                "interest": ["Reading", "Yoga"],
                "description": "Quiet and thoughtful person.",
                "age": 30
            }
        ]
        self.added_friends = []

        self.search_friends_state = SearchFriendsState(self)
        self.chat_state = ChatState(self)
        self.friend_detail_state = FriendDetailState(self)

        self.state = self.search_friends_state

    def set_state(self, state):
        self.state = state

    def request(self, friend_name=None, interest_filter=None):
<<<<<<< HEAD
        self.state.handle(friend_name=friend_name, interest_filter=interest_filter)
=======
        self.state.handle(friend_name=friend_name, interest_filter=interest_filter)
>>>>>>> de7dacd (new commit)
