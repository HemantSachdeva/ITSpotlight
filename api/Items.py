import requests
from flask import jsonify
from flask_restful import Resource

from api.methods import BASE_URL, get_story_ids


class Items(Resource):
    def get(self):
        """
        Returns a list of news stories.
        :return: List of news stories.
        """
        news = []
        for id in get_story_ids(1):
            endpoint = f"/item/{id}.json"
            url = BASE_URL + endpoint
            response = requests.get(url)
            data = response.json()
            ret_json = {
                "id": data.get("id"),
                "time": data.get("time"),
                "by": data.get("by"),
                "title": data.get("title"),
                "url": data.get("url"),
                "likes": data.get("score"),
                "comments": data.get("descendants")
            }
            news.append(ret_json)
        return jsonify(news)
