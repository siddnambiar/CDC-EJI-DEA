import streamlit as st
st.markdown("""
    <style>
    .container {
        padding: 20px;
        border-radius: 10px;
        background-color: #ffffff;
        border: 1px solid #ddd;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    }
    h3 {
        color: #007bff;
    }
    ul {
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🌍 CDC Environmental Justice Index (EJI) Overview")

# Sidebar for Description Page Navigation
st.sidebar.header("📄 Description Page")
st.sidebar.write("Learn about the EJI, its components, and key concepts.")

# Description Section with Enhanced Styling and Additional Context
st.markdown("### Key Concepts")
st.write(
    """
    - **Environmental Justice (EJ):** Fair treatment and meaningful involvement of all people, regardless of race, color, national origin, or income, with respect to environmental laws, regulations, and policies.
    - **Cumulative Impacts:** The combined effects of multiple environmental burdens, social stressors, and existing health conditions that can exacerbate health disparities.
    - **Health Equity:** The attainment of the highest level of health for all people, emphasizing the elimination of health disparities and providing everyone with a fair opportunity to achieve good health.
    """
)

st.markdown("### The EJI uses indicators across three primary modules:")
st.write(
    """
    - **Environmental Burden:** Measures environmental exposures, such as air and water quality, proximity to hazardous sites, and pollution levels.
    - **Social Vulnerability:** Assesses social factors like poverty, housing conditions, and access to health care that can influence community resilience to environmental hazards.
    - **Health Vulnerability:** Captures pre-existing health conditions that make certain populations more susceptible to environmental stressors.
    """
)
