import requests


class RequestHandler:
    @staticmethod
    def send_request(symbol: str, api_key: str) -> list:
        """Return list of tuples, each tuple represents day and includes:
            -day open value
            -day close value
            -percentage day change"""
        r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + symbol
                         + '&&apikey=' + api_key)
        data = r.json()
        values = list()
        for day in list(data['Time Series (Daily)'].values())[0:30]:
            day_open = float(day['1. open'])
            day_close = float(day['4. close'])
            day_change = round(day_close / day_open, 5)
            values.append((day_open, day_close, day_change))
        return values
