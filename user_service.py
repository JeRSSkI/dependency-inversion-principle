class UserService:
    def __init__(self, database):
        self.database = database

    def save_user(self, user):
        self.database.save(user)
