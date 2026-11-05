import json
from pathlib import Path

project_folder = Path(__file__).resolve().parents[1]
test_file = project_folder / "data" / "test.json"

with open(test_file, "r", encoding="utf-8") as file:
    test_data = json.load(file)

total = len(test_data)
valid = 0

for item in test_data:
    if item.get("question") and item.get("answer"):
        valid += 1

print("DATASET EVALUATION")
print("------------------")
print("Total test records:", total)
print("Valid records:", valid)
print("Invalid records:", total - valid)

if total > 0:
    print("Evaluation completed successfully!")
else:
    print("No test records available.")