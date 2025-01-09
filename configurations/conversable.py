import pandas
from autogen.coding.func_with_reqs import Alias, ImportFromModule, with_requirements
from pathlib import Path
from autogen.coding import CodeBlock, LocalCommandLineCodeExecutor
from prompts.prompts import code_writer_system_message, code_writer_gap_system_message
import os
import requests

@with_requirements(python_packages=["pandas", "requests"], global_imports=["pandas", "os", "requests"])
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

@with_requirements(python_packages=["pandas"], global_imports=["pandas"])
def process_csv_data(value) -> pandas.DataFrame:
    current = pandas.read_csv(r'C:\Users\KY996XH\OneDrive - EY\Desktop\Az-Consumption-Assesment\codingazure\downloaded_files\CurrentState.csv' , header=1)
    migration = pandas.read_csv(r'C:\Users\KY996XH\OneDrive - EY\Desktop\Az-Consumption-Assesment\codingazure\downloaded_files\MigrationPlan.csv', header=1)
    print(migration)
    columns_to_clean = ["2022", "2023", "2024", "2025", "2026"]
    for col in columns_to_clean:
        migration[col] = migration[col].str.replace("[$,]", "", regex=True).replace("", 0).astype(float)

    migration_result = migration.groupby("Application Name").agg({
        "ServerName": "first",
        "Operating System": "first",
        "R-Lane Disposition": "first",
        "Migration Phase": "first",
        "Migration Start": "first",
        "Migration End": "first",
        "2022": "sum",
        "2023": "sum",
        "2024": "sum",
        "2025": "sum",
        "2026": "sum"
    }).reset_index()
    migration_result = migration_result.fillna(0)
    current = current.fillna(0)
    column_value = "2022"
    current_gap_col = list(current[column_value])
    current_gap_col = [int(item.replace('$', '').replace(',', '')) if isinstance(item, str) else item for item in
                       current_gap_col]
    migration_gap_col = list(migration_result[column_value])
    migration_gap_col = [int(item.replace('$', '').replace(',', '')) if isinstance(item, str) else item for item in
                         migration_gap_col]
    gap_values = []
    for i in range(len(current_gap_col)):
        gap = current_gap_col[i] - migration_gap_col[i]
        gap_values.append(gap)
    absolute_gap_values = [abs(item) for item in gap_values]
    df = pandas.DataFrame(absolute_gap_values, columns=['GAP'])
    migration_result.drop(columns_to_clean, axis=1, inplace=True)
    migration_result['GAP'] = df['GAP']
    migration_result.to_csv(f"gap.csv")

    return migration_result

work_dir_az = Path("codingazure")
work_dir_gap = Path("codinggap")
work_dir_az.mkdir(exist_ok=True)
work_dir_gap.mkdir(exist_ok=True)
executor = LocalCommandLineCodeExecutor(work_dir=work_dir_az, functions=[load_data])
executor_dtf = LocalCommandLineCodeExecutor(work_dir=work_dir_gap, functions=[process_csv_data])

def get_execution_results(urls, executor):
    code = f"""
from {executor.functions_module} import load_data

# Execute the load_data function with provided URLs
results = load_data({urls})
print(results)
"""
    # Execute the generated code
    result = executor.execute_code_blocks(
        code_blocks=[
            CodeBlock(language="python", code=code),
        ]
    )
    return result

def get_gap_results(executor):
    code = f"""
from {executor.functions_module} import process_csv_data

# Execute the process_csv_data function to process the datasets that recently got downloaded in codingazure/downloaded_files folder
results = process_csv_data()
print(results)
"""
    # Execute the generated code
    result = executor.execute_code_blocks(
        code_blocks=[
            CodeBlock(language="python", code=code),
        ]
    )
    return result

code_writer_system_message += executor.format_functions_for_prompt()
code_writer_gap_system_message += executor_dtf.format_functions_for_prompt()


