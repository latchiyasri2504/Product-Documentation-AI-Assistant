import json
from pathlib import Path

project_folder = Path(__file__).resolve().parents[1]
dataset_file = project_folder / "data" / "cleaned_dataset.json"

with open(dataset_file, "r", encoding="utf-8") as file:
    data = json.load(file)

total_records = len(data)

print("DATASET STATISTICS")
print("------------------")
print("Total records:", total_records)
print("Valid questions:", sum(1 for item in data if item.get("question")))
print("Valid answers:", sum(1 for item in data if item.get("answer")))