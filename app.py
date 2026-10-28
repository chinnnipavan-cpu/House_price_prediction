import streamlit as st
import joblib
import numpy as  np
st.set_page_config(page_title="House Price Prediction", page_icon=":house:", layout="wide")

@st.cache_resource
def load_model():
    model=joblib.load('house_price_model.pkl')
    return model
model=load_model()

st.title("House Price Prediction")
st.write("This app predicts the price of a house based on its features.")
area=st.number_input("Enter the area of the house (in square feet):", min_value=100, max_value=10000, value=1000)
bedrooms=st.number_input("Enter the number of bedrooms:", min_value=1, max_value=10, value=3)
bathrooms=st.number_input("Enter the number of bathrooms:", min_value=1, max_value=10, value=2)
garage=st.number_input("Enter the number of cars that can fit in the garage:", min_value=0, max_value=5, value=2)
year_built=st.number_input("Enter the year the house was built:", min_value=1800, max_value=2023, value=2020)

if st.button("Predict Price"):
    input_data=np.array([[area, bedrooms, bathrooms, garage, year_built ]])
    prediction=model.predict(input_data)
    st.success(f"The predicted price of the house is: ${prediction[0]:,.2f}")

