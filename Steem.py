import streamlit as st
import requests
import pandas as pd

st.title("E-Sport")

Processor = st.number_input("CPU(Core) ", min_value=0, max_value=24, value=2)
Memory = st.number_input("Memory(GB) ", min_value=0, max_value=8192, value=2)
Storage = st.number_input("Storage(GB)", min_value=0, max_value=30000, value=15000)

df = pd.read_csv('list_of_games.csv')
if st.button("Predict"):
    response = requests.post("https://e-sport-fastapi.onrender.com/predict", json={
        "Processor": Processor,
        "Memory": Memory,
        "Storage": Storage,
    })
    
    if response.status_code == 200:
        prediction = response.json().get("cluster")
        
        if prediction == [1]:
            subset = df[df['cluster'] == 1]['Game Names']
            sample_size = min(10, len(subset))  # تعديل العدد هنا إلى 10
            a = subset.sample(n=sample_size)  # إزالة random_state لجعل العينة عشوائية
            st.write(a)
        
        if prediction == [0]:
            subset = df[df['cluster'] == 0]['Game Names']
            sample_size = min(10, len(subset))  # تعديل العدد هنا إلى 10
            b = subset.sample(n=sample_size)  # إزالة random_state لجعل العينة عشوائية
            st.write(b)
    else:
        st.write("Error: Could not get prediction from the API")
