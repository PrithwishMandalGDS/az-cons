import pandas

def process_csv_data() -> pandas.DataFrame:
    current_dtf = pandas.read_csv('./coding/downloaded_files/CurrentState.csv')
    migration_plan_dtf = pandas.read_csv('./coding/downloaded_files/MigrationPlan.csv')
    return current_dtf


