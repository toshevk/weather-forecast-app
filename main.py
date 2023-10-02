import streamlit as st
import plotly.express as px
from request_weather import get_weather_data

st.title("Weather Forecast 🌤️")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days for the forecast")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    weather_data = get_weather_data(place, days, option)
    if option == "Temperature":
        temp_data = []
        temp_date = []
        for data in weather_data:
            temp_data.append(data['temperature'])
            temp_date.append(data['date'])
        # Temperature plot
        figure = px.line(x=temp_date, y=temp_data,
                         labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        # Sky render
        sky_data = []
        sky_img = []
        sky_date = []
        for data in weather_data:
            sky_data.append(data['description'])
            sky_img.append(data['img'])
            sky_date.append(data['date'])
        st.image(sky_img, width=100, caption=sky_date)