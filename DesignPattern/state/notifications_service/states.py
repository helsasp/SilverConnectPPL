from abc import ABC, abstractmethod
import random
from datetime import datetime

class NotificationState(ABC):
    def __init__(self, context):
        self.context = context

    @abstractmethod
    def handle(self):
        pass

class CheckNotificationState(NotificationState):
    def handle(self):
        print(f"\n🔔 Checking notifications for user '{self.context.username}'...\n")

        # Simulated notification categories
        chat_messages = [
            "💬 Anna says: 'Will you be at the music session later?'",
            "💬 David: 'Good morning! Don’t forget our gardening meetup today 🌿'",
            "💬 Lisa: 'How are you feeling today? Let's catch up soon.'"
        ]

        activity_reminders = [
            "📅 Tai Chi at 8:00 AM in the garden – don’t forget your mat!",
            "🎨 Painting Class at 2:00 PM in Room B3 – brushes provided.",
            "🧁 Baking Workshop starts at 10:30 AM in the community kitchen."
        ]

        community_updates = [
            "👥 Welcome Margaret (Age 71) from Riverside Apartments to the Wellness Community!",
            "👥 Mr. Leo (Age 68) has joined the Poetry Club – feel free to greet him!",
            "👥 New member alert: Grandma Elsie (Age 76) – she loves knitting and storytelling!"
        ]

        wellness_tips = [
            "🧘 Tip of the Day: Gentle stretching each morning helps improve balance.",
            "🍵 Health Tip: Stay hydrated and drink herbal teas to soothe your body.",
            "🌞 Don’t forget to spend 10 minutes in the sunshine for Vitamin D!"
        ]

        event_announcements = [
            "🎉 Monthly Birthday Celebration this Friday at 4 PM – join us in the Hall!",
            "🎤 Talent Show Night: Share your hobby or skill this Saturday at 6 PM!",
            "🎶 Live music in the courtyard tomorrow morning – bring a friend!"
        ]

        inspiration_quotes = [
            "🕊️ 'You're never too old to set another goal or to dream a new dream.' – C.S. Lewis",
            "🌟 'Age is merely the number of years the world has been enjoying you!'",
            "❤️ 'A smile is the best makeup anyone can wear – especially you.'"
        ]

        # Combine a few from each category
        all_notifications = random.sample(chat_messages, k=1) + \
                            random.sample(activity_reminders, k=1) + \
                            random.sample(community_updates, k=1) + \
                            random.sample(wellness_tips, k=1) + \
                            random.sample(event_announcements, k=1) + \
                            random.sample(inspiration_quotes, k=1)

        self.context.notifications = all_notifications

        if not all_notifications:
            print("📭 No new notifications.")
        else:
            print("📬 You have new notifications:\n")
            for note in all_notifications:
<<<<<<< HEAD
                print(f" - {note}")
=======
                print(f" - {note}")
>>>>>>> de7dacd (new commit)
