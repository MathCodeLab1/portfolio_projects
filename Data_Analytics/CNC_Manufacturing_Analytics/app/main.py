import streamlit as st

dashboard = st.Page(
    "app.py",
    title="Dashboard",
    default=True
)

analysis = st.Page(
    "analysis.py",
    title="Detailed Analysis"
)

navigation = st.navigation([dashboard, analysis])

navigation.run()