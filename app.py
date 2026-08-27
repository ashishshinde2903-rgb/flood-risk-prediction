import streamlit as st
import pandas as pd
import pickle


# -----------------------------------------
# Load model

with open("model.pkl", "rb") as file:
    saved = pickle.load(file)

model = saved["model"]
le = saved["label_encoder"]


# -----------------------------------------
# Load dataset

df = pd.read_csv("flood_risk_ml_dataset.csv")


# ------------------------------------------
# Page configuration

st.set_page_config(
    page_title="Flood Risk Prediction",
    page_icon="🌊",
    layout="wide"
)


# -------------------------------------------
# Title

st.title("🌊 Flood Risk Prediction")

st.write(
    "Enter environmental and geographical conditions "
    "to predict flood risk."
)


# ------------------------------------------
# Inputs

state = st.selectbox(
    "State",
    sorted(df["State"].unique())
)

districts = sorted(
    df[df["State"] == state]["District"].unique()
)

district = st.selectbox(
    "District",
    districts
)

rainfall = st.number_input(
    "Rainfall (mm): 0.0 to 552.5",
    min_value=0.0,
    value=100.0
)

river_level = st.number_input(
    "River Water Level (m): 0.44 to 9.46",
    min_value=0.0,
    value=3.0
)

reservoir_level = st.number_input(
    "Reservoir Level (%): 15.0 to 100.0",
    min_value=0.0,
    max_value=100.0,
    value=50.0
)

soil_moisture = st.number_input(
    "Soil Moisture (%): 16.5 to 98.0",
    min_value=0.0,
    max_value=100.0,
    value=50.0
)

temperature = st.number_input(
    "Temperature (°C)",
    value=25.0
)

humidity = st.number_input(
    "Humidity (%)",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

elevation = st.number_input(
    "Elevation (m): 5.1 to 3595.2",
    min_value=0.0,
    value=500.0
)

slope = st.number_input(
    "Slope (degrees): 0.1 to 67.39",
    min_value=0.0,
    value=5.0
)

drainage = st.selectbox(
    "Drainage Quality",
    sorted(df["Drainage_Quality"].unique())
)

land_use = st.selectbox(
    "Land Use",
    sorted(df["Land_Use"].unique())
)



flood_history=st.selectbox(
    "Previous Flood History",
    sorted(df["Flood_History"].unique())
)

month = st.selectbox(
    "Month",
    sorted(df["Month"].unique())
)


# -----------------------------------------
# Prediction

if st.button("🔍 Predict Flood Risk"):

    input_data = pd.DataFrame({
        "State": [state],
        "District": [district],
        "Rainfall_mm": [rainfall],
        "River_Water_Level_m": [river_level],
        "Reservoir_Level_pct": [reservoir_level],
        "Soil_Moisture_pct": [soil_moisture],
        "Temperature_C": [temperature],
        "Humidity_pct": [humidity],
        "Elevation_m": [elevation],
        "Slope_deg": [slope],
        "Drainage_Quality": [drainage],
        "Land_Use": [land_use],
        "Flood_History": [flood_history],
        "Month": [month]
    })

    prediction_encoded = model.predict(input_data)

    prediction = le.inverse_transform(
        prediction_encoded.astype(int)
    )[0]

    st.subheader("Prediction")

    st.success(
        f"Predicted Flood Risk: {prediction}"
    )