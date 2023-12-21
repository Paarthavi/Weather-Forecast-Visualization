import streamlit as st
import plotly.express as px
from backend import get_data

# Add a title
st.title("Weather Forecast for the Next Days")

# Add a text input
place = st.text_input("Place: ")

# Add a slider
days = st.slider("Forecast Days", min_value=1, max_value=5,
				 help="Select the number of forecasted days")

# Add a selectbox
option = st.selectbox(label="Select data to view", options=("Temperature", "Sky"))

# Add a subheader
st.subheader(f"{option} for the next {days} days in {place}")

if place:
	# Get the temperature/sky data
	try:
		filtered_data = get_data(place, days)

		if option == "Temperature":
			temperatures = [round(dict["main"]["temp"] - 273.15, 1) for dict in filtered_data]
			dates = [dict["dt_txt"] for dict in filtered_data]
			# Create a temperature plot
			figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
			st.plotly_chart(figure)

		if option == "Sky":
			images = {"Clear": "images_weather/clear.png", "Clouds": "images_weather/cloud.png",
					  "Rain": "images_weather/rain.png", "Snow": "images_weather/snow.png"}
			sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
			image_paths = [images[condition] for condition in sky_conditions]
			st.image(image_paths, width=115)
	except KeyError:
		st.write("Uh oh you entered a non-existing place")