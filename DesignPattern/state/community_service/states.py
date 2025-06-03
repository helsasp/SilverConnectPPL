from abc import ABC, abstractmethod

class CommunityState(ABC):
    def __init__(self, context):
        self.context = context

    @abstractmethod
    def handle(self):
        pass

class BrowseCommunityState(CommunityState):
    def handle(self):
        print(f"[Community] User '{self.context.username}' browsing communities...")
        self.context.communities = ["Sports", "Gamers", "Artists"]
        print(f"[Community] Communities: {', '.join(self.context.communities)}")
        self.context.set_state(self.context.join_community_state)

class JoinCommunityState(CommunityState):
    def handle(self):
        if not self.context.communities:
            print("[Community] No communities to join.")
            return
        community = self.context.communities[0]
        print(f"[Community] User '{self.context.username}' joined community '{community}'")
        self.context.joined = True
