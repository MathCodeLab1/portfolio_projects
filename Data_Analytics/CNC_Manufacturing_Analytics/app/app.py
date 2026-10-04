
import streamlit as st
import pandas as pd
import plotly.express as px

st.title ("CNC Machine Failure Analysis")

df = pd.read_csv ("Data_Analytics/CNC_Manufacturing_Analytics/data/ai4i2020.csv")

st.header("About the CNC Dataset")

st.write("Exploring which machine operating conditions are associated with machine failure.")

with st.sidebar:
    st.header("Machine Type")
    selected_type = st.selectbox("Machine Type", df["Type"].unique())

filtered_df = df[df["Type"] == selected_type]

st.header("Basic Statistics")

st.dataframe(filtered_df.describe(), use_container_width=True)


st.header("Machine Failure Analysis")

st.subheader("Torque")

fig = px.box(
    filtered_df,
    x="Machine failure",
    y="Torque [Nm]"
)
st.plotly_chart(fig)


st.subheader("Rotational Speed")

fig = px.box(
    filtered_df,
    x="Machine failure",
    y="Rotational speed [rpm]"
)
st.plotly_chart(fig)


st.subheader("Tool Wear")

fig = px.box(
    filtered_df,
    x="Machine failure",
    y="Tool wear [min]"
)
st.plotly_chart(fig)


st.header("Key Observations")

st.write("""
The relationship between machine operating conditions and failure varies by machine type.
The dashboard allows you to compare torque, rotational speed, and tool wear between machines with and without failure for each machine type.
""")