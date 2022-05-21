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
@app.route('/<string:type>')
@app.route('/<string:type>/<int:page>')
def index(type="newstories", page=1):

    ALLOWED_TYPES = ["newstories", "topstories", "jobstories"]

    if type not in ALLOWED_TYPES:
        type = "newstories"

    resp = requests.get(f"http://itspotlight.herokuapp.com/api/items/{type}/page/{page}")
    news = resp.json()
    
    if type == "newstories":
        title = "Latest News"
    elif type == "topstories":
        title = "Trending News"
    elif type == "jobstories":
        title = "See who is hiring"

    context = {
        "news": news,
        "title": title
    }
    return render_template('index.html', context=context)


api.add_resource(Items, "/api/items/<string:type>/page/<int:page>")
api.add_resource(User, "/api/user/<string:username>")
