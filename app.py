import streamlit as st
import pandas as pd
import numpy as np
import joblib
import requests
import os

# --- Load model from Google Drive ---
@st.cache_resource
def load_model():
    model_path = "model.joblib"
    if not os.path.exists(model_path):
        url = "https://drive.google.com/uc?id=1MRK5kkhgl9yVFMfyKCbclLBFzTckKtlM&export=download"
        response = requests.get(url)
        with open(model_path, "wb") as f:
            f.write(response.content)
    return joblib.load(model_path)

model = load_model()


st.title("🔌 Electricity Sales Predictor")

st.markdown("""
Enter the following details to estimate electricity sales based on historical data and key features.
""")

# --- User Inputs ---
customers = st.number_input("Number of Customers", min_value=0)
price = st.number_input("Price (USD per unit)", min_value=0.0, format="%.4f")
sector = st.selectbox("Sector", ["Industrial", "Residential", "Commercial", "Transportation"])
month = st.selectbox("Month", list(range(1, 13)))
region = st.selectbox("Region", ["None", "South Atlantic", "West South Central"])

# --- One-hot Encoding for Sector ---
sector_features = {
    'sectorid_IND': 1 if sector == "Industrial" else 0,
    'sectorid_RES': 1 if sector == "Residential" else 0,
    'sectorid_COM': 1 if sector == "Commercial" else 0,
    'sectorid_TRA': 1 if sector == "Transportation" else 0,
}

# --- One-hot Encoding for Region ---
region_features = {
    'stateid_SAT': 1 if region == "South Atlantic" else 0,
    'stateid_WSC': 1 if region == "West South Central" else 0,
    'stateid_US': 0  # Always zero to exclude
}

# --- Build Input Dictionary ---
input_dict = {
    'customers': customers,
    'price': price,
    'month': month,
    **sector_features,
    **region_features
}

# Convert to DataFrame
input_data = pd.DataFrame([input_dict])

# Ensure all features match model expectations
if hasattr(model, "feature_names_in_"):
    model_features = list(model.feature_names_in_)

    # Add any missing columns with zero
    for col in model_features:
        if col not in input_data.columns:
            input_data[col] = 0

    # Reorder columns
    input_data = input_data[model_features]
else:
    st.error("⚠️ Model does not contain feature metadata. You may need to retrain it with scikit-learn >=1.0.")
    st.stop()

# --- Make Prediction ---
if st.button("Predict Sales"):
    prediction = model.predict(input_data)[0]
    st.success(f"🔋 Predicted Electricity Sales: {prediction:,.2f} units")
