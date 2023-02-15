class WeatherDataCalculator:

    def calculate_year_temperatures(self, yearly_weather_records):
        if not yearly_weather_records:
            return []

        max_record = max(yearly_weather_records, key=lambda record: record.max_temperature)
        min_record = min(yearly_weather_records, key=lambda record: record.min_temperature)
        max_humidity_record = max(yearly_weather_records, key=lambda record: record.max_humidity)

        return max_record, min_record, max_humidity_record

    def calculate_avg_month_results(self, month_weather_data):
        if not month_weather_data:
            return []
        
        max_temps = [record for record in month_weather_data if record.max_temperature is not None]
        avg_max_temp = sum(record.max_temperature for record in max_temps) // len(max_temps)
    
        min_temps = [record for record in month_weather_data if record.min_temperature is not None]
        avg_min_temp = sum(record.min_temperature for record in min_temps) // len(min_temps)
        
        humidity_temps = [record for record in month_weather_data if record.mean_humidity is not None]
        avg_humidity_temp = sum(record.mean_humidity for record in humidity_temps) // len(humidity_temps)
            
        return avg_max_temp, avg_min_temp , avg_humidity_temp
