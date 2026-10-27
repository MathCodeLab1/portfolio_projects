
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

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Torque")

    fig = px.box(
        filtered_df,
        x="Machine failure",
        y="Torque [Nm]",
        color="Machine failure",
        color_discrete_map={0: "lightblue", 1: "red"}
    )
    st.plotly_chart(fig, width="stretch")



with col2:
    st.subheader("Rotational Speed")

    fig = px.box(
        filtered_df,
        x="Machine failure",
        y="Rotational speed [rpm]",
        color="Machine failure",
        color_discrete_map={0: "lightblue", 1: "red"}
    )
    st.plotly_chart(fig, width="stretch")



with col3:
    st.subheader("Tool Wear")

    fig = px.box(
        filtered_df,
        x="Machine failure",
        y="Tool wear [min]",
        color="Machine failure",
        color_discrete_map={0: "lightblue", 1: "red"}
    )
    st.plotly_chart(fig, width="stretch")


st.header("Key Observations")

st.write("""
The boxplots show clear differences between machines with and without failure. Machines with 
failure tend to have higher torque and tool wear, while their rotational speed is generally lower.
These patterns suggest that operating conditions are associated with machine failure.
""")