# filename: load_data_example.py
from functions import load_data

# Example list of URLs
urls = [
    'http://example.com/data1.csv',
    'http://example.com/data2.json'
]

# Calling the load_data function with the list of URLs
data = load_data(urls)

# Printing the loaded data
for content in data:
    print(content)