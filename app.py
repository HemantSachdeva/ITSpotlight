"""
 Copyright (C) 2022 Hemant Sachdeva <hemant.evolver@gmail.com>

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU Affero General Public License as
 published by the Free Software Foundation, either version 3 of the
 License, or (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU Affero General Public License for more details.

 You should have received a copy of the GNU Affero General Public License
 along with this program.  If not, see <https://www.gnu.org/licenses/>.
 """

from flask import Flask, render_template
from flask_restful import Api
import requests

from api.Items import Items
from api.User import User

app = Flask(__name__)
api = Api(app)


@app.route('/')
@app.route('/index')
@app.route('/<string:type>')
@app.route('/<string:type>/<int:page>')
def index(type="newstories", page=1):

    ALLOWED_TYPES = ["newstories", "topstories", "jobstories"]

    if type not in ALLOWED_TYPES:
        type = "newstories"

    if page < 1 or page > 100:
        page = 1

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
        "title": title,
        "type": type,
        "page": page
    }
    return render_template('index.html', context=context)


@app.route('/user/<string:username>')
def user_profile(username):
    resp = requests.get(f"http://itspotlight.herokuapp.com/api/user/{username}")
    user = resp.json()
    return render_template('user.html', context=user)


api.add_resource(Items, "/api/items/<string:type>/page/<int:page>")
api.add_resource(User, "/api/user/<string:username>")
