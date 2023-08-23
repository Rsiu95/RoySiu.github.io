from bs4 import BeautifulSoup
import requests, re

URL = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.63417281103516%2C%22east%22%3A-122.23248518896484%2C%22south%22%3A37.66177225771613%2C%22north%22%3A37.888636610997644%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
    "Accept-Language": "en-US"
}

#API_KEY = os.getenv("API_KEY")

response = requests.get(URL, headers = headers)

class HousePrices:
    def __init__(self):
        self.info = response.text
        self.soup = BeautifulSoup(self.info, 'html.parser')
        self.house_prices = self.soup.find_all(name = "div", class_="StyledCard-c11n-8-84-3__sc-rmiu6p-0")
        
    def get_house_prices(self):
        prices = []
        for price in self.house_prices:
            pattern = r"\$(\d{1,3}(?:,\d{3})*)(?=\+)"
            values = re.findall(pattern, price.getText())
            numeric_values = [int(num.replace(",","")) for num in values]
            prices.append(min(numeric_values))
        return prices

    def get_links(self):
        links = []
        for link in self.house_prices:
            try:
                target_url = link.find("a").get("href")
                if "zillow" not in target_url:
                    full_url = "https://www.zillow.com" + target_url
                    links.append(full_url)
                else:
                    links.append(target_url)
            except: 
                pass
        return links

    def get_address(self):
        addresses = []
        for address in self.house_prices:
            if len(address.getText()) == 11:
                continue
            else:
                addresses.append(",".join(address.getText().split(",", 2)[:2]))  
        return addresses
        

