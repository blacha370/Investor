from .RequestHandler import RequestHandler
from .DataConverter import DataConverter


class MarketStock:
    def __init__(self, symbol: str, api_key: str):
        self.stock_data = RequestHandler.send_request(symbol, api_key)
        self.last_month_data = DataConverter.get_interval_data(self.stock_data, 28)
        self.last_week_data = DataConverter.get_interval_data(self.stock_data, 7)
        self.trend_change = self.get_trend_change()

    def get_trend_change(self) -> float:
        """Return last week percentage change compared to last month percentage change"""
        return self.last_week_data[2] / self.last_month_data[2]
