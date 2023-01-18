import calendar
from termcolor import colored


class WeatherReport:
    def __init__(self, weather_data_calculations={}):
        self.weather_data_calculations = weather_data_calculations
        pass

    def generate_years_report(self, year):
        if year in self.weather_data_calculations.keys():
            print("{}".format(year))
            print("Highest: {}C on {} {}".format(
                self.weather_data_calculations[year]["max_temp"],
                calendar.month_name[self.weather_data_calculations[year]
                                    ["max_month"]],
                self.weather_data_calculations[year]["max_day"]))

            print("Lowest: {}C on {} {}".format(
                self.weather_data_calculations[year]["min_temp"],
                calendar.month_name[self.weather_data_calculations[year]
                                    ["min_month"]],
                self.weather_data_calculations[year]["min_day"]))

            print("Humidity: {}C on {} {}".format(
                self.weather_data_calculations[year]["max_humidity"],
                calendar.month_name[self.weather_data_calculations[year]
                                    ["max_humidity_month"]],
                self.weather_data_calculations[year]["max_humidity_day"]))

        else:
            print("{} data is not available.".format(year))

    def generate_avg_temp_report(self, year, month):
        if year in self.weather_data_calculations.keys():
            print("{} {}".format(calendar.month_name[month], year))
            print("Highes Average: {}C".format(
                self.weather_data_calculations[year][month]["avg_highest_temp"]))

            print("Lowest Average: {}C".format(
                self.weather_data_calculations[year][month]["avg_lowest_temp"]))

            print("Average Mean Humidity: {}C".format(
                self.weather_data_calculations[year][month]["avg_mean_humidity"]))
        else:
            print("{} data is not available.".format(year))

    def draw_bars(self, weather_data, year, month):
        if year in weather_data.keys() and month in weather_data[year].keys():
            print("{} {}".format(calendar.month_name[month], year))
            for day in weather_data[year][month]:
                highest_temp_sign = ""
                lowest_temp_sign = ""
                max_temp = int(
                    weather_data[year][month][day]["Max TemperatureC"] or 0)
                min_temp = int(
                    weather_data[year][month][day]["Min TemperatureC"] or 0)
                for i in range(max_temp):
                    highest_temp_sign = highest_temp_sign + "+"

                for i in range(min_temp):
                    lowest_temp_sign = lowest_temp_sign + "+"

                # print("{} {}C".format(colored(highest_temp_sign, 'red'), max_temp))
                # print("{} {}C".format(colored(lowest_temp_sign, 'blue'), min_temp))
                print("{} {}{} {}C - {}C".format(day, colored(lowest_temp_sign, 'blue'), colored(highest_temp_sign, 'red'),
                                                 min_temp, max_temp))
