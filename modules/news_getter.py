import requests
import os

from dotenv import load_dotenv
from pprint import pprint

load_dotenv()


class NewsGetter:

    def __init__(self):
        self.api_key = os.environ["NEWSDATA_KEY"]
        self.url = f"https://newsdata.io/api/1/latest"

    def get_tech_articles(self):
        headers = {"X-ACCESS-KEY": self.api_key}
        params = {"category": "technology", "language": "fr,en", "size": 10}
        tech_articles = requests.get(self.url, headers=headers, params=params).json()
        pprint(tech_articles)
        return tech_articles


if __name__ == "__main__":
    newsGetter = NewsGetter()
    tech_articles = newsGetter.get_tech_articles()
