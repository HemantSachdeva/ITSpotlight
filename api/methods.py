import requests

BASE_URL = "https://hacker-news.firebaseio.com/v0"


def get_story_ids():
    """
    Returns a list of latest 500 story ids.
    :return: List of latest 500 story ids.
    """
    # Get list of ids for the latest news stories.
    endpoint = f"/newstories.json"
    url = BASE_URL + endpoint
    response = requests.get(url)
    data = response.json()
    return data
