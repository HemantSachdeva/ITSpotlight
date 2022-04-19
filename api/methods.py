import requests

BASE_URL = "https://hacker-news.firebaseio.com/v0"


def get_story_ids(page):
    """
    Returns a list of 10 story ids per page.
    :return: List of 10 story ids per page.
    """
    # Get list of ids for the latest news stories.
    endpoint = f"/newstories.json"
    url = BASE_URL + endpoint
    response = requests.get(url)
    data = response.json()
    stories_per_page = 10
    start_index = (page - 1) * stories_per_page
    end_index = start_index + stories_per_page
    return data[start_index:end_index]
