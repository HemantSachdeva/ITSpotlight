from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from api.Items import Items
from api.User import User

app = Flask(__name__)
api = Api(app)
CORS(app)


@app.route('/')
def index():
    return ""


api.add_resource(Items, "/items/page/<int:page>")
api.add_resource(User, "/user/<string:username>")
