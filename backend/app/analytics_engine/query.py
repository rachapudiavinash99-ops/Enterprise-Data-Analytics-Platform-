import pandas as pd
from typing import List, Dict, Any

def execute_analytics_query(df: pd.DataFrame, group_by: List[str], metrics: List[Dict[str, str]]) -> pd.DataFrame:
    # metrics format: [{'column': 'revenue', 'agg': 'sum'}]
    agg_dict = {m['column']: m['agg'] for m in metrics}
    if group_by:
        return df.groupby(group_by).agg(agg_dict).reset_index()
    else:
        # Global aggregation without grouping
        res = {}
        for col, agg in agg_dict.items():
            res[f"{col}_{agg}"] = df[col].agg(agg)
        return pd.DataFrame([res])
