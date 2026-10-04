import streamlit as st
import pandas as pd
import pickle

# Load the trained Gradient Boosting model
with open("gradient_boosting_model.pkl", "rb") as model_file:
    prediction_model = pickle.load(model_file)
    
st.set_page_config(
    page_title="Sydney Housing Price Predictor",
    page_icon="🏠",
    layout="centered"
)

st.title("Sydney Housing Price Prediction")
st.write(
    "Enter the property details below to estimate the sale price "
    "for a property in Parramatta, Ryde or Blacktown."
)

st.subheader("Property Details")

suburb = st.selectbox(
    "Suburb",
    ["Parramatta", "Ryde", "Blacktown"]
)

property_type = st.selectbox(
    "Property Type",
    ["Unit", "House"]
)

bedrooms = st.number_input(
    "Bedrooms",
    min_value=1,
    max_value=10,
    value=2,
    step=1
)

bathrooms = st.number_input(
    "Bathrooms",
    min_value=1,
    max_value=10,
    value=1,
    step=1
)

car_spaces = st.number_input(
    "Car Spaces",
    min_value=0,
    max_value=10,
    value=1,
    step=1
)

# Generate a prediction from the user's property details
if st.button("Predict Sale Price"):

    input_property = pd.DataFrame({
        "Suburb": [suburb],
        "PropertyCategory": [property_type],
        "Bedrooms": [bedrooms],
        "Bathrooms": [bathrooms],
        "CarSpaces": [car_spaces]
    })

    predicted_price = prediction_model.predict(input_property)[0]

    st.success(
        f"Estimated Sale Price: ${predicted_price:,.0f}"
    )

    st.caption(
        "This estimate is generated from the Gradient Boosting regression "
        "model and should be used as decision-support rather than a property valuation."
    )