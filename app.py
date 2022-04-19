from flask import Flask
from flask_restful import Api

from api.Items import Items

app = Flask(__name__)
api = Api(app)


api.add_resource(Items, "/items")
