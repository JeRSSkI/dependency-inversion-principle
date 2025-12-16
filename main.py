from user_service import UserService
from mysql_database import MySQLDatabase
from mongo_database import MongoDatabase

user = {"name": "Alex"}

mysql_service = UserService(MySQLDatabase())
mysql_service.save_user(user)

mongo_service = UserService(MongoDatabase())
mongo_service.save_user(user)
