import pandas as pd
import json

def profile_dataset(file_path: str):
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    else:
        raise ValueError('Unsupported file format for profiling')
        
    profile = {
        'row_count': len(df),
        'column_count': len(df.columns),
        'columns': []
    }
    
    for col in df.columns:
        col_data = df[col]
        col_profile = {
            'name': col,
            'type': str(col_data.dtype),
            'null_count': int(col_data.isnull().sum()),
            'unique_count': int(col_data.nunique())
        }
        if pd.api.types.is_numeric_dtype(col_data):
            col_profile.update({
                'min': float(col_data.min()) if not pd.isna(col_data.min()) else None,
                'max': float(col_data.max()) if not pd.isna(col_data.max()) else None,
                'mean': float(col_data.mean()) if not pd.isna(col_data.mean()) else None
            })
        profile['columns'].append(col_profile)
        
    return profile
