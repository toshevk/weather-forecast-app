import streamlit as st
import plotly.express as px
from request_weather import get_weather_data

st.title("Weather Forecast 🌤️")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days for the forecast")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

dates = ["2023-09-30", "2023-10-01", "2023-10-02", "2023-10-03", "2023-10-04", "2023-10-05"]
temperatures = [27.1, 27.2, 26.6, 26.4, 26.9, 26.5]

weather_data = get_weather_data(place, days, option)

figure = px.line(x=dates, y=temperatures,
                 labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)
