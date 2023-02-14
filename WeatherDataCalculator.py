class WeatherDataCalculator:

    def calculate_year_temperatures(self, yearly_weather_records):
        if not yearly_weather_records:
            return []

        max_record = max(yearly_weather_records,
                         key=lambda record: record.max_temperature)
        min_record = min(yearly_weather_records,
                         key=lambda record: record.min_temperature)
        max_humidity_record = max(
            yearly_weather_records, key=lambda record: record.max_humidity)

        return (max_record, min_record, max_humidity_record)

    def calculate_avg_month_results(self, month_weather_data):
        if not month_weather_data:
            return []
        
        valid_highest_records = [
            record for record in month_weather_data if record.max_temperature is not None]

        average_highest_temperature = round(sum(
            record.max_temperature for record in valid_highest_records)/len(valid_highest_records), 1)
        
        valid_lowest_records = [
            record for record in month_weather_data if record.min_temperature is not None]

        average_lowest_temperature = round(sum(
            record.min_temperature for record in valid_lowest_records)/len(valid_lowest_records), 1)
        
        valid_mean_humudity_records = [
            record for record in month_weather_data if record.mean_humidity is not None]

        average_mean_humidity_temperature = round(sum(
            record.mean_humidity for record in valid_mean_humudity_records)/len(valid_mean_humudity_records), 1)
            
        return (average_highest_temperature, average_lowest_temperature , average_mean_humidity_temperature)
