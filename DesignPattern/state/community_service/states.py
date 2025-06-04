from abc import ABC, abstractmethod

class DashboardState(ABC):
    def __init__(self, context):
        self.context = context

    @abstractmethod
    def handle(self):
        pass

class BrowseCommunityState(DashboardState):
    def handle(self):
        print("\n🧑‍🤝‍🧑 Browse Communities:\n")
        self.context.communities = [
            {
                "id": 1,
                "name": "Gardening Club",
                "photo": "🌱",
                "description": "A place for plant lovers to share tips and stories.",
                "members": 12
            },
            {
                "id": 2,
                "name": "Book Reading Group",
                "photo": "📚",
                "description": "Join fellow readers and discuss your favorite books.",
                "members": 8
            },
            {
                "id": 3,
                "name": "Walking Buddies",
                "photo": "🚶",
                "description": "Find walking partners around your neighborhood.",
                "members": 15
            }
        ]

        for idx, community in enumerate(self.context.communities, 1):
            print(f"[{idx}] {community['photo']} {community['name']} - {community['members']} members")

        choice = input("\nSelect a community to view details (1-3): ")
        if choice.isdigit() and 1 <= int(choice) <= len(self.context.communities):
            selected = self.context.communities[int(choice) - 1]
            self.context.selected_community = selected
            self.context.set_state(self.context.join_community_state)
        else:
            print("❗ Invalid selection, returning to dashboard.")

class JoinCommunityState(DashboardState):
    def handle(self):
        community = self.context.selected_community
        print(f"\n📄 Community Detail:\n")
        print(f"{community['photo']} {community['name']}")
        print(f"📃 Description: {community['description']}")
        print(f"👥 Members: {community['members']}")

        join = input("\nDo you want to join this community? (y/n): ").lower()
        if join == "y":
            if not self.context.joined:
                self.context.joined = True
                print(f"✅ You have successfully joined {community['name']}!")
                print("💬 Entering the community group chat...\n")

                # Simulasi group chat
                print(f"[{community['name']} Group Chat]")
                print("👤 Admin: Welcome to the group!")
                print("👵 Grandma Sue: Excited to share my gardening tips!")
                print("👴 Grandpa Rick: Let’s plant tomatoes together 🌿")
            else:
                print("⚠️ You have already joined a community.")
        else:
            print("↩️ Returning without joining.")
