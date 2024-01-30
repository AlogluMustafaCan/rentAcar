from flask import Blueprint, jsonify, request
from ..repository.userrepository import UserRepository

user = Blueprint('user', __name__)

user_repository = UserRepository("mongodb://172.17.241.66:27017/","rentacar")

@user.route('/users', methods=['GET'])
def get_all_users():
    users = user_repository.get_all_users()

    formatted_users = []
    for user in users:
        formatted_user = {
            "username": user["username"],
            "surname": user["surname"],
            "email": user["email"],
            "password": user["password"],
            #"rented_cars": user["rented_cars"],
        }
        formatted_users.append(formatted_user)
    return jsonify(formatted_users)