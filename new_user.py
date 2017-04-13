from common.database import Database

Database.initialize()
Database.insert('users', {"account": "lostshin@gmail.com", "password": "123456", "name": "lostshin"})
user = Database.find_one('users', {"account": "lostshin@gmail.com"})
print(user)
