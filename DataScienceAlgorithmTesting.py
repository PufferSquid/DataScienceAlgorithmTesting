import DataScienceAlgorithmTesting
import pandas as pd

# Load the 'in' sheet from the Excel file into a DataFrame
df = pd.read_excel('241003 Assignment Data (2025).xlsx', sheet_name='in')

# Display the first few rows to verify
print(df.head())

# Optional: Clean or prepare the data (e.g., convert 'Time' to numeric if needed)
df['Time'] = pd.to_numeric(df['Time'], errors='coerce')



# Display results
print("\nDataFrame:")
print(df.head())
