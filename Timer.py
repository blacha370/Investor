import datetime
import pytz


class Time:
    def __init__(self):
        self.timezone = pytz.timezone('US/Eastern')
        self.start_time = self.get_current_datetime()

    def get_current_datetime(self):
        return datetime.datetime.now(tz=self.timezone)

    def get_program_running_time(self):
        return self.get_current_datetime() - self.start_time

    @staticmethod
    def check_current_day(date):
        if datetime.datetime.weekday(date) < 5:
            return True
        else:
            return False

    @staticmethod
    def check_current_time(time):
        if datetime.time(hour=9, minute=30) < time < datetime.time(hour=16):
            return True
        else:
            return False

    def check_if_market_is_open(self):
        current_datetime = self.get_current_datetime()
        if Time.check_current_day(current_datetime) and Time.check_current_day(current_datetime.time()):
            return True
        else:
            return False
