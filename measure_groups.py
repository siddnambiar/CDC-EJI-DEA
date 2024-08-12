# DEA Measures
dea_measures = {
    "inputs": {
        "Environmental Burden": {
            "EPL_OZONE": "Ozone Percentile (Higher values indicate more days above O3 standard)",
            "EPL_PM": "Particulate Matter Percentile (Higher values indicate more days above PM2.5 standard)",
            "EPL_DSLPM": "Diesel Particulate Matter Percentile (Higher values indicate higher concentrations)",
            "EPL_TOTCR": "Total Cancer Risk Percentile (Higher values indicate higher cancer risk)",
            "EPL_NPL": "Proximity to National Priority List Sites (Higher values indicate closer proximity)",
            "EPL_TRI": "Proximity to Toxic Release Inventory Sites (Higher values indicate closer proximity)",
            "EPL_TSD": "Proximity to Treatment, Storage, and Disposal Sites (Higher values indicate closer proximity)",
            "EPL_RMP": "Proximity to Risk Management Plan Sites (Higher values indicate closer proximity)"
        },
        "Social Vulnerability": {
            "EPL_MINRTY": "Minority Population Percentile (Higher values indicate higher minority population)",
            "EPL_POV200": "Below 200% Poverty Line Percentile (Higher values indicate more poverty)",
            "EPL_NOHSDP": "No High School Diploma Percentile (Higher values indicate more without diplomas)",
            "EPL_UNEMP": "Unemployment Percentile (Higher values indicate higher unemployment)",
            "EPL_RENTER": "Renter Population Percentile (Higher values indicate more renters)"
        }
    },
    "outputs": {
        "Health and Environmental Outcomes": {
            "EPL_PARK": "Proximity to Green Spaces (Higher values indicate closer proximity)",
            "EPL_WLKIND": "Walkability Index (Higher values indicate better walkability)"
        }
    }
}

