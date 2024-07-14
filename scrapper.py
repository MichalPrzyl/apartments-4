import json

import requests
from bs4 import BeautifulSoup

from colors import ENDC, FAIL, HEADER, OKBLUE, OKCYAN, OKGREEN, WARNING


class Scrapper:
    def __init__(self, urls) -> None:
        self.urls = urls

        # Here are the results. We need to reset those after each scrap.
        self.results = None

    def scrap_all_urls(self):
        self.results = []

        for url in self.urls:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            ad_price_container = soup.find("div", {"data-testid": "ad-price-container"})

            # Literal price
            if ad_price_container:
                price_text = ad_price_container.find("h3").get_text(strip=True)
                price = "".join(filter(str.isdigit, price_text))

                self.results.append({
                    "link": url,
                    "price": price
                })
            else:
                self.results.append({
                    "link": url,
                    "price": "Not found data..."
                })


    def save_results_to_json_file(self):
        if not self.results:
            raise ValueError("There are no results. First use scrapping function!")

        with open("results.json", 'w') as file:
            print(f"self.results: {self.results}")
            file.write(json.dumps(self.results))
