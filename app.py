import streamlit as st
import joblib
import numpy as np

# Load the trained model and scaler
model = joblib.load("D:\\ML heart disease project\\random_forest_heart_disease_model.pkl")
scaler = joblib.load("D:\\ML heart disease project\\scaler_heart_disease.pkl")

# Streamlit app title
st.title("Heart Disease Risk Prediction")

# User input fields
age = st.number_input("Age", min_value=1, max_value=120, value=30)
sex = st.selectbox("Sex", [0, 1])  # 0: Female, 1: Male
chest_pain = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
resting_bp_s = st.number_input("Resting BP", min_value=50, max_value=250, value=120)
cholesterol = st.number_input("Cholesterol", min_value=100, max_value=600, value=200)
fasting_bloodsugar = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
resting_ecg = st.selectbox("Resting ECG", [0, 1, 2])
heart_rate = st.number_input("Max Heart Rate", min_value=60, max_value=220, value=150)
exercise_angina = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.number_input("Oldpeak", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
ST_slope = st.selectbox("ST Slope", [1, 2, 3])

# Prediction button
if st.button("Predict Risk"):
    # Prepare input
    input_data = np.array([[age, sex, chest_pain, resting_bp_s, cholesterol,
                            fasting_bloodsugar, resting_ecg, heart_rate,
                            exercise_angina, oldpeak, ST_slope]])
    
    # Scale input
    input_data_scaled = scaler.transform(input_data)
    
    # Make prediction
    prediction = model.predict(input_data_scaled)
    prob = model.predict_proba(input_data_scaled)[0][1]
    
    # Show result
    if prediction[0] == 1:
        st.error(f"High Risk ⚠\nProbability: {prob:.2f}")
    else:
        st.success(f"Low Risk 😊\nProbability: {prob:.2f}")
