from abc import ABC, abstractmethod

class FriendState(ABC):
    def __init__(self, context):
        self.context = context

    @abstractmethod
    def handle(self, friend_name=None, interest_filter=None):
        pass

class SearchFriendsState(FriendState):
    def handle(self, friend_name=None, interest_filter=None):
        print("[Friends] Listing people you may know:")
        filtered = self.context.potential_friends
        if interest_filter:
            filtered = [p for p in filtered if interest_filter in p["interest"]]
            print(f"[Filter] Showing users with interest: {interest_filter}")

        if not filtered:
            print("No users found with that interest.")
        else:
            for person in filtered:
                print(f"- {person['name']} | Interests: {', '.join(person['interest'])}")

        print("Use request(friend_name='Name') to view details.")
        self.context.set_state(self.context.friend_detail_state)

class FriendDetailState(FriendState):
    def handle(self, friend_name=None, interest_filter=None):
        if not friend_name:
            print("[Friends] Please provide a name to view details.")
            return

        match = next((p for p in self.context.potential_friends if p["name"] == friend_name), None)
        if not match:
            print(f"[Friends] No details found for {friend_name}.")
            return

        print(f"\n=== Detail for {match['name']} ===")
        print(f"Photo: {match['photo']}")
        print(f"Name: {match['name']}")
        print(f"Age: {match['age']}")
        print(f"Interest: {', '.join(match['interest'])}")
        print(f"Description: {match['description']}")

        if match['name'] in self.context.added_friends:
            print("Status: Already your friend ✅")
        else:
            print("Action: [Add Friend]")
            self.context.added_friends.append(match['name'])
            print(f"✅ Friend request sent to {match['name']}!")

        self.context.set_state(self.context.search_friends_state)

class ChatState(FriendState):
    def handle(self, friend_name=None, interest_filter=None):
        if not self.context.friends:
            print("[Friends] No friends found to chat.")
            return
        print(f"[Friends] User '{self.context.username}' chatting with '{self.context.friends[0]}'...")
        print(f"[Friends] Message sent: Hi {self.context.friends[0]}!")
