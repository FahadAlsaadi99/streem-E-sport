import streamlit as st
import requests
import pandas as pd

st.title("E-Sport")

Processor = st.number_input("CPU(Core) ", min_value=0, max_value=24, value=2)
Memory = st.number_input("Memory(GB) ", min_value=0, max_value=32, value=2)
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
        
        if prediction == [0]:
            subset = df[df['cluster'] == 0]['Game Names']
            sample_size = min(10, len(subset))
            b = subset.sample(n=sample_size)
            html_table = b.to_frame().reset_index(drop=True).to_html(index=False)
            st.markdown(html_table, unsafe_allow_html=True)
            
        if prediction == [1]:
            subset = df[df['cluster'] == 1]['Game Names']
            sample_size = min(10, len(subset))
            a = subset.sample(n=sample_size)
            html_table = a.to_frame().reset_index(drop=True).to_html(index=False)
            st.markdown(html_table, unsafe_allow_html=True)
        
        if prediction == [2]:
            subset = df[df['cluster'] == 2]['Game Names']
            sample_size = min(10, len(subset))
            c = subset.sample(n=sample_size)
            html_table = c.to_frame().reset_index(drop=True).to_html(index=False)
            st.markdown(html_table, unsafe_allow_html=True)

        if prediction == [3]:
            subset = df[df['cluster'] == 3]['Game Names']
            sample_size = min(10, len(subset))
            d = subset.sample(n=sample_size)
            html_table = d.to_frame().reset_index(drop=True).to_html(index=False)
            st.markdown(html_table, unsafe_allow_html=True)

        if prediction == [4]:
            subset = df[df['cluster'] == 0]['Game Names']
            sample_size = min(10, len(subset))
            e = subset.sample(n=sample_size)
            html_table = e.to_frame().reset_index(drop=True).to_html(index=False)
            st.markdown(html_table, unsafe_allow_html=True)
        
    else:
        st.write("Error: Could not get prediction from the API")
