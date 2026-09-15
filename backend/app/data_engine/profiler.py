import pandas as pd
import json
import numpy as np

def profile_dataset(file_path: str):
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        else:
            raise ValueError('Unsupported file format')
            
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
                'null_percentage': float((col_data.isnull().sum() / len(df)) * 100) if len(df) > 0 else 0,
                'unique_count': int(col_data.nunique())
            }
            
            if pd.api.types.is_numeric_dtype(col_data):
                col_profile.update({
                    'min': float(col_data.min()) if not pd.isna(col_data.min()) else None,
                    'max': float(col_data.max()) if not pd.isna(col_data.max()) else None,
                    'mean': float(col_data.mean()) if not pd.isna(col_data.mean()) else None,
                    'median': float(col_data.median()) if not pd.isna(col_data.median()) else None,
                    'std_dev': float(col_data.std()) if not pd.isna(col_data.std()) else None,
                })
            elif pd.api.types.is_string_dtype(col_data):
                top_values = col_data.value_counts().head(5).to_dict()
                col_profile['top_values'] = {str(k): int(v) for k, v in top_values.items()}
                
            profile['columns'].append(col_profile)
            
        return profile
    except Exception as e:
        return {'error': str(e)}
