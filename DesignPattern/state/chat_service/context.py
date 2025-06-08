from chat_service.states import ChatStartState, ChatSendMessageState

class ChatContext:
    def __init__(self, username):
        self.username = username
        self.friend_name = None
        self.message = None
        self.state = ChatStartState(self)

    def set_state(self, state):
        self.state = state

    def request(self, friend_name=None, message=None):
        if friend_name:
            self.friend_name = friend_name
        if message:
            self.message = message
        self.state.handle()
