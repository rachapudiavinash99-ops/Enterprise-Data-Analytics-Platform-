import pandas as pd

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates()

def fill_missing_values(df: pd.DataFrame, column: str, value) -> pd.DataFrame:
    df[column] = df[column].fillna(value)
    return df

def drop_missing_values(df: pd.DataFrame, column: str) -> pd.DataFrame:
    return df.dropna(subset=[column])

def normalize_text(df: pd.DataFrame, column: str) -> pd.DataFrame:
    df[column] = df[column].str.strip().str.lower()
    return df

def apply_cleaning_operations(df: pd.DataFrame, operations: list) -> pd.DataFrame:
    for op in operations:
        op_type = op['type']
        if op_type == 'remove_duplicates':
            df = remove_duplicates(df)
        elif op_type == 'fill_missing':
            df = fill_missing_values(df, op['column'], op['value'])
        elif op_type == 'drop_missing':
            df = drop_missing_values(df, op['column'])
        elif op_type == 'normalize_text':
            df = normalize_text(df, op['column'])
    return df
