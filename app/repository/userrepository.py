from pymongo import MongoClient
from bson import ObjectId

class UserRepository:
    def __init__(self, db_url, db_name):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.users_collection = self.db['users']
    
    def add_user(self, user_data):
        result = self.users_collection.insert_one(user_data)
        return str(result.inserted_id)
    
    def get_all_users(self):
        users = list(self.users_collection.find())
        return users
    
    def get_user_by_id(self, user_id):
        return self.users_collection.find_one({'_id': ObjectId(user_id)})
    
    def rent_car(self, user_id, car_id):
        result = self.users_collection.update_one(
            {'_id': ObjectId(user_id)},
            {'$addToSet': {'rented_cars': ObjectId(car_id)}}
        )
        return result.modified_count
    
    def return_car(self, car_id):
        result = self.users_collection.update_many(
            {'rented_cars': ObjectId(car_id)},
            {'$pull': {'rented_cars': ObjectId(car_id)}}
        )
        return result.modified_count