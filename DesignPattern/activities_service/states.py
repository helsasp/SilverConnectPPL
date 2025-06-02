from abc import ABC, abstractmethod

class ActivityState(ABC):
    def __init__(self, context):
        self.context = context

    @abstractmethod
    def handle(self):
        pass

class FindActivityState(ActivityState):
    def handle(self):
        print(f"[Activities] User '{self.context.username}' looking for activities...")
        self.context.activities = ["Yoga", "Cooking", "Painting"]
        print(f"[Activities] Activities found: {', '.join(self.context.activities)}")
        self.context.set_state(self.context.book_activity_state)

class BookActivityState(ActivityState):
    def handle(self):
        if not self.context.activities:
            print("[Activities] No activities found.")
            return
        activity = self.context.activities[0]
        print(f"[Activities] User '{self.context.username}' booked '{activity}' activity")
        self.context.booked = True
