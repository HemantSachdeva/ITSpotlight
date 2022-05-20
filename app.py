from flask import Flask, render_template
from flask_cors import CORS
from flask_restful import Api
import requests

from api.Items import Items
from api.User import User

app = Flask(__name__)
api = Api(app)
CORS(app)


@app.route('/')
@app.route('/index')
def index():
    resp = requests.get('http://127.0.0.1:5000/api/items/page/1')
    latest_news = resp.json()
    context = {
        "latest_news": latest_news
    }
    return render_template('index.html', context=context)


api.add_resource(Items, "/api/items/page/<int:page>")
api.add_resource(User, "/api/user/<string:username>")
