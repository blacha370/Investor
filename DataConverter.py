class DataConverter:
    @staticmethod
    def get_interval_data(data: list, interval: int) -> tuple:
        """Return tuple(first day open value, last day close value, interval change, daily average change)"""
        interval_data = data[:interval]
        interval_change = int()
        for day in interval_data:
            interval_change += day[2]
        average_change = round(interval_change / interval, 5)
        return interval_data[-1][0], interval_data[0][1], round(interval_change, 5), average_change
