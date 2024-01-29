from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime, timedelta

class CarRepository:
    def __init__(self, db_url, db_name):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.cars_collection = self.db['cars']
    
    def add_car(self, car_data):
        result = self.cars_collection.insert_one(car_data)
        return result.insert_id
    
    def get_all_cars(self):
        cars = list(self.cars_collection.find())
        return cars
    
    def get_car_by_id(self, car_id):
        return self.cars_collection.find_one({'_id': ObjectId(car_id)})
    
    def rent_car(self, car_id, user_id, rent_start_date, rent_end_date):
        result = self.cars_collection.update_one(
            {'_id': ObjectId(car_id)},
            {
                '$set': {
                    'available': False,
                    'renter': ObjectId(user_id),
                    'rent_start_date': datetime.fromisoformat(rent_start_date),
                    'rent_end_date': datetime.fromisoformat(rent_end_date)
                }
            }
        )
        return result.modified_count
    
    def return_car(self, car_id):
        car = self.cars_collection.find_one({'_id': ObjectId(car_id)})
        if car and not car['available']:
            result = self.cars_collection.update_one(
                {'_id': ObjectId(car_id)},
                {'$set': {
                    'available': True,
                    'renter': None,
                    'rent_start_date': None,
                    'rent_end_date': None
                }}
            )
            return result.modified_count
        return 0