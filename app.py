from .WebScraper import WebScraper
from .MarketStock import MarketStock
import time


class App:
    def __init__(self, path, api_key):
        self.scraper = WebScraper(path)
        self.today_active_stocks = list()
        self.api_key = api_key
        self.get_today_active_stocks()

    def get_today_active_stocks(self):
        for symbol in self.scraper.get_most_active_stocks(5):
            self.today_active_stocks.append(MarketStock(symbol, self.api_key))
            time.sleep(15)
