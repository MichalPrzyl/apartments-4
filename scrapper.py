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
            # surface_container = soup.find('li', {'class': 'css-1r0s1ie'})
            surface_container = soup.find('li', {'class': 'css-1r0si1e'})

            # Initial values for each iteration
            surface_value = "No data..."
            price = "No data..."

            # Literal surface
            # TODO: That doesn't work
            if surface_container:
                surface_text = surface_container.find('p', {'class': 'css-b5m1rv'}).get_text(strip=True)
                surface_value = ''.join(filter(str.isdigit, surface_text))
                # print(f"surface_value: surface_value")
                # print(f"Wartość powierzchni: {surface_value} m²")

            # Literal price
            if ad_price_container:
                price_text = ad_price_container.find("h3").get_text(strip=True)
                price = "".join(filter(str.isdigit, price_text))

            self.results.append({
                "link": url,
                "price": price if price else "No data...",
                "surface": surface_value if surface_value else "No data..."
            })
            
    def save_results_to_json_file(self):
        if not self.results:
            raise ValueError("There are no results. First use scrapping function!")

        with open("results.json", 'w') as file:
            file.write(json.dumps(self.results, indent=4))
