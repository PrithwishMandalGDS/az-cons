
from functions import load_data

# Execute the load_data function with provided URLs
results = load_data(['https://azassesment.blob.core.windows.net/gap/MigrationPlan.csv', 'https://azassesment.blob.core.windows.net/gap/CurrentState.csv'])
print(results)
