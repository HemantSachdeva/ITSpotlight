from flask import Flask
from flask_restful import Api

from api.Items import Items
from api.User import User

app = Flask(__name__)
api = Api(app)


api.add_resource(Items, "/items")
api.add_resource(User, "/user/<string:username>")
