from abc import ABC, abstractmethod

class DashboardState(ABC):
    def __init__(self, context):
        self.context = context

    @abstractmethod
    def handle(self):
        pass

class ViewDashboardState(DashboardState):
    def handle(self):
        print(f"\n👋 Hello, {self.context.username.capitalize()}! Welcome to SilverConnect 🌿")
        print("Your personalized dashboard for elderly well-being and social connection:\n")

        # Top buttons
        print("🔘 [ Community ]    🔘 [ Activity ]    🔘 [ Friend ]\n")

        # Lists owned by the user
        print("🧑‍🤝‍🧑 Your Communities:")
        print("- Gardening Club")
        print("- Book Reading Group")
        print("- Local Walking Buddies\n")

        print("🎯 Your Activities:")
        print("- Morning Yoga at 8AM")
        print("- Chair Aerobics at 10AM")
        print("- Online Memory Game\n")

        print("👥 Your Friends:")
        print("- Aunt May")
        print("- Grandpa Joe")
        print("- Nana Lily\n")

        # Options
        print("📋 Options:")
        print("[1] Update Profile")

class ViewProfileState(DashboardState):
    def handle(self):
        print(f"[Dashboard] Showing profile of user '{self.context.username}'")

class SettingsState(DashboardState):
    def handle(self):
        print(f"[Dashboard] User '{self.context.username}' updating settings")
class ViewProfileState(DashboardState):
    def handle(self):
        print(f"[Dashboard] Showing profile of user '{self.context.username}'")
        print(f"👤 Full Name: {self.context.full_name}")
        print(f"📅 Date of Birth: {self.context.dob}")
        print(f"📸 Photo URL: {self.context.photo_url}")
        print(f"🎨 Hobbies: {', '.join(self.context.hobbies)}")

        choice = input("Do you want to edit your profile? (y/n): ").lower()
        if choice == "y":
            self.context.full_name = input("Enter full name: ") or self.context.full_name
            self.context.dob = input("Enter date of birth (YYYY-MM-DD): ") or self.context.dob
            self.context.photo_url = input("Enter photo URL: ") or self.context.photo_url
            hobbies = input("Enter hobbies separated by comma: ")
            if hobbies:
                self.context.hobbies = [h.strip() for h in hobbies.split(",")]
            print("[✓] Profile updated successfully.")
