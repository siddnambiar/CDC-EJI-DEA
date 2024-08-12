import streamlit as st
import pandas as pd
import numpy as np
import random
from envelopment import DEA  # Importing the DEA class from envelopment.py
from measure_groups import dea_measures  # Importing measures from measure_groups.py

# Set page configuration
st.set_page_config(page_title="Performance Analysis - CDC EJI Explorer", page_icon="📈", layout="wide")
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Page title
st.title("📈 Performance Analysis")
st.write("""
This page allows you to assess how well selected counties are performing in managing environmental, social, and health-related factors. 
The analysis helps identify counties that effectively minimize negative impacts while promoting positive health outcomes.
""")

# Load the data
@st.cache_data
def load_data():
    return pd.read_csv('CDC_EJI_US.csv')

data = load_data()

# Create a unique identifier for County and State combination
data['County_State'] = data['COUNTY'] + ", " + data['StateDesc']

# Initialize session state for selected counties
if "selected_counties" not in st.session_state:
    st.session_state["selected_counties"] = []

# Sidebar instructions
st.sidebar.header("📊 Performance Analysis")
st.sidebar.write("""
1. **Select Counties**: Use the dropdown to select multiple counties for analysis.
2. **Random Selection**: Click "Select Random 25 Counties" if you want to let the system choose for you.
3. **Run Analysis**: After selecting counties, click "Run Performance Analysis" to see the results.
""")

# Button to randomly select 25 counties outside the form
if st.button("Select Random 25 Counties"):
    st.session_state["selected_counties"] = random.sample(list(data['County_State'].unique()), 25)

# Sidebar for County and State selection within a form
with st.sidebar.form(key="county_selection_form"):
    selected_counties_states = st.multiselect(
        "Select County, State combinations", 
        options=data['County_State'].unique(),
        default=st.session_state["selected_counties"],
        help="Choose multiple counties to evaluate their relative performance in managing environmental and health outcomes."
    )
    
    submit_button = st.form_submit_button(label="Run Performance Analysis")

# Main content
if submit_button and selected_counties_states:
    st.markdown("## Performance Analysis Results")
    st.write("""
    The results below show the performance scores for each selected county. 
    A performance score close to or equal to 1 indicates that a county is effectively managing its environmental burdens, social vulnerabilities, and health outcomes relative to other selected counties.
    """)

    # Filter the data to only include the selected counties
    filtered_data = data[data['County_State'].isin(selected_counties_states)]
    
    # Extract input and output measures from dea_measures
    input_measures = []
    for category in dea_measures["inputs"].values():
        input_measures.extend(category.keys())

    output_measures = []
    for category in dea_measures["outputs"].values():
        output_measures.extend(category.keys())

    # Select only the columns that are needed for the performance analysis
    columns_to_average = input_measures + output_measures

    # Average the input and output measures for each DMU (county_state)
    grouped_data = filtered_data.groupby('County_State')[columns_to_average].mean()

    # Replace zeros with a small positive value
    grouped_data.replace(0, 1e-6, inplace=True)

    # Verify and normalize input/output measures
    for col in columns_to_average:
        grouped_data[col] = grouped_data[col].apply(lambda x: max(1e-6, min(1, x / 100.0)))

    # Extract the input and output data after normalization
    input_data = grouped_data[input_measures].values
    output_data = grouped_data[output_measures].values
    dmu_labels = grouped_data.index.values

    # Perform DEA using the custom DEA class
    dea = DEA(inputs=input_data, outputs=output_data)
    dea.name_units(dmu_labels)
    dea.fit()

    # Structure the outputs
    # 1. Performance Scores Table
    performance_df = pd.DataFrame({
        "County_State": dmu_labels,
        "Performance Score": dea.efficiency.flatten()
    })

    # Consider scores >= 0.95 as high-performing
    performance_df["Status"] = np.where(performance_df["Performance Score"] >= 0.95, "High-Performing", "Needs Improvement")

    # Display Performance Scores in a visually pleasing way
    st.markdown("### Performance Scores")
    st.write("""
    Counties with a performance score close to or equal to 1 are effectively managing environmental burdens and promoting health outcomes. 
    Counties with lower scores may need to enhance their efforts in these areas.
    """)
    
    cols = st.columns(3)
    for i, row in performance_df.iterrows():
        with cols[i % 3]:
            color = "green" if row["Status"] == "High-Performing" else "red"
            st.markdown(f"""
            <div style="border: 1px solid #ddd; border-radius: 8px; padding: 20px; background-color: #f9f9f9; text-align: center; margin-bottom: 15px;">
                <h4 style="color: {color};">{row["County_State"]}</h4>
                <p>Performance Score: <span style="color: {color}; font-size: 24px;">{row["Performance Score"]:.4f}</span></p>
                <p style="font-size: 14px;">Status: {row["Status"]}</p>
            </div>
            """, unsafe_allow_html=True)

    # 2. Summary of Results
    st.markdown("### Summary of Performance Results")
    num_high_performing = np.sum(performance_df["Status"] == "High-Performing")
    num_needs_improvement = len(dmu_labels) - num_high_performing
    st.write(f"**Number of High-Performing Counties:** {num_high_performing}")
    st.write(f"**Number of Counties Needing Improvement:** {num_needs_improvement}")

else:
    st.markdown("## Instructions")
    st.write("""
    To begin the performance analysis:
    1. Select one or more counties from the sidebar, or click 'Select Random 25 Counties' to automatically choose a subset of counties.
    2. After making your selection, click 'Run Performance Analysis' to see the results.
    The analysis will compare the performance of these counties in handling environmental burdens, social vulnerabilities, and health outcomes.
    """)

