import streamlit as st
import numpy as np
import pickle

# Load model and scaler
import pickle

model = pickle.load(open('model/model.pkl', 'rb'))
scaler = pickle.load(open('model/scaler.pkl', 'rb'))

st.title("Obesity Prediction App")
st.write("Enter your details below:")

# Input form
age = st.number_input("Age", min_value=1, max_value=100, value=25)
weight = st.number_input("Weight (kg)", min_value=10.0, max_value=200.0, value=70.0)
height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=170.0)

# Calculate BMI
bmi = weight / ((height / 100) ** 2)
st.write(f"**BMI:** {bmi:.2f}")

# Predict button
if st.button("Predict"):
    input_data = np.array([[age, weight, height, bmi]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    result = "Obese" if prediction == 1 else "Not Obese"
    st.success(f"Prediction: **{result}**")
    st.info(f"Probability of being obese: **{probability:.2f}**")
