import pandas

def process_csv_data() -> pandas.DataFrame:
    current_dtf = pandas.read_csv(r'C:\Users\KY996XH\OneDrive - EY\Desktop\Az-Consumption-Assesment\codingazure\downloaded_files\CurrentState.csv')
    migration_plan_dtf = pandas.read_csv(r'C:\Users\KY996XH\OneDrive - EY\Desktop\Az-Consumption-Assesment\codingazure\downloaded_files\MigrationPlan.csv')
    return current_dtf


