import argparse
import os

from WeatherDataCalculator import WeatherDataCalculator
from WeatherDataParser import WeatherDataParser
from WeatherReport import WeatherReport


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "dir",
        help="Directory which contains Weather Files.", nargs='?')
    arg_parser.add_argument(
        "-e",
        help="For a given year display the highest temperature and day, lowest temperature and day, most humid day and humidity.")
    arg_parser.add_argument(
        "-a",
        help="For a given month display the average highest temperature, average lowest temperature, average mean humidity.")
    arg_parser.add_argument(
        "-c",
        help="For a given month draw two horizontal bar charts on the console for the highest and lowest temperature on each day. Highest in red and lowest in blue.")
    args = arg_parser.parse_args()

    if not args.dir or not os.path.exists(args.dir):
        print("Directory Not Found.")
        return

    weather_data_parser = WeatherDataParser(args.dir)
    weather_data_parser.parse_weather_data()
    weather_data_calculator = WeatherDataCalculator()

    if args.e:
        year_weather_data = weather_data_parser.get_filtered_data(int(args.e))
        records = weather_data_calculator.calculate_year_temperatures(year_weather_data)
        report = WeatherReport()
        report.generate_year_report(args.e, records)

    if args.a:
        year, month = [int(a) for a in args.a.split("/")]
        month_weather_data = weather_data_parser.get_filtered_data(year, month)
        averages = weather_data_calculator.calculate_avg_month_results(month_weather_data)
        report = WeatherReport()
        report.generate_avg_temp_report(averages, year, month)

    if args.c:
        year, month = [int(a) for a in args.c.split("/")]
        month_weather_data = weather_data_parser.get_filtered_data(year, month)
        report = WeatherReport()
        report.draw_bars(month_weather_data, year, month)

if __name__ == "__main__":
    main()
