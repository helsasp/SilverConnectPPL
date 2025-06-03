from auth_service.context import AuthContext
from friends_service.context import FriendContext
from community_service.context import CommunityContext
from activities_service.context import ActivityContext
from dashboard_service.context import DashboardContext
from notifications_service.context import NotificationContext

def main():
    print("=== SIGNUP ===")
    new_user = AuthContext(
        username="elder1", 
        password="pass123", 
        email="elder1@example.com", 
        full_name="Elder One"
    )
    new_user.set_state(new_user.signup_state)
    new_user.request()  # signup

    print("\n=== FORGOT PASSWORD ===")
    forgot_user = AuthContext(
        username="elder1",
        email="elder1@example.com"
    )
    forgot_user.set_state(forgot_user.forgot_password_state)
    forgot_user.request()  # forgot password

    print("\n=== AUTH SERVICE ===")
    auth = AuthContext(
        username="elder1", 
        password="pass123", 
        email="elder1@example.com"
    )
    auth.request()  # login
    auth.request()  # onboarding

    print("\n=== DASHBOARD SERVICE ===")
    dashboard = DashboardContext(username=auth.username)
    dashboard.request()  # view dashboard
    dashboard.set_state(dashboard.profile_state)
    dashboard.request()  # view profile
    dashboard.set_state(dashboard.settings_state)
    dashboard.request()  # update settings

    print("\n=== FRIENDS SERVICE ===")
    friends = FriendContext(username=auth.username)
    friends.request()  # search friends
    friends.request()  # chat

    print("\n=== COMMUNITY SERVICE ===")
    community = CommunityContext(username=auth.username)
    community.request()  # browse
    community.request()  # join

    print("\n=== ACTIVITIES SERVICE ===")
    activities = ActivityContext(username=auth.username)
    activities.request()  # find activity
    activities.request()  # book activity

    print("\n=== NOTIFICATIONS SERVICE ===")
    notifications = NotificationContext(username=auth.username)
    notifications.request()  # check notifications

if __name__ == "__main__":
    main()
