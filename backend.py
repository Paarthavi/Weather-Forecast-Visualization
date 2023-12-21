import os
import requests

API_KEY = os.getenv("openweather_api")

def get_data(place, forecast_days=None, kind=None):
	url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
	response = requests.get(url)
	data = response.json()
	filtered_data = data["list"]
	# Multiplying forecast days with 8 because one day has 24 hours and data are being recorded every 3 hours
	# so 24/3 = 8 is equal to 8 data points
	nr_values = 8 * forecast_days
	filtered_data = filtered_data[:nr_values]
	if kind == "Temperature":
		filtered_data = [dict["main"]["temp"] for dict in filtered_data]
	if kind == "Sky":
		filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
	return filtered_data

if __name__ == "__main__":
	print(get_data(place="Tokyo", forecast_days=3, kind="Temperature"))