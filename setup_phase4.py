import os
import subprocess
import time

def run_git(cmd_args):
    subprocess.run(["git"] + cmd_args, check=True)

def create_file(path, content=""):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

commits = [
    {
        "msg": "Implement Data Quality rules engine",
        "files": {
            "backend/app/data_engine/quality.py": "import pandas as pd\n\ndef validate_not_null(df: pd.DataFrame, column: str):\n    return df[column].notnull()\n\ndef validate_unique(df: pd.DataFrame, column: str):\n    return ~df[column].duplicated(keep=False)\n\ndef apply_quality_rules(df: pd.DataFrame, rules: list):\n    results = {}\n    for rule in rules:\n        col = rule['column']\n        rule_type = rule['type']\n        if rule_type == 'not_null':\n            valid_mask = validate_not_null(df, col)\n        elif rule_type == 'unique':\n            valid_mask = validate_unique(df, col)\n        else:\n            continue\n        \n        results[f\"{col}_{rule_type}\"] = {\n            'valid_count': int(valid_mask.sum()),\n            'invalid_count': int((~valid_mask).sum()),\n            'pass_rate': float(valid_mask.mean())\n        }\n    return results\n"
        }
    },
    {
        "msg": "Implement Data Cleaning engine operations",
        "files": {
            "backend/app/data_engine/cleaning.py": "import pandas as pd\n\ndef remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:\n    return df.drop_duplicates()\n\ndef fill_missing_values(df: pd.DataFrame, column: str, value) -> pd.DataFrame:\n    df[column] = df[column].fillna(value)\n    return df\n\ndef drop_missing_values(df: pd.DataFrame, column: str) -> pd.DataFrame:\n    return df.dropna(subset=[column])\n\ndef normalize_text(df: pd.DataFrame, column: str) -> pd.DataFrame:\n    df[column] = df[column].str.strip().str.lower()\n    return df\n\ndef apply_cleaning_operations(df: pd.DataFrame, operations: list) -> pd.DataFrame:\n    for op in operations:\n        op_type = op['type']\n        if op_type == 'remove_duplicates':\n            df = remove_duplicates(df)\n        elif op_type == 'fill_missing':\n            df = fill_missing_values(df, op['column'], op['value'])\n        elif op_type == 'drop_missing':\n            df = drop_missing_values(df, op['column'])\n        elif op_type == 'normalize_text':\n            df = normalize_text(df, op['column'])\n    return df\n"
        }
    },
    {
        "msg": "Add Data Transformation engine capabilities",
        "files": {
            "backend/app/data_engine/transformation.py": "import pandas as pd\n\ndef add_calculated_column(df: pd.DataFrame, new_col: str, expr: str) -> pd.DataFrame:\n    # Extremely basic and unsafe eval for demonstration\n    # In production, use a safe parser or specialized grammar\n    df[new_col] = df.eval(expr)\n    return df\n\ndef filter_rows(df: pd.DataFrame, column: str, operator: str, value) -> pd.DataFrame:\n    if operator == '==':\n        return df[df[column] == value]\n    elif operator == '>':\n        return df[df[column] > value]\n    elif operator == '<':\n        return df[df[column] < value]\n    return df\n\ndef aggregate_data(df: pd.DataFrame, group_by: list, agg_col: str, agg_func: str) -> pd.DataFrame:\n    return df.groupby(group_by).agg({agg_col: agg_func}).reset_index()\n"
        }
    },
    {
        "msg": "Add frontend pages for Data Quality and Cleaning",
        "files": {
            "frontend/src/pages/DataQuality.tsx": "import React from 'react';\n\nconst DataQuality = () => {\n  return (\n    <div>\n      <h2>Data Quality Engine</h2>\n      <p>Configure and run quality rules (e.g., Not Null, Unique).</p>\n    </div>\n  );\n};\n\nexport default DataQuality;\n",
            "frontend/src/App.tsx": "import React from 'react';\nimport { BrowserRouter, Routes, Route } from 'react-router-dom';\nimport Login from './pages/Login';\nimport Dashboard from './pages/Dashboard';\nimport Organizations from './pages/Organizations';\nimport Users from './pages/Users';\nimport Datasets from './pages/Datasets';\nimport DataQuality from './pages/DataQuality';\n\nfunction App() {\n  return (\n    <BrowserRouter>\n      <Routes>\n        <Route path='/login' element={<Login />} />\n        <Route path='/' element={<Dashboard />} />\n        <Route path='/organizations' element={<Organizations />} />\n        <Route path='/users' element={<Users />} />\n        <Route path='/datasets' element={<Datasets />} />\n        <Route path='/quality' element={<DataQuality />} />\n      </Routes>\n    </BrowserRouter>\n  );\n}\n\nexport default App;\n"
        }
    }
]

for commit in commits:
    for path, content in commit["files"].items():
        create_file(path, content)
    run_git(["add", "."])
    run_git(["commit", "-m", commit["msg"]])
    time.sleep(1)

print("Phase 4 commits created successfully.")
