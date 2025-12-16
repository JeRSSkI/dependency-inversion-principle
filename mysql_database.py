from database import Database

class MySQLDatabase(Database):
    def save(self, data):
        print("Saving data to MySQL database")
