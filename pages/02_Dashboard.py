import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 CDC EJI Data Dashboard")

# Sidebar for Dashboard Navigation
st.sidebar.header("📊 Dashboard Page")
st.sidebar.write("Explore and visualize EJI data interactively.")

# Load the data
@st.cache_data
def load_data():
    return pd.read_csv('CDC_EJI_US.csv')

data = load_data()

# Create a unique identifier for County and State combination
data['County_State'] = data['COUNTY'] + ", " + data['StateDesc']

# User Selection for County and State
county_state_options = data['County_State'].unique()
selected_counties_states = st.multiselect("Select County, State combinations", options=county_state_options, help="Choose one or more counties to explore their data.")

if selected_counties_states:
    filtered_data = data[data['County_State'].isin(selected_counties_states)]
    
    # Calculate totals and averages
    total_population = filtered_data.groupby('County_State')['E_TOTPOP'].sum().reset_index()
    percentile_cols = [col for col in filtered_data.columns if col.startswith('EPL_') or col.startswith('RPL_') or col.startswith('SPL_')]
    percentile_means = filtered_data.groupby('County_State')[percentile_cols].mean().reset_index()
    
    # Merge results for visualization
    result_data = pd.merge(total_population, percentile_means, on='County_State')
    
    # Display pie chart for total population
    st.markdown("<h2 style='color: #007bff;'>Total Population Distribution</h2>", unsafe_allow_html=True)
    fig_pie = px.pie(result_data, values='E_TOTPOP', names='County_State', color_discrete_sequence=px.colors.sequential.Blues)
    st.plotly_chart(fig_pie, use_container_width=True)
    
    # Measure group selection
    measure_groups = {
        'Environmental Burden': {
            'EPL_OZONE': 'Ozone Percentile (Higher values indicate more days above O3 standard)',
            'EPL_PM': 'Particulate Matter Percentile (Higher values indicate more days above PM2.5 standard)',
            'EPL_DSLPM': 'Diesel Particulate Matter Percentile (Higher values indicate higher concentrations)',
            'EPL_TOTCR': 'Total Cancer Risk Percentile (Higher values indicate higher cancer risk)',
            'EPL_NPL': 'Proximity to National Priority List Sites (Higher values indicate closer proximity)',
            'EPL_TRI': 'Proximity to Toxic Release Inventory Sites (Higher values indicate closer proximity)',
            'EPL_TSD': 'Proximity to Treatment, Storage, and Disposal Sites (Higher values indicate closer proximity)',
            'EPL_RMP': 'Proximity to Risk Management Plan Sites (Higher values indicate closer proximity)',
            'EPL_COAL': 'Proximity to Coal Mines (Higher values indicate closer proximity)',
            'EPL_LEAD': 'Proximity to Lead Mines (Higher values indicate closer proximity)',
            'EPL_PARK': 'Proximity to Green Spaces (Higher values indicate closer proximity)',
            'EPL_HOUAGE': 'Housing Age (Lead Exposure) (Higher values indicate more older houses)',
            'EPL_WLKIND': 'Walkability Index (Higher values indicate better walkability)',
            'EPL_RAIL': 'Proximity to Railroads (Higher values indicate closer proximity)',
            'EPL_ROAD': 'Proximity to Highways (Higher values indicate closer proximity)',
            'EPL_AIRPRT': 'Proximity to Airports (Higher values indicate closer proximity)',
            'EPL_IMPWTR': 'Proximity to Impaired Waters (Higher values indicate closer proximity)'
        },
        'Social Vulnerability': {
            'EPL_MINRTY': 'Minority Population Percentile (Higher values indicate higher minority population)',
            'EPL_POV200': 'Below 200% Poverty Line Percentile (Higher values indicate more poverty)',
            'EPL_NOHSDP': 'No High School Diploma Percentile (Higher values indicate more without diplomas)',
            'EPL_UNEMP': 'Unemployment Percentile (Higher values indicate higher unemployment)',
            'EPL_RENTER': 'Renter Population Percentile (Higher values indicate more renters)',
            'EPL_HOUBDN': 'Housing Burden Percentile (Higher values indicate more burdened households)',
            'EPL_UNINSUR': 'Uninsured Population Percentile (Higher values indicate more uninsured)',
            'EPL_NOINT': 'No Internet Access Percentile (Higher values indicate less internet access)',
            'EPL_AGE65': 'Population Age 65+ Percentile (Higher values indicate more elderly population)',
            'EPL_AGE17': 'Population Age 17- Percentile (Higher values indicate more youth population)',
            'EPL_DISABL': 'Disability Population Percentile (Higher values indicate more disabilities)',
            'EPL_LIMENG': 'Limited English Proficiency Percentile (Higher values indicate more language barriers)',
            'EPL_MOBILE': 'Mobile Homes Percentile (Higher values indicate more mobile homes)',
            'EPL_GROUPQ': 'Group Quarters Population Percentile (Higher values indicate more group quarters)'
        },
        'Health Vulnerability': {
            'EPL_BPHIGH': 'High Blood Pressure Percentile (Higher values indicate more high blood pressure)',
            'EPL_ASTHMA': 'Asthma Percentile (Higher values indicate more asthma cases)',
            'EPL_CANCER': 'Cancer Percentile (Higher values indicate more cancer cases)',
            'EPL_DIABETES': 'Diabetes Percentile (Higher values indicate more diabetes cases)',
            'EPL_MHLTH': 'Mental Health Percentile (Higher values indicate more mental health issues)'
        }
    }

    
    st.markdown("<h2 style='color: #007bff;'>Percentile Measures</h2>", unsafe_allow_html=True)
    measure_group = st.selectbox("Select a measure group", options=list(measure_groups.keys()))
    measure = st.selectbox("Select a measure to compare", options=list(measure_groups[measure_group].keys()), format_func=lambda x: measure_groups[measure_group][x])
    
    # Display bar chart for selected measure
    fig_bar = px.bar(result_data, x='County_State', y=measure, title='', labels={'County_State': 'County, State', measure: measure_groups[measure_group][measure]}, color_discrete_sequence=px.colors.sequential.Teal)
    st.plotly_chart(fig_bar, use_container_width=True)