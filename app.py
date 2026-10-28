import streamlit as st
import joblib
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="House Price Prediction", page_icon=":house:", layout="wide")

@st.cache_resource
def load_model():
    return joblib.load(Path(__file__).with_name("house_prediction.pkl"))

@st.cache_data
def load_default_features(feature_names):
    data_path = Path(__file__).with_name("Cleaned_datset.csv")
    training_data = pd.read_csv(data_path).drop(columns=["SalePrice"])
    encoded_data = pd.get_dummies(training_data, drop_first=True)
    defaults = encoded_data.median(numeric_only=True).to_frame().T
    return defaults.reindex(columns=feature_names, fill_value=0)

model=load_model()

st.title("House Price Prediction")
st.write("This app predicts the price of a house based on its features.")
area=st.number_input("Enter the area of the house (in square feet):", min_value=100, max_value=10000, value=1000)
bedrooms=st.number_input("Enter the number of bedrooms:", min_value=1, max_value=10, value=3)
bathrooms=st.number_input("Enter the number of bathrooms:", min_value=1, max_value=10, value=2)
garage=st.number_input("Enter the number of cars that can fit in the garage:", min_value=0, max_value=5, value=2)
year_built=st.number_input("Enter the year the house was built:", min_value=1800, max_value=2023, value=2020)

if st.button("Predict Price"):
    feature_names = tuple(model.feature_names_in_)
    input_data = load_default_features(feature_names)
    input_data.loc[0, ["GrLivArea", "BedroomAbvGr", "FullBath", "GarageCars", "YearBuilt"]] = [
        area,
        bedrooms,
        bathrooms,
        garage,
        year_built,
    ]
    prediction=model.predict(input_data)
    st.success(f"The predicted price of the house is: ${prediction[0]:,.2f}")
