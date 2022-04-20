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
