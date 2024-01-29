from flask import Flask
from app.controller.carcontroller import car
from app.controller.usercontroller import user

def create_app():
    app = Flask(__name__)
    app.register_blueprint(car)
    app.register_blueprint(user)
    return app