# filename: example_data_script.py
from functions import load_data

# Simulated function for demonstration
def simulated_load_data(urls):
    return ["Data from URL 1", "Data from URL 2"]

# A list of fake URLs to demonstrate the use of the function
urls = ['http://fakeurl.com/data1', 'http://fakeurl.com/data2']

# Simulating loading data using the fake function
data = simulated_load_data(urls)

# Print the simulated loaded data
print(data)