import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from measure_groups import eji_percentile_measures  # Import the EJI percentile measures

st.set_page_config(page_title="County Comparison - CDC EJI Explorer", page_icon="📊", layout="wide")
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar for Navigation
st.sidebar.header("📊 County Comparison")
st.sidebar.write("Use this page to compare Environmental Justice Index (EJI) data across multiple counties and states.")

# Load the data
@st.cache_data
def load_data():
    return pd.read_csv('CDC_EJI_US.csv')

data = load_data()

# Create a unique identifier for County and State combination
data['County_State'] = data['COUNTY'] + ", " + data['StateDesc']

# User Selection for State
st.sidebar.subheader("Select States")
st.sidebar.write("Choose one or more states to filter the available counties.")
state_options = data['StateDesc'].unique()
selected_states = st.sidebar.multiselect(
    "Select States", 
    options=state_options, 
    help="Selecting a state will filter the counties to those within the selected states."
)

# Filter data by selected states
if selected_states:
    filtered_data_by_state = data[data['StateDesc'].isin(selected_states)]
else:
    filtered_data_by_state = data

# User Selection for County and State
st.sidebar.subheader("Select Counties and States")
st.sidebar.write("Choose one or more counties and states to explore and compare their EJI data.")
county_state_options = filtered_data_by_state['County_State'].unique()
selected_counties_states = st.sidebar.multiselect(
    "Select County, State combinations", 
    options=county_state_options, 
    help="Select multiple counties to view a side-by-side comparison."
)

# Measure group selection in sidebar
st.sidebar.subheader("Select a Measure Group")
st.sidebar.write("Choose a measure group and a specific measure to compare across the selected counties.")
measure_group = st.sidebar.selectbox("Measure Group", options=list(eji_percentile_measures.keys()))
measure = st.sidebar.selectbox(
    "Measure", 
    options=list(eji_percentile_measures[measure_group].keys()), 
    format_func=lambda x: eji_percentile_measures[measure_group][x]['description']
)

# Main content
if selected_counties_states:
    st.markdown("## County Comparison Overview")
    st.write("""
        This page allows you to compare population distribution and selected Environmental Justice Index (EJI) percentile measures across multiple counties and states. 
        The EJI percentile measures are standardized scores that rank the relative standing of each area on specific environmental, social, and health vulnerability indicators.
    """)

    filtered_data = data[data['County_State'].isin(selected_counties_states)]
    
    # Calculate totals and averages
    total_population = filtered_data.groupby('County_State')['E_TOTPOP'].sum().reset_index()
    percentile_cols = list(eji_percentile_measures[measure_group].keys())
    percentile_means = filtered_data.groupby('County_State')[percentile_cols].mean().reset_index()

    # Convert mean percentile values to percentages (0-100)
    percentile_means[percentile_cols] = percentile_means[percentile_cols] * 100
    
    # Check for invalid data
    invalid_data = any(percentile_means[measure] < 0)

    # Merge results for visualization
    result_data = pd.merge(total_population, percentile_means, on='County_State')

    # Display pie chart for total population in a container with border
    with st.container(border=True):
        st.markdown("<h2 style='color: #007bff;'>Population Distribution</h2>", unsafe_allow_html=True)
        st.write("This pie chart illustrates the total population distribution across the selected counties. It helps you understand the relative population sizes of the regions you’re comparing.")
        
        # Generate colors for the pie chart
        cmap = plt.get_cmap('PuBu')
        colors = cmap(np.linspace(0, 1, len(result_data)))

        def autopct_format(pct, allvals):
            absolute = int(np.round(pct/100.*np.sum(allvals)))
            return f"{absolute:,} ({pct:.1f}%)"

        fig, ax = plt.subplots()
        wedges, texts, autotexts = ax.pie(
            result_data['E_TOTPOP'], labels=result_data['County_State'], autopct=lambda pct: autopct_format(pct, result_data['E_TOTPOP']),
            startangle=90, colors=colors
        )
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.setp(autotexts, size=10, weight="bold")
        st.pyplot(fig)

    # Display horizontal bar chart for selected measure in a container with border
    if not invalid_data:
        with st.container(border=True):
            st.markdown("<h2 style='color: #007bff;'>Percentile Measure Comparison</h2>", unsafe_allow_html=True)
            st.write(f"""
                This bar chart compares the selected measure, **{eji_percentile_measures[measure_group][measure]['description']}**, across the selected counties.
                Percentile scores range from 0 to 100 and represent the relative standing of each county on this measure:
            """)
            st.write(f"""
                - **High percentile values** (closer to 100%) often indicate greater exposure to environmental burdens, higher social vulnerability, or greater health risks, depending on the context of the measure.
                - **Low percentile values** (closer to 0%) often indicate lesser exposure to environmental burdens, lower social vulnerability, or fewer health risks.
            """)
            st.write(f"""
                For the selected measure, **{eji_percentile_measures[measure_group][measure]['description']}**, higher values are generally considered **{eji_percentile_measures[measure_group][measure]['higher_is']}**. 
                { 'Higher values may indicate increased risk or burden, which is concerning for communities.' if eji_percentile_measures[measure_group][measure]['higher_is'] == 'bad' else 'Higher values may indicate better conditions or resilience, which is beneficial for communities.'}
            """)

            fig, ax = plt.subplots()
            result_data = result_data.sort_values(by=measure, ascending=False)
            ax.barh(result_data['County_State'], result_data[measure], color='teal')
            ax.set_xlabel(f'{eji_percentile_measures[measure_group][measure]["description"]} (%)')
            ax.set_ylabel('County, State')
            ax.invert_yaxis()  # Invert y-axis to have the highest values at the top
            st.pyplot(fig)
    else:
        with st.container(border=True):
            st.markdown("<h2 style='color: #007bff;'>Percentile Measure Comparison</h2>", unsafe_allow_html=True)
            st.write("The data for the selected measure group may be invalid or unavailable and is not displayed.")
else:
    st.markdown("## Instructions")
    st.write("To begin your analysis, please select one or more states and counties from the sidebar. You can then choose a measure group and specific measure to compare across these counties.")
