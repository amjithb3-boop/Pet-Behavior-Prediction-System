import streamlit as st
import joblib
import numpy as np

model = joblib.load('pet_behavior_model.pkl')
scaler = joblib.load('pet_behavior_scaler.pkl')

st.title("Pet Behavior Prediction System")


barking_frequency = st.number_input(
    "Barking Frequency",
    min_value=1,
    max_value=20,
    value=5
)

aggression_level = st.number_input(
    "Aggression Level",
    min_value=1,
    max_value=10,
    value=5
)

anxiety_level = st.number_input(
    "Anxiety Level",
    min_value=1,
    max_value=10,
    value=5
)

activity_level = st.number_input(
    "Activity Level",
    min_value=1,
    max_value=10,
    value=5
)

social_interaction = st.number_input(
    "Social Interaction",
    min_value=1,
    max_value=10,
    value=5
)

eating_habits = st.number_input(
    "Eating Habits",
    min_value=1,
    max_value=10,
    value=5
)

sleep_disruptions = st.number_input(
    "Sleep Disruptions",
    min_value=0,
    max_value=4,
    value=2
)



if st.button("Predict Pet Behavior"):

    input_data = np.array([[
        barking_frequency,
        aggression_level,
        anxiety_level,
        activity_level,
        social_interaction,
        eating_habits,
        sleep_disruptions
    ]])


    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    if prediction[0] == 0:
        st.success("Normal Behavior")

    else:
        st.warning("Possible Behavioral Concern")