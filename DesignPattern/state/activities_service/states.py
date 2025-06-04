from abc import ABC, abstractmethod

class ActivityState(ABC):
    def __init__(self, context):
        self.context = context

    @abstractmethod
    def handle(self):
        pass

class FindActivityState(ActivityState):
    def handle(self):
        print(f"\n🎯 Finding activities for '{self.context.username}'...\n")
        self.context.activities = [
            {
                "id": 1,
                "name": "Morning Yoga",
                "time": "07:00 AM",
                "location": "Community Park",
                "photo": "🧘",
                "description": "Gentle yoga session to start the day.",
                "participants": 10
            },
            {
                "id": 2,
                "name": "Cooking Class",
                "time": "11:00 AM",
                "location": "Senior Center Kitchen",
                "photo": "👩‍🍳",
                "description": "Learn to cook healthy meals together.",
                "participants": 8
            },
            {
                "id": 3,
                "name": "Art Therapy",
                "time": "02:00 PM",
                "location": "Art Hall",
                "photo": "🎨",
                "description": "Express emotions through painting.",
                "participants": 12
            }
        ]

        print("✨ Available Activities:\n")
        for idx, activity in enumerate(self.context.activities, 1):
            print(f"[{idx}] {activity['photo']} {activity['name']} at {activity['time']} - {activity['location']}")

        choice = input("\nSelect an activity to view details (1-3): ")
        if choice.isdigit() and 1 <= int(choice) <= len(self.context.activities):
            self.context.selected_activity = self.context.activities[int(choice) - 1]
            self.context.set_state(self.context.book_activity_state)
        else:
            print("❗ Invalid choice.")

class BookActivityState(ActivityState):
    def handle(self):
        activity = self.context.selected_activity
        print(f"\n📄 Activity Details:\n")
        print(f"{activity['photo']} {activity['name']}")
        print(f"📍 Location: {activity['location']}")
        print(f"🕒 Time: {activity['time']}")
        print(f"🧾 Description: {activity['description']}")
        print(f"👥 Participants: {activity['participants']}")

        confirm = input("\nDo you want to book this activity? (y/n): ").lower()
        if confirm == 'y':
            if not self.context.booked:
                self.context.booked = True
                print(f"\n✅ You have successfully booked '{activity['name']}'!")
                print(f"📅 Your Schedule: {activity['name']} at {activity['time']} on {activity['location']}")
            else:
                print("⚠️ You already booked an activity.")
        else:
            print("↩️ Booking cancelled.")
