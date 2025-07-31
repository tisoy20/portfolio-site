import pandas as pd  # pandas is the go-to library for working with tabular data like spreadsheets or CSVs

# Step 1: Load the messy CSV file
df = pd.read_csv('messy_data.csv')  # This reads the file into a DataFrame (basically a table in Python)

# Step 2: Clean column names (e.g., remove spaces and make lowercase)
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]  
# We're using a list comprehension to loop through all column names and tidy them

# Step 3: Fill missing values with a placeholder
df.fillna('N/A', inplace=True)  
# This replaces any empty cells with 'N/A' so nothing gets lost

# Step 4: Save the cleaned data into a new CSV file
df.to_csv('cleaned_data.csv', index=False)  
# index=False tells pandas not to add row numbers to the saved file

print("✅ Data cleaning complete! Saved as cleaned_data.csv")