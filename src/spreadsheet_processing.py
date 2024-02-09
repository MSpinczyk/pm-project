import pandas as pd
from io import StringIO
import csv

def save_string_as_csv(str):

    rows = [line.split(',') for line in str.strip().split('\n')]
    with open('output/output.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(rows)
     

def create_spreadsheet(table_string):
    cleaned_data_str = '\n'.join([','.join(cell.strip() for cell in line.split(',')) for line in table_string.split('\n')])

    lines = cleaned_data_str.split('\n')
    filtered_lines = [line for line in lines if "--- | --- | --- | --- | --- | ---" not in line]

    # Join the filtered lines back into a single string
    filtered_data_str = '\n'.join(filtered_lines)
    df = pd.read_csv(StringIO(filtered_data_str), sep='|', skipinitialspace=True)
    # df = df.iloc[1:-1, 1:-1]

    return df

def load_spreadsheet(filepath):
    df = pd.read_csv(filepath, index_col=None)
    return df

def update_spreadsheet(existing_spreadsheet, new_process_info):
    return NotImplementedError

def save_spreadsheet(df, filepath):
    return df.to_csv(filepath, index=False)
