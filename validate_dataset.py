import json
from pathlib import Path

# Find the main project folder
project_folder = Path(__file__).resolve().parents[1]
data_folder = project_folder / "data"

files = ["product_dataset.json", "train.json", "validation.json", "test.json"]

for file_name in files:
    file_path = data_folder / file_name

    print(f"\nChecking {file_name}...")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("ERROR: Data must be a list.")
            continue

        valid = True

        for item in data:
            if not isinstance(item, dict):
                valid = False
                break

            if not isinstance(item.get("question"), str) or not item["question"].strip():
                valid = False
                break

            if not isinstance(item.get("answer"), str) or not item["answer"].strip():
                valid = False
                break

        if valid:
            print(f"SUCCESS: {len(data)} records found.")
        else:
            print("ERROR: A record has a missing or invalid question/answer.")

    except FileNotFoundError:
        print("ERROR: File not found.")

    except json.JSONDecodeError:
        print("ERROR: Invalid JSON format.")