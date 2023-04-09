import pandas as pd
import requests
import io

# Replace these URLs with the actual URLs of your data sources
url_ons = "https://example.com/ons_data.csv"
url_gla = "https://example.com/gla_data.csv"
url_numbeo = "https://example.com/numbeo_data.csv"

# Read data from the sources
ons_data = pd.read_csv(io.StringIO(requests.get(url_ons).text))
gla_data = pd.read_csv(io.StringIO(requests.get(url_gla).text))
numbeo_data = pd.read_csv(io.StringIO(requests.get(url_numbeo).text))

# Clean and preprocess the data
# This step depends on the structure and format of the datasets you collect
# Perform tasks like removing duplicates, handling missing values, converting units, etc.

# Merge the data into a single DataFrame
merged_data = ons_data.merge(gla_data, on='year').merge(numbeo_data, on='year')

# Calculate the Cost of Living Index (CLI)
# Replace the column names with the actual names from your datasets
merged_data['costOfLivingIndex'] = merged_data.apply(lambda row: (row['column_1'] + row['column_2'] + row['column_3']) / 3, axis=1)

# Export the data to a CSV file
merged_data[['year', 'costOfLivingIndex']].to_csv('line.csv', index=False)

# Generate synthetic data for scatter.csv
num_samples = 100
years = np.random.randint(2000, 2022, size=num_samples)
x_values = np.random.rand(num_samples) * 100
y_values = np.random.rand(num_samples) * 100

scatter_data = pd.DataFrame({
    'year': years,
    'xValue': x_values,
    'yValue': y_values
})

scatter_data.to_csv('scatter.csv', index=False)

# Generate synthetic data for bar.csv
num_years = 10
categories = ['category_1', 'category_2', 'category_3']

bar_data = pd.DataFrame({
    'year': range(2010, 2010 + num_years)
})

for category in categories:
    bar_data[category] = np.random.randint(10, 100, size=num_years)

bar_data.to_csv('bar.csv', index=False)