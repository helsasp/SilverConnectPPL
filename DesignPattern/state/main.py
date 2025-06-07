from auth_service.context import AuthContext
from friends_service.context import FriendContext
from community_service.context import CommunityContext
from activities_service.context import ActivityContext
from dashboard_service.context import DashboardContext
from notifications_service.context import NotificationContext
from settings_service.context import SettingsContext

def main():
    print("=== Daftar Akun ===")
    new_user = AuthContext(
        username="elder1", 
        password="pass123", 
        email="elder1@example.com", 
        full_name="Elder One"
    )
    new_user.set_state(new_user.signup_state)
    new_user.request()

    print("\n=== Lupa Password ===")
    forgot_user = AuthContext(
        username="elder1",
        email="elder1@example.com"
    )
    forgot_user.set_state(forgot_user.forgot_password_state)
    forgot_user.request()

    print("\n=== Authorisasi ===")
    auth = AuthContext(
        username="elder1", 
        password="pass123", 
        email="elder1@example.com"
    )
    auth.request()  # login
    auth.request()  # onboarding

    print("\n=== Dashboard Pengguna ===")
    dashboard = DashboardContext(username=auth.username)
    dashboard.request()  # view dashboard
    dashboard.set_state(dashboard.profile_state)
    dashboard.request()
    dashboard.set_state(dashboard.settings_state)
    dashboard.request()

    print("\n=== Pengaturan ===")
    settings = SettingsContext(username=auth.username)
    settings.request()
    settings.set_state(settings.theme_state)
    settings.request()

    print("\n=== Teman ===")
    friends = FriendContext(username=auth.username)
    friends.request(interest_filter="Yoga")
    friends.request(friend_name="Diana")
    friends.request(interest_filter="Reading")
    friends.request(friend_name="Charlie")

    print("\n=== Komunitas ===")
    community = CommunityContext(username=auth.username)

    # Step 1: Browse communities
    community.set_state(community.browse_community_state)
    community.request()

    # Step 2: View details and join
    community.request()

    print("\n=== Aktivitas ===")
    activities = ActivityContext(username=auth.username)
    activities.set_state(activities.find_activity_state)
    activities.request()  # Browse activities
    activities.request()  # Show detail and booking

    print("\n=== Notifikasi ===")
    notifications = NotificationContext(username=auth.username)
    notifications.request()

if __name__ == "__main__":
    main()