# EJI Percentile Measures for Risk Scorecard
eji_percentile_measures = {
    "Environmental Burden": {
        "EPL_OZONE": {
            "description": "Ozone Percentile",
            "context": "Higher values indicate more days above O3 standard",
            "higher_is": "bad"
        },
        "EPL_PM": {
            "description": "Particulate Matter Percentile",
            "context": "Higher values indicate more days above PM2.5 standard",
            "higher_is": "bad"
        },
        "EPL_DSLPM": {
            "description": "Diesel Particulate Matter Percentile",
            "context": "Higher values indicate higher concentrations",
            "higher_is": "bad"
        },
        "EPL_TOTCR": {
            "description": "Total Cancer Risk Percentile",
            "context": "Higher values indicate higher cancer risk",
            "higher_is": "bad"
        },
        "EPL_NPL": {
            "description": "Proximity to National Priority List Sites",
            "context": "Higher values indicate closer proximity",
            "higher_is": "bad"
        },
        "EPL_TRI": {
            "description": "Proximity to Toxic Release Inventory Sites",
            "context": "Higher values indicate closer proximity",
            "higher_is": "bad"
        },
        "EPL_TSD": {
            "description": "Proximity to Treatment, Storage, and Disposal Sites",
            "context": "Higher values indicate closer proximity",
            "higher_is": "bad"
        },
        "EPL_RMP": {
            "description": "Proximity to Risk Management Plan Sites",
            "context": "Higher values indicate closer proximity",
            "higher_is": "bad"
        },
        "EPL_COAL": {
            "description": "Proximity to Coal Mines",
            "context": "Higher values indicate closer proximity",
            "higher_is": "bad"
        },
        "EPL_LEAD": {
            "description": "Proximity to Lead Mines",
            "context": "Higher values indicate closer proximity",
            "higher_is": "bad"
        },
        "EPL_PARK": {
            "description": "Proximity to Green Spaces",
            "context": "Higher values indicate closer proximity",
            "higher_is": "good"
        },
        "EPL_HOUAGE": {
            "description": "Housing Age (Lead Exposure)",
            "context": "Higher values indicate more older houses",
            "higher_is": "bad"
        },
        "EPL_WLKIND": {
            "description": "Walkability Index",
            "context": "Higher values indicate better walkability",
            "higher_is": "good"
        },
        "EPL_RAIL": {
            "description": "Proximity to Railroads",
            "context": "Higher values indicate closer proximity",
            "higher_is": "bad"
        },
        "EPL_ROAD": {
            "description": "Proximity to Highways",
            "context": "Higher values indicate closer proximity",
            "higher_is": "bad"
        },
        "EPL_AIRPRT": {
            "description": "Proximity to Airports",
            "context": "Higher values indicate closer proximity",
            "higher_is": "bad"
        },
        "EPL_IMPWTR": {
            "description": "Proximity to Impaired Waters",
            "context": "Higher values indicate closer proximity",
            "higher_is": "bad"
        }
    },
    "Social Vulnerability": {
        "EPL_MINRTY": {
            "description": "Minority Population Percentile",
            "context": "Higher values indicate higher minority population",
            "higher_is": "neutral"
        },
        "EPL_POV200": {
            "description": "Below 200% Poverty Line Percentile",
            "context": "Higher values indicate more poverty",
            "higher_is": "bad"
        },
        "EPL_NOHSDP": {
            "description": "No High School Diploma Percentile",
            "context": "Higher values indicate more without diplomas",
            "higher_is": "bad"
        },
        "EPL_UNEMP": {
            "description": "Unemployment Percentile",
            "context": "Higher values indicate higher unemployment",
            "higher_is": "bad"
        },
        "EPL_RENTER": {
            "description": "Renter Population Percentile",
            "context": "Higher values indicate more renters",
            "higher_is": "neutral"
        },
        "EPL_HOUBDN": {
            "description": "Housing Burden Percentile",
            "context": "Higher values indicate more burdened households",
            "higher_is": "bad"
        },
        "EPL_UNINSUR": {
            "description": "Uninsured Population Percentile",
            "context": "Higher values indicate more uninsured",
            "higher_is": "bad"
        },
        "EPL_NOINT": {
            "description": "No Internet Access Percentile",
            "context": "Higher values indicate less internet access",
            "higher_is": "bad"
        },
        "EPL_AGE65": {
            "description": "Population Age 65+ Percentile",
            "context": "Higher values indicate more elderly population",
            "higher_is": "neutral"
        },
        "EPL_AGE17": {
            "description": "Population Age 17- Percentile",
            "context": "Higher values indicate more youth population",
            "higher_is": "neutral"
        },
        "EPL_DISABL": {
            "description": "Disability Population Percentile",
            "context": "Higher values indicate more disabilities",
            "higher_is": "bad"
        },
        "EPL_LIMENG": {
            "description": "Limited English Proficiency Percentile",
            "context": "Higher values indicate more language barriers",
            "higher_is": "bad"
        },
        "EPL_MOBILE": {
            "description": "Mobile Homes Percentile",
            "context": "Higher values indicate more mobile homes",
            "higher_is": "neutral"
        },
        "EPL_GROUPQ": {
            "description": "Group Quarters Population Percentile",
            "context": "Higher values indicate more group quarters",
            "higher_is": "neutral"
        }
    },
    "Health Vulnerability": {
        "EPL_BPHIGH": {
            "description": "High Blood Pressure Percentile",
            "context": "Higher values indicate more high blood pressure",
            "higher_is": "bad"
        },
        "EPL_ASTHMA": {
            "description": "Asthma Percentile",
            "context": "Higher values indicate more asthma cases",
            "higher_is": "bad"
        },
        "EPL_CANCER": {
            "description": "Cancer Percentile",
            "context": "Higher values indicate more cancer cases",
            "higher_is": "bad"
        },
        "EPL_DIABETES": {
            "description": "Diabetes Percentile",
            "context": "Higher values indicate more diabetes cases",
            "higher_is": "bad"
        },
        "EPL_MHLTH": {
            "description": "Mental Health Percentile",
            "context": "Higher values indicate more mental health issues",
            "higher_is": "bad"
        }
    }
}