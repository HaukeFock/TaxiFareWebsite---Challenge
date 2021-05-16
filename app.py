import streamlit as st
import requests 

st.markdown("**TaxiFare Prediction in NYC**")

pickup_date = st.date_input("Date of pickup?3")
pickup_time = st.time_input('Time of pickup?')
pickup_datetime = (f"{pickup_date} {pickup_time} UTC")
pickup_longitude = st.number_input('Longitude Startpoint?')
pickup_latitude = st.number_input('Latitude Startpoint?')
dropoff_longitude = st.number_input('Longitude Endpoint?')
dropoff_latitude = st.number_input('Latitude Endpoint?')
passenger_count = st.number_input('How many passengers?')


url = 'https://taxifare.lewagon.ai/predict_fare/'

params = {
    "key": pickup_datetime,
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": float(pickup_longitude),
    "pickup_latitude": float(pickup_latitude),
    "dropoff_longitude": float(dropoff_longitude),
    "dropoff_latitude": float(dropoff_latitude),
    "passenger_count": int(passenger_count)
}

if st.button('Predict'):
    response = requests.get(url, params= params)
    print(response.json())
    response_fare = response.json()["prediction"]
    st.write(f"Your fare will be: {response_fare}")
   