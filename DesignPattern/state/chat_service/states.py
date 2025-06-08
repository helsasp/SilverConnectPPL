class ChatState:
    def __init__(self, context):
        self.context = context

    def handle(self):
        raise NotImplementedError("Harus diimplementasikan oleh subclass")

class ChatStartState(ChatState):
    def handle(self):
        if self.context.friend_name:
            print(f"\n👵 Memulai obrolan dengan {self.context.friend_name}...")
            print("💬 Kamu bisa mulai mengetik pesanmu.")
            self.context.set_state(ChatSendMessageState(self.context))
        else:
            print("⚠️ Harap masukkan nama teman untuk memulai chat.")

class ChatSendMessageState(ChatState):
    def handle(self):
        if self.context.message:
            print(f"📤 Mengirim pesan ke {self.context.friend_name}: {self.context.message}")
        else:
            print("✍️ Belum ada pesan untuk dikirim.")
