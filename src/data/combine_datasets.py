import pandas as pd

# Load the CSV file into a DataFrame
file_path = '2014_output.csv'
df = pd.read_csv(file_path)

# Drop rows where the "Name" column is empty
df.dropna(subset=['Name'], inplace=True)

# Write the modified DataFrame back to a CSV file
df.to_csv('modified_file.csv', index=False)
