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

from datetime import datetime

import requests

BASE_URL = "https://hacker-news.firebaseio.com/v0"


def get_story_ids(type, page):
    """
    Returns a list of 10 story ids per page.
    :return: List of 10 story ids per page.
    """
    # Get list of ids for the latest news stories.
    endpoint = f"/{type}.json"
    url = BASE_URL + endpoint
    response = requests.get(url)
    data = response.json()
    stories_per_page = 10
    start_index = (page - 1) * stories_per_page
    end_index = start_index + stories_per_page
    return data[start_index:end_index]


def time_parser(unix_time):
    """
    Compares the current time to the time of the last update.
    :param unix_time: Unix time of the last update.
    :return: String of the time difference.
    """
    just_now = int(datetime.now().strftime('%s'))
    time_diff = just_now - unix_time
    if time_diff < 60:
        return 'Just now'
    elif time_diff < 3600:
        return '{} minutes ago'.format(int(time_diff / 60))
    elif time_diff < 86400:
        return '{} hours ago'.format(int(time_diff / 3600))
    elif time_diff < 604800:
        return '{} days ago'.format(int(time_diff / 86400))
    elif time_diff < 2592000:
        return '{} weeks ago'.format(int(time_diff / 604800))
    elif time_diff < 31536000:
        return '{} months ago'.format(int(time_diff / 2592000))
    else:
        return '{} years ago'.format(int(time_diff / 31536000))
