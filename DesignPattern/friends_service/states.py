from abc import ABC, abstractmethod

class FriendState(ABC):
    def __init__(self, context):
        self.context = context

    @abstractmethod
    def handle(self):
        pass

class SearchFriendsState(FriendState):
    def handle(self):
        print(f"[Friends] Searching friends for user '{self.context.username}'...")
        self.context.friends = ["Alice", "Bob"]
        print(f"[Friends] Friends found: {', '.join(self.context.friends)}")
        self.context.set_state(self.context.chat_state)

class ChatState(FriendState):
    def handle(self):
        if not self.context.friends:
            print("[Friends] No friends found to chat.")
            return
        print(f"[Friends] User '{self.context.username}' chatting with '{self.context.friends[0]}'...")
        print(f"[Friends] Message sent: Hi {self.context.friends[0]}!")
