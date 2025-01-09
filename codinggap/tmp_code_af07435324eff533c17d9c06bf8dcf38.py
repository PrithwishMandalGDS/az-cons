import pandas

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


