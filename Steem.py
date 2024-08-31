import streamlit as st
import requests

st.title("E-Sport")


Processor = st.number_input("Processor ", min_value=0, max_value=1000, value=2)
Memory = st.number_input("Memory ", min_value=0, max_value=700, value=2)
Storage = st.number_input("Storage", min_value=0.0, max_value=500000.0, value=15000.0)


if st.button("Predict"):
    response = requests.post(f"https://e-sport-fastapi.onrender.com/predict", json={
        "Processor": Processor,
        "Memory": Memory,
        "Storage": Storage,
    })
    
    if response.status_code == 200:
        prediction = response.json().get("cluster")
        st.write(f"The predicted cluster is: {prediction}")
    else:
        st.write("Error: Could not get prediction from the API")

