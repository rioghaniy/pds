import pickle
import numpy as np
import streamlit as st

loaded_model = pickle.load(open('E:/Kuliah/Semester 6/Proyek DS/Air Passenger Satisfaction/model_knn.sav'))

def air_passenger_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0] == 0):
        return'Pelanggan tidak puas'
    else:
        return'Pelanggan puas'

def main():
    
    st.title('')

    Gender,Customer_Type, Age, Type_of_Travel, Class, Flight_Distance, 
    Inflight_wifi_service, Departure_or_Arrival_time_convenient, Ease_of_Online_booking,
    Gate_location, Food_and_drink, Online_boarding, Seat_comfort,
    Inflight_entertainment, On_board_service, Leg_room_service,
    Baggage_handling, Checkin_service, Inflight_service,
    Cleanliness, Departure_Delay_in_Minutes, Arrival_Delay_in_Minutes

    Gender = st.select.slider('Gender',['Male','Female'])
    Customer_Type = st.select.slider('Customer Type',['Loyal Customer','Disloyal Customer'])
    Age = st.text_input('Age')
    Type_of_Travel = st.text_input('Type of Travel',['Business Travel','Personal Travel'])
    Class = st.text_input('Class',['Business','Eco','Eco Plus'])
    Flight_Distance = st.text_input('Fligh Distance')
    Inflight_wifi_service= st.text_input('Inflight wifi service')
    Departure_Arrival_time_convenient = st.text_input('Departure Arrival time convenient')
    Ease_of_Online_booking = st.text_input('Ease_of_Online_booking') 
    Gate_location = st.text_input('Gate_location')
    Food_and_drink = st.text_input('Food_and_drink')
    Onlie_boarding = st.text_input('Online_boarding')
    Seat_compfort = st.text_input('Srat_comfort')
    Inflight_entertainment = st.text_input('Inflight_entertainment')
    On_board_service = st.text_input('On-board service')
    Leg_room_service = st.text_input('Leg_room_service')
    Baggage_handling = st.text_input('Baggage_handling')
    Checkin_service = st.text_input('Checkin_service')
    Inflight_service = st.text_input('Inflight_service')
    Cleanliness = st.text_input('Cleanliness')
    Departure_Delay_in_Minutes = st.text_input('Departure_Delay_in_Minutes')
    Arrival_Delay_in_Minutes = st.text_input('Arrival_Delay_in_Minutes')

    Satisfaction = ''

    if st.button('Hasil Prediksi'):
        diagnosis = air_passenger_prediction([Gender, Customer_Type, Age, Type_of_Travel, Class,
        Flight_Distance, Inflight_wifi_service,
        Departure_or_Arrival_time_convenient, Ease_of_Online_booking,
        Gate_location, Food_and_drink, Online_boarding, Seat_comfort,
        Inflight_entertainment, On_board_service, Leg_room_service,
        Baggage_handling, Checkin_service, Inflight_service,
        Cleanliness, Departure_Delay_in-Minutes, Arrival_Delay_in_Minutes])

    st.succes(Satisfaction)

if __name__ == '__main__':
    main()

