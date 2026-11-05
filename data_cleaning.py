import json
from pathlib import Path


def clean_dataset(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    cleaned_data = []
    seen_questions = set()

    for item in data:
        question = item.get("question", "").strip()
        answer = item.get("answer", "").strip()

        if not question or not answer:
            continue

        if question.lower() in seen_questions:
            continue

        seen_questions.add(question.lower())

        cleaned_data.append({
            "question": question,
            "answer": answer
        })

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(cleaned_data, file, indent=4)

    print(f"Cleaning completed: {len(cleaned_data)} records saved.")


if __name__ == "__main__":
    project_folder = Path(__file__).resolve().parents[2]
    input_file = project_folder / "data" / "product_dataset.json"
    output_file = project_folder / "data" / "cleaned_dataset.json"

    clean_dataset(input_file, output_file)