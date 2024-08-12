import streamlit as st

# Set page configuration for a light-themed app
st.set_page_config(page_title="CDC EJI Dashboard", page_icon="🌍", layout="wide")
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# Main Title and Welcome Message
st.title("🌍 Welcome to the CDC Environmental Justice Index Dashboard")

st.write("""
The **Environmental Justice Index (EJI)** by the CDC is a powerful tool that measures the cumulative impacts of environmental burdens on health, with a focus on promoting health equity across communities in the United States. 
This interactive dashboard allows you to delve into these important metrics, providing a platform for exploring and understanding how various environmental, social, and health factors intersect to influence the well-being of communities nationwide.
""")

# Enhanced Call to Action
st.markdown("""
### 🌟 **Take Action with Data-Driven Insights**
This dashboard is designed to empower you with the information needed to address environmental justice issues in your community. 
- **Explore** various facets of environmental justice.
- **Analyze** the data to uncover patterns and disparities.
- **Understand** the impacts on community health and resilience.

Whether you’re a researcher, policymaker, or community advocate, this tool provides the insights necessary to make informed decisions and drive positive change.
""")

# Sidebar for Navigation
st.sidebar.header("📂 Navigation")
st.sidebar.write("""
Navigate through the app using the sidebar. Here’s what you can explore:
- **Home:** An overview of the dashboard and its purpose.
- **EJI Overview:** Learn about the Environmental Justice Index, its components, and key concepts.
- **County Comparison:** Compare EJI measures across multiple counties and states.
- **Risk Scorecard:** View detailed risk assessments for a selected county and state.
""")

# Concluding Statement on Home Page
st.markdown("""
### Why Environmental Justice Matters
Environmental justice is about ensuring that all communities, especially those historically marginalized, are treated fairly with respect to environmental laws, regulations, and policies. 
By using this dashboard, you’re taking the first step towards understanding and addressing the critical environmental health disparities that impact the most vulnerable populations. 
Let’s work together to promote health equity and protect the environment for everyone.
""")

# Link to CDC EJI Website
st.markdown("""
For more information, visit the [CDC Environmental Justice Index (EJI) website](https://www.atsdr.cdc.gov/placeandhealth/eji/index.html).
""")
