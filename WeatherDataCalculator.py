class WeatherDataCalculator:
    def __init__(self):
        pass
        # self.weather_data_calculations = weather_data_calculations
        # self.weather_data = weather_data

    def calculate_year_results(self, year):
        if year in self.weather_data.keys():
            max_temp, max_month, max_day, min_temp, min_month, min_day, max_humidity, max_humidity_month, max_humidity_day = \
                self.calculate_temperatures(year)
            self.weather_data_calculations[year] = {
                "max_temp": max_temp,
                "max_month": max_month,
                "max_day": max_day,
                "min_temp": min_temp,
                "min_month": min_month,
                "min_day": min_day,
                "max_humidity": max_humidity,
                "max_humidity_month": max_humidity_month,
                "max_humidity_day": max_humidity_day
            }

    def calculate_year_temperatures(self, year_weather_data):
        if not year_weather_data:
            return []

        max_temp = year_weather_data[0].max_temperature
        min_temp = year_weather_data[0].min_temperature
        max_humidity = year_weather_data[0].max_humidity
        max_record = year_weather_data[0]
        min_record = year_weather_data[0]
        max_humidity_record = year_weather_data[0]

        for record in year_weather_data:
            if not record.max_temperature is None and record.max_temperature > max_temp:
                max_temp = record.max_temperature
                max_record = record

            if not record.min_temperature is None and record.min_temperature < min_temp:
                min_temp = record.min_temperature
                min_record = record

            if not record.max_humidity is None and record.max_humidity > max_humidity:
                max_humidity = record.max_humidity
                max_humidity_record = record

        return (max_record, min_record, max_humidity_record)

    def calculate_avg_month_results(self, month_weather_data):
        if not month_weather_data:
            return []

        total_highest = 0
        total_highest_day = 0
        total_lowest = 0
        total_lowest_day = 0
        total_mean_humidity = 0
        total_mean_humidity_days = 0

        for record in month_weather_data:
            if not record.max_temperature is None:
                total_highest += record.max_temperature
                total_highest_day += 1
            if not record.min_temperature is None:
                total_lowest += record.min_temperature
                total_lowest_day += 1

            if not record.mean_humidity is None:
                total_mean_humidity += record.mean_humidity
                total_mean_humidity_days += 1

        return (round(total_highest/total_highest_day, 1), round(total_lowest/total_lowest_day, 1), round(
            total_mean_humidity/total_mean_humidity_days, 1
        ))
