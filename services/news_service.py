import requests
from config import Config

def get_top_headlines(country="us", category=None, page=1, page_size=12):
    url = f"{Config.BASE_URL}/top-headlines"

    params = {
        "apiKey": Config.NEWS_API_KEY,
        "country": country,
        "page": page,
        "pageSize": page_size
    }

    if category:
        params["category"] = category

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return [], 0

    data = response.json()
    return data.get("articles", []), data.get("totalResults", 0)


def search_news(query, page=1, page_size=12):
    url = f"{Config.BASE_URL}/everything"

    params = {
        "apiKey": Config.NEWS_API_KEY,
        "q": query,
        "page": page,
        "pageSize": page_size,
        "sortBy": "publishedAt"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return [], 0

    data = response.json()
    return data.get("articles", []), data.get("totalResults", 0)
