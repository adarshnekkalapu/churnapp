import streamlit as st
import pandas as pd
import joblib

st.title("Churn Prediction App")
model = joblib.load("model.pkl")

age = st.number_input("Age", min_value=18, max_value=100)
gender = st.selectbox("Gender", ["Male", "Female"])
tenure = st.slider("Tenure (months)", 1, 72)
balance = st.number_input("Account Balance")
is_active = st.selectbox("Is Active", [0, 1])

input_data = pd.DataFrame({
    'Age': [age],
    'Gender': [1 if gender == "Male" else 0],
    'Tenure': [tenure],
    'Balance': [balance],
    'IsActiveMember': [is_active]
})

if st.button("Predict Churn"):
    prediction = model.predict(input_data)
    st.write("Churn Probability:" if prediction[0] == 1 else "Customer is likely to stay.")