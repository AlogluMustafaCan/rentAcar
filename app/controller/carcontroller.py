from flask import Blueprint, jsonify, request
from app.repository.carrepository import CarRepository
from app.repository.userrepository import UserRepository
#from datetime import datetime, timedelta

car = Blueprint('car', __name__)

car_repository = CarRepository("mongodb://localhost:27017/","rentacar")
user_repository = UserRepository("mongodb://localhost:27017/","rentacar")

@car.route('/cars', methods=['GET'])
def get_all_cars():
    cars = car_repository.get_all_cars()

    formatted_cars = []
    for car in cars:
        formatted_car = {
            "make": car["make"],
            "model": car["model"],
            "year": car["year"],
            #"renter": car["renter"],
            "rent_start_date": car["rent_start_date"],
            "rent_end_date": car["rent_end_date"]
        }
        formatted_cars.append(formatted_car)
    return jsonify(formatted_cars)

@car.route('/cars/rent', methods=['POST'])
def rent_car():
    data = request.json
    user_id = data.get('user_id')
    car_id = data.get('car_id')
    rent_start_date = data.get('rent_start_date')
    rent_end_date = data.get('rent_end_date')

    if not user_id or not car_id:
        return jsonify({"error":"User ID and Car ID are required"}), 400
    
    user = user_repository.get_user_by_id(user_id)
    if not user:
        return jsonify({"error":"User not found"}),404
    
    car = car_repository.get_car_by_id(car_id)
    if not car['available']:
        return jsonify({"error":"Car is not available for rent"}),400
    car_repository.rent_car(car_id, user_id, rent_start_date, rent_end_date)
    user_repository.rent_car(user_id, car_id)

    return jsonify({"message":"Car rented successfully"})

@car.route('/cars/return', methods=['POST'])
def return_car():
    data = request.json
    car_id = data.get('car_id')

    if not car_id:
        return jsonify({"error": "Car ID is required"}), 400

    # Return the car in both repositories
    car_repository.return_car(car_id)
    user_repository.return_car(car_id)

    return jsonify({"message": "Car returned successfully"})

