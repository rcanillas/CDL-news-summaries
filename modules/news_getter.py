import requests
from dotenv import load_dotenv
import os

load_dotenv()
print(os.environ["NEWSDATA_KEY"])


class NewsGetter:

    def __init__(api_key):
        self.api_key = api_key
