
import streamlit as st
import pandas as pd

st.title ("CNC Predictive Maintenance Dashboard")

df = pd.read_csv ("Data_Analytics/CNC_Manufacturing_Analytics/data/ai4i2020.csv")

st.header("About the CNC Dataset")

st.write("""
The dataset contains 10,000 observations of machine operating conditions and machine failures. 
It includes variables such as air temperature, process temperature, rotational speed, torque, and tool wear.

This dashboard investigates which machine operating conditions are associated with machine failure.
""")


with st.sidebar:
    st.header("Filter")
    selected_type = st.selectbox("Machine Type", df["Type"].unique())

filtered_df = df[df["Type"] == selected_type]

st.header("Basic Statistics")

st.dataframe(filtered_df.describe(), use_container_width=True)
