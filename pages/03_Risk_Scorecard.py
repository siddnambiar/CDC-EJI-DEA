import streamlit as st
import pandas as pd
from measure_groups import eji_percentile_measures  # Import the EJI percentile measures

st.set_page_config(page_title="Risk Scorecard - CDC EJI Explorer", page_icon="🛡️", layout="wide")
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# Load the data
@st.cache_data
def load_data():
    return pd.read_csv('CDC_EJI_US.csv')

data = load_data()

# Create a unique identifier for County and State combination
data['County_State'] = data['COUNTY'] + ", " + data['StateDesc']

# Sidebar for County and State selection
st.sidebar.header("🛡️ Risk Scorecard")
st.sidebar.write("Use this page to view detailed Environmental Justice Index (EJI) information for a specific county and state.")
selected_county_state = st.sidebar.selectbox(
    "Select a County, State combination", 
    options=data['County_State'].unique(),
    help="Select a county to view its risk scorecard."
)

# Function to determine color based on value and context
def get_color(value, higher_is):
    if higher_is == "bad":
        if value > 80:
            return "red"
        elif value > 40:
            return "blue"
        else:
            return "green"
    elif higher_is == "good":
        if value > 80:
            return "green"
        elif value > 40:
            return "blue"
        else:
            return "red"
    return "gray"  # For neutral

# Main content
st.title("🛡️ Risk Scorecard")
st.write("The Risk Scorecard provides a detailed overview of the Environmental Justice Index (EJI) measures for the selected county and state. Use this page to explore specific vulnerabilities and strengths in various categories.")

if selected_county_state:
    # Filter data for the selected County, State
    county_data = data[data['County_State'] == selected_county_state]

    # Ensure we are working with a single row
    if not county_data.empty:
        county_data = county_data.iloc[0]  # Extract the first row as a Series

        # Display Total Population in large numbers
        total_population = county_data['E_TOTPOP']
        st.markdown(f"<h1 style='text-align: center; color: #007bff;'>Population: {total_population:,}</h1>", unsafe_allow_html=True)

        # Display measures in cards under expanders
        for category, measures in eji_percentile_measures.items():
            with st.expander(f"{category} Measures (click to expand)", expanded=False):
                st.markdown(f"### {category}")
                st.write(f"The following measures provide insights into the {category.lower()} aspects of the selected county. Higher values may indicate either greater risk or greater benefit, depending on the measure's context.")
                
                cols = st.columns(3)  # Create three columns for cards
                for i, (measure, details) in enumerate(measures.items()):
                    value = county_data[measure] * 100  # Convert to percentage
                    color = get_color(value, details['higher_is'])
                    with cols[i % 3]:  # Distribute cards across columns
                        st.markdown(f"""
                        <div style="border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9; text-align: center; height:225px; margin-bottom: 15px;">
                            <h4 style="color: {color};">{details['description']}</h4>
                            <p>Value: <span style="color: {color}; font-size: 24px;">{value:.2f}%</span></p>
                            <p style="font-size: 12px;">{details['context']}</p>
                        </div>
                        """, unsafe_allow_html=True)
else:
    st.markdown("## Instructions")
    st.write("Please select a County, State combination from the sidebar to view the detailed risk scorecard for that region.")
