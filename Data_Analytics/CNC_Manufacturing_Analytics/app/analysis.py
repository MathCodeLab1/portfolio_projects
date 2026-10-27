
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Detailed Machine Failure Analysis")

df = pd.read_csv("Data_Analytics/CNC_Manufacturing_Analytics/data/ai4i2020.csv")

with st.sidebar:
    st.header("Filter")
    selected_type = st.selectbox("Machine Type", df["Type"].unique())


st.write(
    "This page investigates the relationship between torque "
    "and rotational speed for machines with and without failure."
)

st.write(
    "Machine failures are mainly concentrated at lower rotational "
    "speeds and higher torque values."
)

filtered_df = df[df["Type"] == selected_type]

filtered_df = filtered_df.copy()
filtered_df["Machine failure"] = filtered_df["Machine failure"].astype(str)

fig = px.scatter(
    filtered_df,
    x="Rotational speed [rpm]",
    y="Torque [Nm]",
    color="Machine failure",
    color_discrete_map={"0": "lightblue", "1": "red"}
)
st.plotly_chart(fig, width="stretch")

st.header("Key Observations")

st.write(
    "Machine failures are more frequently observed at lower rotational "
    "speeds and higher torque values. However, failures also occur in "
    "other operating conditions, so these variables alone do not explain "
    "all machine failures."
)

st.header("Failure Rate by Machine Type")

failure_rate = (
    df.groupby("Type")["Machine failure"]
    .mean()
    .reset_index()
)

failure_rate["Failure Rate (%)"] = failure_rate["Machine failure"] * 100

fig = px.bar(
    failure_rate,
    x="Type",
    y="Failure Rate (%)",
    labels={
        "Type": "Machine Type", 
        "Failure Rate (%)": "Failure Rate (%)"
    },
    color_discrete_sequence=["lightblue"]
)    
st.plotly_chart(fig, width="stretch")


st.header("Failure Types")

failure_types = [
    "TWF",  # Tool Wear Failure
    "HDF",  # Heat Dissipation Failure
    "PWF",  # Power Failure
    "OSF",  # Overstrain Failure
    "RNF"   # Random Failure
]

failure_counts = df[failure_types].sum().reset_index()
failure_counts.columns = ["Failure Type", "Count"]

fig = px.bar(
    failure_counts,
    x="Failure Type",
    y="Count",
    color_discrete_sequence=["lightblue"]
)
st.plotly_chart(fig, width="stretch")


st.header("Key Observations")

st.write(
    "HDF is the most frequently observed failure type, followed by OSF and PWF. "
    "RNF is the least frequently observed failure type."
)