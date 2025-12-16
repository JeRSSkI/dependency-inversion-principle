from database import Database

class MongoDatabase(Database):
    def save(self, data):
        print("Saving data to MongoDB database")
