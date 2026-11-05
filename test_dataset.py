import json
import unittest
from pathlib import Path


project_folder = Path(__file__).resolve().parents[1]
dataset_file = project_folder / "data" / "cleaned_dataset.json"


class TestDataset(unittest.TestCase):

    def test_dataset_exists(self):
        self.assertTrue(dataset_file.exists())

    def test_dataset_records(self):
        with open(dataset_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.assertGreater(len(data), 0)

    def test_questions_and_answers(self):
        with open(dataset_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        for item in data:
            self.assertTrue(item["question"].strip())
            self.assertTrue(item["answer"].strip())


if __name__ == "__main__":
    unittest.main()