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
