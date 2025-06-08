from auth_service.context import AuthContext
from friends_service.context import FriendContext
from community_service.context import CommunityContext
from activities_service.context import ActivityContext
from dashboard_service.context import DashboardContext
from notifications_service.context import NotificationContext
from settings_service.context import SettingsContext
from chat_service.context import ChatContext


def main():
    print("===========================================")
    print(" Silver Connect - Your Companion Through")
    print("               The Golden Years")
    print("===========================================\n")

    print("=== Daftar Akun ===")
    new_user = AuthContext(
        username="elder1",
        password="pass123",
        confirm_password="pass123",
        email="elder1@example.com",
        full_name="Elder One"
    )
    new_user.set_state(new_user.signup_state)
    new_user.request()

    new_user.mode = "cinta"
    new_user.hobbies = ["Membaca", "Berkebun", "Yoga"]
    new_user.story = "Saya suka menjelajahi tempat baru dan mencari cinta sejati."

    new_user.set_state(new_user.profile_setup_state)
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
    auth.set_state(auth.login_state)
    auth.request()
    auth.set_state(auth.onboarding_state)
    auth.request()

    print("\n=== Dashboard Pengguna ===")
    dashboard = DashboardContext(username=auth.username)
    dashboard.request()
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
    friends.request(friend_name="Diana", action="add")
    friends.request(friend_name="Diana", action="like")
    friends.request(friend_name="Diana", action="chat")

    friends.request(interest_filter="Gaming")
    friends.request(friend_name="Charlie", action="like")


    print("\n=== Chat ===")
    chat = ChatContext(username=auth.username)
    chat.request(friend_name="Diana")
    chat.request(message="Hai Diana, bagaimana kabarmu hari ini?")

    print("\n=== Komunitas ===")
    community = CommunityContext(username=auth.username)
    community.set_state(community.browse_community_state)
    community.request()
    community.request()

    print("\n=== Aktivitas ===")
    activities = ActivityContext(username=auth.username)
    activities.set_state(activities.find_activity_state)
    activities.request()
    activities.request()

    print("\n=== Notifikasi ===")
    notifications = NotificationContext(username=auth.username)
    notifications.request()

if __name__ == "__main__":
    main()
