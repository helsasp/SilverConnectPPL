from abc import ABC, abstractmethod

class FriendState(ABC):
    def __init__(self, context):
        self.context = context

    @abstractmethod
    def handle(self, friend_name=None, interest_filter=None, action=None):
        pass


class SearchFriendsState(FriendState):
    def handle(self, friend_name=None, interest_filter=None, action=None):
        print("[Teman] Menampilkan orang yang mungkin Anda kenal:")
        filtered = self.context.potential_friends
        if interest_filter:
            filtered = [p for p in filtered if interest_filter in p["interest"]]
            print(f"[Filter] Menampilkan pengguna dengan minat: {interest_filter}")

        if not filtered:
            print("Tidak ada pengguna yang ditemukan dengan minat tersebut.")
        else:
            for person in filtered:
                print(f"- {person['name']} | Minat: {', '.join(person['interest'])}")

       
        self.context.set_state(self.context.friend_detail_state)


class FriendDetailState(FriendState):
    def handle(self, friend_name=None, interest_filter=None, action=None):
        if not friend_name:
            print("[Teman] Silakan masukkan nama untuk melihat detail.")
            return

        match = next((p for p in self.context.potential_friends if p["name"] == friend_name), None)
        if not match:
            print(f"[Teman] Tidak ditemukan detail untuk {friend_name}.")
            return

        print(f"\n=== Detail untuk {match['name']} ===")
        print(f"Foto: {match['photo']}")
        print(f"Nama: {match['name']}")
        print(f"Usia: {match['age']}")
        print(f"Minat: {', '.join(match['interest'])}")
        print(f"Deskripsi: {match['description']}")

        if match['name'] in self.context.added_friends:
            print("Status: Sudah menjadi teman Anda ✅")
        else:
            if action == "add":
                self.context.added_friends.append(match['name'])
                print(f"✅ Permintaan pertemanan dikirim ke {match['name']}!")
            else:
                print("Aksi: [Tambah Teman]")

        if action == "like":
            if match['name'] not in self.context.liked_friends:
                self.context.liked_friends.append(match['name'])
                print(f"❤️ Anda menyukai {match['name']}!")
            else:
                print(f"❤️ Anda sudah menyukai {match['name']} sebelumnya.")

        if action == "chat":
            print(f"[Obrolan] Anda memulai percakapan dengan {match['name']}...")
            print(f"[Obrolan] Anda: Hai {match['name']}! Senang bisa terhubung.")

        print("Aksi tersedia: [Tambah Teman], [Like], [Chat]")
        

        self.context.set_state(self.context.search_friends_state)


class ChatState(FriendState):
    def handle(self, friend_name=None, interest_filter=None, action=None):
        if not self.context.friends:
            print("[Teman] Tidak ada teman untuk diajak mengobrol.")
            return
        print(f"[Teman] Pengguna '{self.context.username}' sedang mengobrol dengan '{self.context.friends[0]}'...")
        print(f"[Teman] Pesan terkirim: Hai {self.context.friends[0]}!")
