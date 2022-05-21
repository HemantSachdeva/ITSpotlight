import requests
from flask import jsonify
from flask_restful import Resource

from api.methods import BASE_URL, get_story_ids, time_parser


class Items(Resource):
    def get(self, type, page):
        """
        Returns a list of news stories when given a page number (10 stories per page).
        :param page: Page number.
        :return: List of news stories.
        """
        news = []
        for id in get_story_ids(type, page):
            endpoint = f"/item/{id}.json"
            url = BASE_URL + endpoint
            response = requests.get(url)
            data = response.json()
            ret_json = {
                "id": data.get("id"),
                "time": time_parser(data.get("time")),
                "by": data.get("by"),
                "title": data.get("title"),
                "url": data.get("url") if data.get("url") else "",
                "sliced_url": data.get("url").split("/")[2] if data.get("url") else "",
                "likes": data.get("score"),
                "comments": data.get("descendants") if data.get("descendants") else 0
            }
            news.append(ret_json)
        return jsonify(news)
