import streamlit as st
import requests

st.title('Taxi Fare Predictor')


st.header('Wondering what it\'s going to cost you? Get an data-based estimate with this NYC cab fare predictor')

st.subheader('Input below details and let our model work it\'s magic:')


pickup_date = st.date_input('Date')
pickup_time = st.time_input('Time')
pickup_longitude = st.number_input('Pickup Longitude', format='%f', value=40.7614327)
pickup_latitude = st.number_input('Pickup Latitude', format='%f', value=-73.9798156)
dropoff_longitude = st.number_input('Dropoff Longitude', format='%f', value=40.6513111)
dropoff_latitude = st.number_input('Dropoff Latitude', format='%f', value=-73.8803331)
passenger_count = st.number_input('Number of Passengers', format='%i', value=1)

st.markdown("""---""")

url = 'https://light-intel-fqcfqdx4ka-ew.a.run.app/predict'

pickup_datetime = f"{pickup_date} {pickup_time}"
params={'pickup_datetime': pickup_datetime, 'pickup_longitude': pickup_longitude, 'pickup_latitude': pickup_latitude, 'dropoff_longitude': dropoff_longitude, 'dropoff_latitude': dropoff_latitude, 'passenger_count': passenger_count}
response = requests.get(url, params=params).json()

st.header(f"This is your fare estimation: {response['fare_amount']}")
