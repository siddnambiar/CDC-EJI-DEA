import pandas as pd
import numpy as np
import random
from envelopment import DEA  # Importing the DEA class from envelopment.py
from measure_groups import dea_measures  # Importing measures from measure_groups.py

# Load the data
data = pd.read_csv('CDC_EJI_US.csv')

# Create a unique identifier for County and State combination
data['County_State'] = data['COUNTY'] + ", " + data['StateDesc']

# Randomly select a few counties
random.seed(42)  # For reproducibility
selected_counties_states = random.sample(list(data['County_State'].unique()), 25)  # Select 5 random counties

# Filter the data to only include the selected counties
filtered_data = data[data['County_State'].isin(selected_counties_states)]

# Extract input and output measures from dea_measures
input_measures = []
for category in dea_measures["inputs"].values():
    input_measures.extend(category.keys())

output_measures = []
for category in dea_measures["outputs"].values():
    output_measures.extend(category.keys())

# Select only the columns that are needed for the DEA analysis
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
# 1. Efficiency Scores Table
efficiency_df = pd.DataFrame({
    "County_State": dmu_labels,
    "Efficiency Score": dea.efficiency.flatten()
})

# Consider scores >= 0.95 as efficient
efficiency_df["Status"] = np.where(efficiency_df["Efficiency Score"] >= 0.99, "Efficient", "Inefficient")

print("Efficiency Scores:")
print(efficiency_df.to_string(index=False))

# 2. Reference Sets
print("\nReference Sets:")
reference_sets = dea.lambdas
for i, dmu in enumerate(dmu_labels):
    references = [dmu_labels[j] for j in range(len(dmu_labels)) if reference_sets[j] > 0]
    print(f"{dmu}: {', '.join(references) if references else 'No references (efficient)'}")

# 3. Summary of Results
num_efficient = np.sum(efficiency_df["Status"] == "Efficient")
num_inefficient = len(dmu_labels) - num_efficient
print("\nSummary of DEA Results:")
print(f"Number of Efficient DMUs: {num_efficient}")
print(f"Number of Inefficient DMUs: {num_inefficient}")
