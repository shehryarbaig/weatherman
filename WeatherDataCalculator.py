

class WeatherDataCalculator:
    def __init__(self, weather_data_calculations, weather_data):
        self.weather_data_calculations = weather_data_calculations
        self.weather_data = weather_data

    def calculate_year_results(self, year):
        if year in self.weather_data.keys():
            max_temp, max_month, max_day, min_temp, min_month, min_day, max_humidity, max_humidity_month, max_humidity_day = \
            self.calculate_temperatures(year)
            self.weather_data_calculations[year] = {
                "max_temp" : max_temp, 
                "max_month": max_month, 
                "max_day": max_day, 
                "min_temp": min_temp, 
                "min_month": min_month, 
                "min_day": min_day,
                "max_humidity": max_humidity,
                "max_humidity_month": max_humidity_month,
                "max_humidity_day": max_humidity_day
                }
            

    def calculate_temperatures(self, year):
        max_temp = int(list(list(self.weather_data[year].items())[0][1].items())[0][1]["Max TemperatureC"])
        max_month = list(self.weather_data[year].keys())[0]
        max_day = list(list(self.weather_data[year].items())[0][1].keys())[0]
        min_temp = int(list(list(self.weather_data[year].items())[0][1].items())[0][1]["Min TemperatureC"])
        min_month = max_month
        min_day = max_day
        max_humidity = int(list(list(self.weather_data[year].items())[0][1].items())[0][1]["Max Humidity"])
        max_humidity_month = max_month
        max_humidity_day = max_day

        for month in self.weather_data[year]:
            for day in self.weather_data[year][month]:
                max_temperature = self.weather_data[year][month][day]["Max TemperatureC"]
                if not max_temperature == "" and int(max_temperature) > max_temp:
                    max_temp = int(max_temperature)
                    max_month = month
                    max_day = day
                
                min_temperature = self.weather_data[year][month][day]["Min TemperatureC"]
                if not min_temperature == "" and int(min_temperature) < min_temp:
                    min_temp = int(min_temperature)
                    min_month = month
                    min_day = day

                humidity = self.weather_data[year][month][day]["Max Humidity"]
                if not humidity == "" and int(humidity) > max_humidity:
                    max_humidity = int(humidity)
                    max_humidity_month = month
                    max_humidity_day = day

        return (max_temp, max_month, max_day, min_temp, min_month, min_day, max_humidity, max_humidity_month, max_humidity_day)

    def calculate_avg_month_results(self, year, month):
        if year in self.weather_data.keys():
            total_highest = 0
            total_lowest = 0
            total_mean_humidity = 0
            total_days = len(self.weather_data[year][month])

            for day in self.weather_data[year][month]:
                total_highest += int(self.weather_data[year][month][day]["Max TemperatureC"] or 0)
                total_lowest += int(self.weather_data[year][month][day]["Min TemperatureC"] or 0)
                total_mean_humidity += int(self.weather_data[year][month][day]["Mean Humidity"] or 0)

            self.weather_data_calculations[year]={}
            self.weather_data_calculations[year][month] = {}
            self.weather_data_calculations[year][month]["avg_highest_temp"] = round(total_highest/total_days, 1)
            self.weather_data_calculations[year][month]["avg_lowest_temp"] = round(total_lowest/total_days, 1)
            self.weather_data_calculations[year][month]["avg_mean_humidity"] = round(total_mean_humidity/total_days, 1)
