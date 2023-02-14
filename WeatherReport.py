import calendar

from termcolor import colored


class WeatherReport:

    def generate_year_report(self, year, records):
        if len(records) == 0:
            print("{} data is not available.".format(year))
            return

        print("{}".format(records[0].date.year))
        print(
            f"Highest: {records[0].max_temperature}C on {calendar.month_name[records[0].date.month]} {records[0].date.day}")

        print(
            f"Lowest: {records[1].min_temperature}C on {calendar.month_name[records[1].date.month]} {records[1].date.day}")

        print(
            f"Humidity: {records[2].max_humidity}C on {calendar.month_name[records[2].date.month]} {records[2].date.day}")
        print("--------------------------------------")

    def generate_avg_temp_report(self, averages, year, month):
        if len(averages) == 0:
            print("{} data is not available.".format(year))
            return

        print("{} {}".format(calendar.month_name[month], year))
        print(f"Highes Average: {averages[0]}C")

        print(f"Lowest Average: {averages[1]}C")

        print(f"Average Mean Humidity: {averages[2]}C")
        print("--------------------------------------")

    def draw_bars(self, month_weather_data, year, month):
        if len(month_weather_data) != 0:
            print("{} {}".format(calendar.month_name[month], year))

            for record in month_weather_data:
                print(
                    f"{record.date.day} {colored('+' * (record.min_temperature or 0), 'blue')}{colored('+' * (record.max_temperature or 0), 'red')} {(record.min_temperature or 0)}C - {(record.max_temperature or 0)}C")
