import pandas as pd

# Load data from an Excel file into a DataFrame
excel_file = "googleplaystore.xlsx"  # Replace with the path to your Excel file
df = pd.read_excel(excel_file)

# Now you can work with the data in the DataFrame
# For example, you can print the first few rows of the DataFrame:
print(df.head())



