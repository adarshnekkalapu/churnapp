import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("churn_model.pkl", "rb"))

st.title("📞 Telecom Customer Churn Prediction")

# Input features
gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", [0, 1])
tenure = st.slider("Tenure (months)", 0, 72)
monthly = st.number_input("Monthly Charges", 0.0, 200.0, 50.0)

# Simple example: assuming 4 features only (you can map full ones)
input_df = pd.DataFrame([[gender, senior, tenure, monthly]], 
                        columns=["gender", "SeniorCitizen", "tenure", "MonthlyCharges"])
input_df['gender'] = input_df['gender'].map({'Male': 1, 'Female': 0})

if st.button("Predict Churn"):
    prediction = model.predict(input_df)[0]
    st.success("✅ Not likely to churn" if prediction == 0 else "⚠️ Likely to churn")
