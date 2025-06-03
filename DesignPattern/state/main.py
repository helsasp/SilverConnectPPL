from auth_service.context import AuthContext
from friends_service.context import FriendContext
from community_service.context import CommunityContext
from activities_service.context import ActivityContext
from dashboard_service.context import DashboardContext
from notifications_service.context import NotificationContext

def main():
    username = "elder1"
    password = "pass123"

    print("=== AUTH SERVICE ===")
    auth = AuthContext(username=username, password=password)
    auth.request()  # login
    auth.request()  # onboarding
    print("\n=== DASHBOARD SERVICE ===")
    dashboard = DashboardContext(username=username)
    dashboard.request()  # view dashboard
    dashboard.set_state(dashboard.profile_state)
    dashboard.request()  # view profile
    dashboard.set_state(dashboard.settings_state)
    dashboard.request()  # update settings


    print("\n=== FRIENDS SERVICE ===")
    friends = FriendContext(username=username)
    friends.request()  # search friends
    friends.request()  # chat

    print("\n=== COMMUNITY SERVICE ===")
    community = CommunityContext(username=username)
    community.request()  # browse
    community.request()  # join

    print("\n=== ACTIVITIES SERVICE ===")
    activities = ActivityContext(username=username)
    activities.request()  # find activity
    activities.request()  # book activity


    print("\n=== NOTIFICATIONS SERVICE ===")
    notifications = NotificationContext(username=username)
    notifications.request()  # check notifications

if __name__ == "__main__":
    main()
