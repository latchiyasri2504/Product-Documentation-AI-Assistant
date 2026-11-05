import json
from pathlib import Path

project_folder = Path(__file__).resolve().parents[1]

train_file = project_folder / "data" / "train.json"
validation_file = project_folder / "data" / "validation.json"
test_file = project_folder / "data" / "test.json"

with open(train_file, "r", encoding="utf-8") as file:
    train_data = json.load(file)

with open(validation_file, "r", encoding="utf-8") as file:
    validation_data = json.load(file)

with open(test_file, "r", encoding="utf-8") as file:
    test_data = json.load(file)

print("MODEL PERFORMANCE REPORT")
print("------------------------")
print("Training records:", len(train_data))
print("Validation records:", len(validation_data))
print("Testing records:", len(test_data))
print("Total records:", len(train_data) + len(validation_data) + len(test_data))
print("Dataset preparation status: Successful")
print("Actual SLM performance: Not evaluated (model unavailable offline)")