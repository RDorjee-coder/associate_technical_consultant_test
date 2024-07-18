# Python program to import excel file and computing aggregate on the sales and transaction column
# using pandas
import pandas as pd
from datetime import datetime, timedelta
import random

# Load Excel file
file_path = 'data.xlsx'
df = pd.read_excel(file_path)

# Transaction column missing in the data.xls
# Create new column 'transaction' with random numbers

df['transaction'] = [random.randint(0, 100) for _ in range(len(df))]

# Convert 'time' column to datetime format
df['time'] = pd.to_datetime(df['time'])

# Calculate sales and transactions per 15-minute time bucket
df['time_bucket'] = df['time'] - pd.to_timedelta(df['time'].dt.minute % 15, unit='m')
result_df = df.groupby('time_bucket').agg({'sales': 'sum', 'transaction': 'sum'}).reset_index()

# Write results to CSV file
output_file = 'results.csv'
result_df.to_csv(output_file, index=False, date_format='%Y-%m-%d %H:%M:%S')

print(f"Results saved to {output_file}")
