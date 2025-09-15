import pandas as pd

def add_calculated_column(df: pd.DataFrame, new_col: str, expr: str) -> pd.DataFrame:
    # Extremely basic and unsafe eval for demonstration
    # In production, use a safe parser or specialized grammar
    df[new_col] = df.eval(expr)
    return df

def filter_rows(df: pd.DataFrame, column: str, operator: str, value) -> pd.DataFrame:
    if operator == '==':
        return df[df[column] == value]
    elif operator == '>':
        return df[df[column] > value]
    elif operator == '<':
        return df[df[column] < value]
    return df

def aggregate_data(df: pd.DataFrame, group_by: list, agg_col: str, agg_func: str) -> pd.DataFrame:
    return df.groupby(group_by).agg({agg_col: agg_func}).reset_index()
