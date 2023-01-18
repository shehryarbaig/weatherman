import glob
import os
from datetime import datetime


class WeatherDataParser:
    def __init__(self, weather_data, path) -> None:
        self.weather_data = weather_data
        self.path = path

    def parse_data(self):
        weather_data_files = self.get_files()
        for filename in weather_data_files:
            with open(os.path.join(os.getcwd(), filename), 'r') as file_data:
                weather_headings = []
                weather_readings = []

                for i, line in enumerate(file_data):
                    if (i == 0):
                        weather_headings = [heading.strip()
                                            for heading in line.split(",")]
                    else:
                        weather_readings = [value.strip()
                                            for value in line.split(",")]
                        date_str = weather_readings[0]
                        date_object = datetime.strptime(date_str, "%Y-%m-%d")
                        year = date_object.year
                        month = date_object.month
                        day = date_object.day

                        if not year in self.weather_data:
                            self.weather_data[year] = {}

                        if not month in self.weather_data[year]:
                            self.weather_data[year][month] = {}

                        if not day in self.weather_data[year][month]:
                            self.weather_data[year][month][day] = {}

                        for j, reading in enumerate(weather_readings):
                            self.weather_data[year][month][day][weather_headings[j]] = reading

    def get_files(self):
        os.chdir(r'%s' % self.path)
        my_files = glob.glob('*.txt')
        return my_files
