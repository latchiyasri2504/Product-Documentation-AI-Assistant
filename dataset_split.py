import json
from pathlib import Path

project_folder = Path(__file__).resolve().parents[1]

input_file = project_folder / "data" / "cleaned_dataset.json"

with open(input_file, "r", encoding="utf-8") as file:
    data = json.load(file)

total = len(data)

train_end = int(total * 0.6)
validation_end = int(total * 0.8)

train_data = data[:train_end]
validation_data = data[train_end:validation_end]
test_data = data[validation_end:]

datasets = {
    "train.json": train_data,
    "validation.json": validation_data,
    "test.json": test_data
}

for filename, records in datasets.items():
    output_file = project_folder / "data" / filename

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)

    print(f"{filename}: {len(records)} records saved.")

print("Dataset splitting completed!")