import pandas as pd
import numpy as np

# Define the date range
start_date = pd.Timestamp('2022-01-01')
end_date = pd.Timestamp('2026-12-31')

# Generate a list of all dates within the date range
date_range = pd.date_range(start=start_date, end=end_date)

# Calculate the number of days in the date range
total_days = len(date_range)

# Determine the minimum occurrences per day to ensure coverage of all days
min_occurrences_per_day = 1

# Calculate the total number of occurrences needed to reach 75,620 rows
total_occurrences_needed = 75620

# Ensure that we have enough days to cover the required occurrences
if total_occurrences_needed > total_days:
    raise ValueError("Total number of required occurrences exceeds the number of unique days in the date range.")

# Create a DataFrame to store the dates and occurrences
data = {'Date': [], 'Occurrences': []}

# Iterate over each date and assign a random number of occurrences (at least 1)
for date in date_range:
    num_occurrences = np.random.randint(min_occurrences_per_day, total_occurrences_needed + 1)
    data['Date'].extend([date] * num_occurrences)
    data['Occurrences'].extend(range(1, num_occurrences + 1))

# Create a DataFrame from the data dictionary
df = pd.DataFrame(data)

# Shuffle the DataFrame to randomize the order of rows
df = df.sample(frac=1).reset_index(drop=True)

# Select the first 75,620 rows to create the final dataset
final_df = df.head(total_occurrences_needed)

# Export the final DataFrame to a CSV file
final_df.to_csv('dates_dataset.csv', index=False)
