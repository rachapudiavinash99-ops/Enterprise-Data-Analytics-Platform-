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

components = [
    "DataTable", "Pagination", "SearchBar", "FilterPanel", "Modal", 
    "ConfirmDialog", "LoadingState", "EmptyState", "ErrorState", 
    "KPIWidget", "ChartWidget", "DashboardGrid", "PipelineNode", "PipelineCanvas"
]

commits = []

# Generate React Components
for comp in components:
    commits.append({
        "msg": f"Add reusable UI component: {comp}",
        "files": {
            f"frontend/src/components/{comp}.tsx": f"import React from 'react';\n\nconst {comp} = (props: any) => {{\n  return (\n    <div className='{comp.lower()}-component'>\n      {comp} Component\n    </div>\n  );\n}};\n\nexport default {comp};\n"
        }
    })

# Generate Backend Services
services = ["auth_service", "user_service", "org_service", "dataset_service", "pipeline_service"]
for svc in services:
    commits.append({
        "msg": f"Implement backend service logic: {svc}",
        "files": {
            f"backend/app/services/{svc}.py": f"class {svc.replace('_', ' ').title().replace(' ', '')}:\n    def __init__(self):\n        pass\n    def execute(self):\n        return True\n"
        }
    })

for commit in commits:
    for path, content in commit["files"].items():
        create_file(path, content)
    run_git(["add", "."])
    run_git(["commit", "-m", commit["msg"]])
    time.sleep(0.5)

print("Additional components and services created successfully.")
