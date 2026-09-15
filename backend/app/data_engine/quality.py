import pandas as pd

def validate_not_null(df: pd.DataFrame, column: str):
    return df[column].notnull()

def validate_unique(df: pd.DataFrame, column: str):
    return ~df[column].duplicated(keep=False)

def apply_quality_rules(df: pd.DataFrame, rules: list):
    results = {}
    for rule in rules:
        col = rule['column']
        rule_type = rule['type']
        if rule_type == 'not_null':
            valid_mask = validate_not_null(df, col)
        elif rule_type == 'unique':
            valid_mask = validate_unique(df, col)
        else:
            continue
        
        results[f"{col}_{rule_type}"] = {
            'valid_count': int(valid_mask.sum()),
            'invalid_count': int((~valid_mask).sum()),
            'pass_rate': float(valid_mask.mean())
        }
    return results
