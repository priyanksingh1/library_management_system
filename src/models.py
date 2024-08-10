class User:
    def __init__(self, name, email, password, role="user"):
        self.name = name
        self.email = email
        self.password = password  # In real applications, never store plain text passwords!
        self.role = role

    def check_password(self, password):
        return self.password == password
