import sys
import unittest
from pathlib import Path

project_folder = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_folder))

from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


class TestAPI(unittest.TestCase):

    def test_health_endpoint(self):
        response = client.get("/health")
        self.assertEqual(response.status_code, 200)

    def test_ask_endpoint(self):
        response = client.post(
            "/ask",
            json={"question": "What is a product?"}
        )
        self.assertEqual(response.status_code, 200)

    def test_short_question(self):
        response = client.post(
            "/ask",
            json={"question": "Hi"}
        )
        self.assertEqual(response.status_code, 422)


if __name__ == "__main__":
    unittest.main()