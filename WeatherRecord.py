from datetime import datetime

class WeatherRecord:

    def __init__(self, date, max_temperature, min_temperature, max_humidity, mean_humidity):

        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.max_temperature = self.assign_value(max_temperature)
        self.min_temperature = self.assign_value(min_temperature)
        self.max_humidity = self.assign_value(max_humidity)
        self.mean_humidity = self.assign_value(mean_humidity)

    def assign_value(self, string_value):
        if string_value:
            return int(string_value)
        else:
            return None
