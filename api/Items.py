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

from flask import jsonify
from flask_restful import Resource

from api.methods import get_story_ids, get_item, time_parser


class Items(Resource):
    def get(self, type, page):
        """
        Returns a list of news stories when given a page number (10 stories per page).
        :param page: Page number.
        :return: List of news stories.
        """
        news = []
        for id in get_story_ids(type, page):
            data = get_item(id)
            if data.get('url'):
                ret_json = {
                    "id": data.get("id"),
                    "time": time_parser(data.get("time")),
                    "by": data.get("by"),
                    "title": data.get("title"),
                    "url": data.get("url"),
                    "sliced_url": data.get("url").split("/")[2],
                    "likes": data.get("score")
                }
                news.append(ret_json)
        return jsonify(news)
