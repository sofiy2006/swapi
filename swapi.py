import requests
from pathlib import Path


class APIRequester:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        try:
            url = f"{self.base_url}{endpoint}"
            return requests.get(url)
        except requests.exceptions.RequestException:
            print("Возникла ошибка при выполнении запроса")


class SWRequester(APIRequester):
    def get_sw_info(self, category):
        response = self.get(f"/{category}/")
        return response.text

    def get_sw_categories(self):
        response = self.get("/")
        data = response.json()
        return data.keys()


def save_sw_data():
    Path("data").mkdir(exist_ok=True)
    requester = SWRequester("https://swapi.dev/api")
    # requester = SWRequester("https://www.swapi.tech/api")
    categories = requester.get_sw_categories()
    for category in categories:
        data = requester.get_sw_info(category)
        with open(f"data/{category}.txt", "w", encoding="utf-8") as f:
            f.write(data)
