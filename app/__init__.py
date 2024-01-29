from flask import Flask
from app.controller.carcontroller import home

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home)
    return app