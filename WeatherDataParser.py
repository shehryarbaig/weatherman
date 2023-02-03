import glob
import os
from datetime import datetime
from WeatherRecord import WeatherRecord
import csv


class WeatherDataParser:

    def __init__(self, path) -> None:
        self.weather_records = []
        self.path = path

    def get_files(self):
        os.chdir(r'%s' % self.path)
        return glob.glob('*.txt')

    def parse_weather_data(self):
        weather_data_files = self.get_files()
        for filename in weather_data_files:
            with open(os.path.join(os.getcwd(), filename), 'r') as file_data:
                reader = csv.DictReader(file_data)
                for row in reader:
                    self.weather_records.append(WeatherRecord(
                        row["PKT"],
                        row["Max TemperatureC"],
                        row["Min TemperatureC"],
                        row["Max Humidity"],
                        row[" Mean Humidity"]))

    def get_filtered_data(self, year):
        return [record for record in self.weather_records if record.date.year == year]

    def get_filtered_data(self, year, month=None):
        if month == None:
            return [record for record in self.weather_records if record.date.year == year]
        
        return [record for record in self.weather_records if record.date.year == year and 
        record.date.month == month]
