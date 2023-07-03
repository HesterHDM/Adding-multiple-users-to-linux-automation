import pandas as pd

# Load the Excel file
excel_file = 'users.xlsx'
df = pd.read_excel(excel_file)

# Convert DataFrame to a text file
text_file = 'users.txt'
df.to_csv(text_file, sep='\t', index=False)

print("Excel file converted to a text file.")
