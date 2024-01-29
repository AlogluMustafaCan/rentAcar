from pymongo import MongoClient

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