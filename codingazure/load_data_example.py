# filename: load_data_example.py
from functions import load_data

# Replace these with the actual URLs you want to load data from
urls_to_load = ["http://example.com/data1", "http://example.com/data2"]

# Calling the load_data function with the list of URLs
data = load_data(urls_to_load)

# For demonstration purposes, we'll print out the type of the data returned
print(type(data))

# If data is expected to be a list or any iterable, we can print the first few elements.
if isinstance(data, (list, tuple, set)):
    for item in data[:10]:  # Assuming you want to see the first 10 items
        print(item)