import streamlit as st
import pickle
import numpy as np
import joblib

# Load the trained model from the pickle fil
import pickle

model = joblib.load("credit_card_model.pkl",)
st.set_page_config(page_title="Credit Card Fraud Detection", layout="centered")
st.title("💳 Credit Card Fraud Detection")
st.markdown("Enter transaction features and adjust the threshold to control false positives.")

inputs = []
for i in range(30):
    val = st.number_input(f"Feature {i+1}", value=0.0)
    inputs.append(val)

threshold = st.slider("Set fraud probability threshold", 0.0, 1.0, 0.5, 0.01)

if st.button("Check Transaction"):
    input_array = np.array(inputs).reshape(1, -1)
    proba = model.predict_proba(input_array)[0][1]
    st.markdown(f"*Fraud Probability:* {proba:.4f}")
    
    if proba >= threshold:
        st.error("⚠️ Fraudulent Transaction Detected")
    else:
        st.success("✅ Normal Transaction")


