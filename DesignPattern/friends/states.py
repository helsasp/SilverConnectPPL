class FriendState:
    def handle(self, context):
        pass

class FindFriendState(FriendState):
    def handle(self, context):
        print("🤝 Mencari teman berdasarkan minat...")
        context.set_state(SendFriendRequestState())

class SendFriendRequestState(FriendState):
    def handle(self, context):
        print("📨 Mengirim permintaan teman...")
        context.set_state(ChatFriendState())

class ChatFriendState(FriendState):
    def handle(self, context):
        print("💬 Mulai chat dengan teman")
