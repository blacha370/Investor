class DataConverter:
    @staticmethod
    def get_interval_data(data: list, interval: int) -> tuple:
        """Return tuple(first day open value, last day close value, percentage interval change)"""
        interval_data = data[:interval]
        interval_change = interval_data[0][1] / interval_data[-1][0]
        return interval_data[-1][0], interval_data[0][1], interval_change
