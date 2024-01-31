import pandas as pd
from io import StringIO

def create_spreadsheet(table_string):
    df = pd.read_csv(StringIO(table_string), delimiter='|', skipinitialspace=True)
    df = df.iloc[1:-1, 1:-1]

    return df

def load_spreadsheet(filepath):
    df = pd.read_csv(filepath, index_col=None)
    return df

def update_spreadsheet(existing_spreadsheet, new_process_info):
    # Update an existing spreadsheet with new process information
    pass

def save_spreadsheet(df, filepath):
    return df.to_csv(filepath, index=False)
