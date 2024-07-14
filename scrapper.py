from colors import OKGREEN, ENDC, WARNING, OKCYAN,\
    FAIL, OKBLUE, HEADER
import requests
from bs4 import BeautifulSoup

URLS = [
    "https://www.olx.pl/d/oferta/na-sprzedaz-2-pokojowe-mieszkanie-ul-borkowska-kliny-CID3-IDNP9Nq.html?isPreviewActive=0&sliderIndex=0",
    "https://www.otodom.pl/pl/oferta/2-pokoje-os-stalowe-45m2-ID4quTP.html?_gl=1*5yer2a*_gcl_aw*R0NMLjE3MjA5ODI5OTMuQ2p3S0NBanc3czIwQmhCRkVpd0FCVklNclYtNVlDclZzSDdCU0g5bDlMaFNseEhxdkhDLU1kaTBrdTlWcnozT1MySlFObkFMTy1NWWl4b0NnazRRQXZEX0J3RQ..*_gcl_au*NDY2NzA1Mzk4LjE3MTQ0MjQyNDY.*_ga*MTA0MzQ4NDQxMi4xNzE0NDI0MjQ2*_ga_6PZTQNYS5C*MTcyMDk4Mjk4OS44LjEuMTcyMDk4Mjk5Mi41Ny4wLjA.&_ga=2.263538572.1480870937.1720982989-1043484412.1714424246&_gac=1.149630404.1720982992.CjwKCAjw7s20BhBFEiwABVIMrV-5YCrVsH7BSH9l9LhSlxHqvHC-Mdi0ku9Vrz3OS2JQNnALO-MYixoCgk4QAvD_BwE",
    "https://www.olx.pl/d/oferta/mieszkanie-apartament-prywatnie-park-lotnikow-grzegorzki-tauron-arena-CID3-IDZFoDG.html",
    "https://www.olx.pl/d/oferta/3-pokoje-73-m2-z-tarasem-ul-masarska-od-zaraz-CID3-ID10WZyE.html"
]

for url in URLS:
    print(f"Getting data from url:\n{url}")
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    ad_price_container = soup.find('div', {'data-testid': 'ad-price-container'})

    # Wyciągnięcie wartości liczbowej ceny
    if ad_price_container:
        price_text = ad_price_container.find('h3').get_text(strip=True)
        results = ''.join(filter(str.isdigit, price_text))

        print(f"{HEADER}results: {results}{ENDC}")
    else:
        print(f"{FAIL}No price found{ENDC}")

    print(50*'-')


