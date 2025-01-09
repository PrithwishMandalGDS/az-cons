# filename: load_and_preview_csv_data.py
from functions import process_csv_data

# Since I don't have direct access to the downloaded file, 
# I am assuming that the file path is known and assigned to a variable `recent_csv_file_path`.
# You will need to replace `recent_csv_file_path` with the actual path to your CSV file.
recent_csv_file_path = 'path_to_the_recently_downloaded_csv'

# Load the data using the `process_csv_data` function
data = process_csv_data(recent_csv_file_path)

# Print the first few rows of the DataFrame
print(data.head())