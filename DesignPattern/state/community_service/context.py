from community_service.states import BrowseCommunityState, JoinCommunityState

class CommunityContext:
    def __init__(self, username=""):
        self.username = username
        self.communities = []
        self.joined = False

        self.browse_community_state = BrowseCommunityState(self)
        self.join_community_state = JoinCommunityState(self)

        self.state = self.browse_community_state

    def set_state(self, state):
        self.state = state

    def request(self):
        self.state.handle()
