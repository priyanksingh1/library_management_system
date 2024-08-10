from src.models import User

class UserManager:
    def __init__(self):
        self.users = {}  # This will store users keyed by their email

    def register_user(self, name, email, password, role="user"):
        if email in self.users:
            raise ValueError("Email already registered.")
        user = User(name, email, password, role)
        self.users[email] = user
        return user

    def authenticate_user(self, email, password):
        user = self.users.get(email)
        if not user or not user.check_password(password):
            raise ValueError("Invalid email or password.")
        return user

