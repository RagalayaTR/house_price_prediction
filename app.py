import streamlit as st
import pandas as pd
import joblib
import os

# Load trained model
model_path = os.path.join(
    os.path.dirname(__file__),
    "house_price_model.pkl"
)

model = joblib.load(model_path)

# App title
st.title("House Price Prediction")
st.write("Predict house price based on area, bedrooms and floors")

# User inputs
area = st.number_input(
    "Enter Area (Sq Ft)",
    min_value=100,
    max_value=10000,
    value=1500
)

bedrooms = st.number_input(
    "Number of Bedrooms",
    min_value=1,
    max_value=10,
    value=3
)

floors = st.number_input(
    "Number of Floors",
    min_value=1,
    max_value=20,
    value=5
)

# Prediction
if st.button("Predict Price"):

    # Create input dataframe
    input_data = pd.DataFrame({
        "area": [area],
        "bedrooms": [bedrooms],
        "floors": [floors]
    })

    # Predict
    prediction = model.predict(input_data)

    price = prediction[0]

    st.success(f"Estimated House Price: ₹ {price:.2f}")
