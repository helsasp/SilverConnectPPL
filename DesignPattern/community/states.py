class CommunityState:
    def handle(self, context):
        pass

class FindCommunityState(CommunityState):
    def handle(self, context):
        print("🔍 Mencari komunitas...")
        context.set_state(JoinCommunityState())

class JoinCommunityState(CommunityState):
    def handle(self, context):
        print("👥 Bergabung ke komunitas...")
        context.set_state(ChatCommunityState())

class ChatCommunityState(CommunityState):
    def handle(self, context):
        print("💬 Chat grup komunitas aktif.")
