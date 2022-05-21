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

import requests
from flask import jsonify
from flask_restful import Resource

from api.methods import BASE_URL, time_parser


class User(Resource):
    def get(self, username):
        """
        Returns user info.
        :param username: Username of user.
        :return: User info.
        """
        endpoint = f"/user/{username}.json"
        url = BASE_URL + endpoint
        response = requests.get(url)
        data = response.json()
        ret_json = {
            "about": data.get("about") if data.get("about") else "No about info.",
            "account_created": time_parser(data.get("created")),
            "karma": data.get("karma"),
            "post_ids": data.get("submitted") if data.get("submitted") else 0,
            "total_posts": len(data.get("submitted")) if data.get("submitted") else 0,
            "username": data.get("id")
        }
        return jsonify(ret_json)
