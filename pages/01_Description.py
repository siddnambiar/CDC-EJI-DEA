import streamlit as st

st.set_page_config(page_title="EJI Overview - CDC EJI Explorer", page_icon="🌍", layout="wide")
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
st.title("🌍 CDC Environmental Justice Index (EJI) Overview")

# Sidebar for Description Page Navigation
st.sidebar.header("📄 About the EJI")
st.sidebar.write("Explore the key concepts, components, and methodology of the Environmental Justice Index.")

# Introduction Section
st.markdown("## Introduction")
st.write("""
The **CDC Environmental Justice Index (EJI)** is a groundbreaking tool designed to help identify and address the impacts of environmental injustices in communities across the United States. 
It provides a comprehensive assessment of how environmental burdens, social vulnerabilities, and health conditions combine to affect community well-being. 
The EJI is an essential resource for policymakers, researchers, and community leaders aiming to advance health equity and environmental justice.
""")

st.markdown("""
For more detailed information, visit the [CDC Environmental Justice Index (EJI) website](https://www.atsdr.cdc.gov/placeandhealth/eji/index.html).
""")

# Key Concepts Section
st.markdown("## Key Concepts")
st.write("""
Understanding the core principles behind the EJI is essential for interpreting its findings and applying them effectively. Below are the key concepts that underpin the EJI:
""")
st.markdown("""
- **Environmental Justice (EJ):** The fair treatment and meaningful involvement of all people, regardless of race, color, national origin, or income, with respect to the development, implementation, and enforcement of environmental laws, regulations, and policies.
- **Cumulative Impacts:** The total, combined effects of multiple environmental burdens, social stressors, and existing health disparities that can amplify risks and adverse outcomes in affected communities.
- **Health Equity:** The pursuit of eliminating disparities in health and ensuring that everyone has the opportunity to achieve their highest level of health, regardless of their social or economic circumstances.
""")

# EJI Modules Section
st.markdown("## EJI Modules")
st.write("""
The EJI is structured around three primary modules, each capturing different dimensions of environmental justice:
""")

st.markdown("""
- **Environmental Burden:** This module quantifies environmental exposures such as air and water quality, proximity to hazardous waste sites, and levels of pollution. These factors are critical in understanding the physical environmental risks that communities face.
  
- **Social Vulnerability:** This module assesses social factors including poverty, housing quality, and access to health care. These elements are vital in determining a community's ability to respond to and recover from environmental hazards.

- **Health Vulnerability:** This module measures pre-existing health conditions and disparities that make certain populations more susceptible to environmental stressors. Understanding these vulnerabilities helps in identifying populations at greater risk.
""")

# Concluding Remarks
st.markdown("## Using the EJI for Action")
st.write("""
The EJI is not just a data tool—it’s a catalyst for change. By highlighting areas where environmental justice is lacking, the EJI supports targeted interventions that promote health equity and environmental resilience. 
Communities, organizations, and governments can use the insights from the EJI to make informed decisions, prioritize resources, and advocate for policies that protect vulnerable populations.
""")

st.markdown("""
Visit the [CDC Environmental Justice Index (EJI) website](https://www.atsdr.cdc.gov/placeandhealth/eji/index.html) to explore the full scope of the index and access additional resources.
""")
