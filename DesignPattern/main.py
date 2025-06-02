from auth.context import AuthContext
from friends.context import FriendContext
from community.context import CommunityContext
from activities.context import ActivityContext
from dashboard.context import DashboardContext
from notifications.context import NotificationContext

def main():
    print("=== [AUTH FLOW] ===")
    auth = AuthContext()
    auth.process()

    print("\n=== [FRIENDS FLOW] ===")
    friends = FriendContext()
    friends.process()

    print("\n=== [COMMUNITY FLOW] ===")
    community = CommunityContext()
    community.process()

    print("\n=== [ACTIVITIES FLOW] ===")
    activity = ActivityContext()
    activity.process()

    print("\n=== [DASHBOARD FLOW] ===")
    dashboard = DashboardContext()
    dashboard.process()

    print("\n=== [NOTIFICATION FLOW] ===")
    notif = NotificationContext()
    notif.process()

if __name__ == "__main__":
    main()
