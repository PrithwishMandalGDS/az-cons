import os
import pandas
import requests

def load_data(urls, save_directory) -> pandas.DataFrame:
    print(urls)
    print(save_directory)
    data = pandas.read_csv(r'C:\Users\KY996XH\OneDrive - EY\Desktop\AIOPS\AZConsumption\GENAI\dataset\mvp.csv')
    return pandas.DataFrame(data)


