import streamlit as st
import requests
import pandas as pd

st.title("E-Sport")


Processor = st.number_input("Processor ", min_value=0, max_value=220, value=2)
Memory = st.number_input("Memory ", min_value=0, max_value=8192, value=2)
Storage = st.number_input("Storage", min_value=0, max_value=30000, value=15000)

df = pd.read_csv('list_of_games.csv')
if st.button("Predict"):
    response = requests.post(f"https://e-sport-fastapi.onrender.com/predict", json={
        "Processor": Processor,
        "Memory": Memory,
        "Storage": Storage,
    })
    
    if response.status_code == 200:
        prediction = response.json().get("cluster")
        st.write(f"The predicted cluster is: {prediction}")
        if prediction == [1]:
            st.write(df[['Game Names']][df['cluster'] == 1])
        if prediction == [0]:
            st.write(df[['Game Names']][df['cluster'] == 0])
    else:
        st.write("Error: Could not get prediction from the API")

