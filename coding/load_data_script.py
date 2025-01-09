# filename: load_data_script.py
from functions import load_data

# List of URLs to load data from
urls = ['http://example.com/data1', 'http://example.com/data2']

# Loading data using the load_data function
data = load_data(urls)

# Print the loaded data
print(data)