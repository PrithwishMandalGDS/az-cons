import requests
import os
import pandas

def load_data(urls):
    save_directory = "downloaded_files"
    os.makedirs(save_directory, exist_ok=True)
    for url in urls:
        try:
            filename = url.split("/")[-1]
            save_path = os.path.join(save_directory, filename)
            response = requests.get(url, stream=True, verify=False)
            response.raise_for_status()
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f"File downloaded successfully: {save_path}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while downloading the file from {url}: {e}")

    return save_directory


