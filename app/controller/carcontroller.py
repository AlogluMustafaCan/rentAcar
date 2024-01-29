from flask import Blueprint, jsonify, request
from ..repository.carrepository import CarRepository

home = Blueprint('home', __name__)

car_repository = CarRepository("mongodb://localhost:27017/","rentacar")

@home.route('/', methods=['GET'])
def get_all_cars():
    cars = car_repository.get_all_cars()

    formatted_cars = []
    for car in cars:
        formatted_car = {
            "make": car["make"],
            "model": car["model"],
            "year": car["year"],
            "renter": car["renter"],
            "rent_start_date": car["rent_start_date"],
            "rent_end_date": car["rent_end_date"]
        }
        formatted_cars.append(formatted_car)
    return jsonify(formatted_cars)
