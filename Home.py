import streamlit as st

# Set page configuration for a light-themed app
st.set_page_config(page_title="CDC EJI Dashboard", page_icon="🌍", layout="wide")

# Main Title and Welcome Message
st.title("🌍 Welcome to the CDC Environmental Justice Index Dashboard")

st.write("""
The Environmental Justice Index (EJI) by the CDC offers a comprehensive measure of the cumulative impacts of environmental burdens on health, focusing on human health and health equity across the U.S. This dashboard provides detailed insights into these metrics, allowing you to explore and analyze the data interactively.
""")

# Sidebar for Navigation
st.sidebar.header("📂 Navigation")
st.sidebar.write("Use the sidebar to navigate to different sections of the app.")

# Call to action to guide the user
st.markdown("""
<div style='text-align: center; border: 1px solid #ccc; padding: 20px; border-radius: 10px; background-color: #f9f9f9;'>
    <h2>🔍 Explore and Understand Environmental Justice Data</h2>
    <p>Dive into various aspects of environmental justice, analyze the data, and gain insights into how different factors affect community health across the U.S.</p>
</div>
""", unsafe_allow_html=True)
