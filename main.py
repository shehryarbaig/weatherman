import os
import argparse
from WeatherDataParser import WeatherDataParser
from WeatherDataCalculator import WeatherDataCalculator
from WeatherReport import WeatherReport

def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("dir", help="Directory which contains Weather Files.", nargs='?')
    arg_parser.add_argument("-e", help="For a given year display the highest temperature and day, lowest temperature and day, most humid day and humidity.")
    arg_parser.add_argument("-a", help="For a given month display the average highest temperature, average lowest temperature, average mean humidity.")
    arg_parser.add_argument("-c", help="For a given month draw two horizontal bar charts on the console for the highest and lowest temperature on each day. Highest in red and lowest in blue.")
    args = arg_parser.parse_args()
   
    if args.dir and os.path.exists(args.dir):
        murree_weather_data = {}
        weather_data_parser = WeatherDataParser(murree_weather_data, args.dir)
        weather_data_parser.parse_data()
        weather_data_calculations = {}
        weather_data_calculator = WeatherDataCalculator(weather_data_calculations, murree_weather_data)

        if args.e:
            weather_data_calculator.calculate_year_results(int(args.e))
            report = WeatherReport(weather_data_calculations)
            report.generate_years_report(int(args.e))
            print("--------------------------------------")

        if args.a:
            year = int(args.a.split("/")[0])
            month = int(args.a.split("/")[1])
            weather_data_calculator.calculate_avg_month_results(year, month)
            report = WeatherReport(weather_data_calculations)
            report.generate_avg_temp_report(year, month)
            print("--------------------------------------")

        if args.c:
            year = int(args.c.split("/")[0])
            month = int(args.c.split("/")[1])
            report = WeatherReport()
            report.draw_bars(murree_weather_data, year, month)
        
    else:
        print("Directory Not Found.")

 

main()