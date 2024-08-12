import streamlit as st
import pandas as pd
import plotly.express as px
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
    st.write("This page allows you to compare population distribution and selected EJI percentile measures across multiple counties and states. Use the visualizations below to analyze differences and similarities among the selected regions.")

    filtered_data = data[data['County_State'].isin(selected_counties_states)]
    
    # Calculate totals and averages
    total_population = filtered_data.groupby('County_State')['E_TOTPOP'].sum().reset_index()
    percentile_cols = list(eji_percentile_measures[measure_group].keys())
    percentile_means = filtered_data.groupby('County_State')[percentile_cols].mean().reset_index()
    
    # Check for invalid data
    invalid_data = any(percentile_means[measure] < 0)

    # Merge results for visualization
    result_data = pd.merge(total_population, percentile_means, on='County_State')
    
    # Display pie chart for total population in a container with border
    with st.container(border=True):
        st.markdown("<h2 style='color: #007bff;'>Population Distribution</h2>", unsafe_allow_html=True)
        st.write("This pie chart illustrates the total population distribution across the selected counties. It helps you understand the relative population sizes of the regions you’re comparing.")
        fig_pie = px.pie(
            result_data, 
            values='E_TOTPOP', 
            names='County_State', 
            title='',
            color_discrete_sequence=px.colors.sequential.PuBu,
            labels={'E_TOTPOP': 'Population'},
            hover_data={'E_TOTPOP': True},
            hole=0.3
        )
        fig_pie.update_traces(textinfo='percent+label')
        st.plotly_chart(fig_pie, use_container_width=True)

    # Display horizontal bar chart for selected measure in a container with border
    if not invalid_data:
        with st.container(border=True):
            st.markdown("<h2 style='color: #007bff;'>Percentile Measure Comparison</h2>", unsafe_allow_html=True)
            st.write(f"This bar chart compares the selected measure, **{eji_percentile_measures[measure_group][measure]['description']}**, across the selected counties.")
            st.write(f"**Context:** {eji_percentile_measures[measure_group][measure]['context']}. Higher values are generally considered **{eji_percentile_measures[measure_group][measure]['higher_is']}**.")
            fig_bar = px.bar(
                result_data.sort_values(by=measure, ascending=False), 
                x=measure, 
                y='County_State', 
                orientation='h',
                labels={'County_State': 'County, State', measure: eji_percentile_measures[measure_group][measure]['description']},
                color_discrete_sequence=px.colors.sequential.Teal
            )
            st.plotly_chart(fig_bar, use_container_width=True)
    else:
        with st.container(border=True):
            st.markdown("<h2 style='color: #007bff;'>Percentile Measure Comparison</h2>", unsafe_allow_html=True)
            st.write("The data for the selected measure group may be invalid or unavailable and is not displayed.")
else:
    st.markdown("## Instructions")
    st.write("To begin your analysis, please select one or more states and counties from the sidebar. You can then choose a measure group and specific measure to compare across these counties.")
