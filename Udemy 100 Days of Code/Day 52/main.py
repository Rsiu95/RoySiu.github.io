from auto_filler import AutoFill
from web_scraper import HousePrices

def main():
    form = AutoFill()
    housing_info = HousePrices()
    prices = housing_info.get_house_prices()
    addresses = housing_info.get_address()
    links = housing_info.get_links()

    fill_info = list(zip(addresses, prices, links))
    print("listing found:", fill_info)
    form.fill_application(fill_info)
    print("Done")

if __name__ == "__main__":
    main()