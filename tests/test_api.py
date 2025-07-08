import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import json
from app import app 

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

@pytest.mark.parametrize("payload, expected", [
    ({"situation": "Commercial Auto", "level": "Structure", "file_type": "Summary Report", "data": "Test"}, "Prompt 1"),
    ({"situation": "General Liability", "level": "Summarize", "file_type": "Deposition", "data": "Test"}, "Prompt 2"),
    ({"situation": "Commercial Auto", "level": "Summarize", "file_type": "Summons", "data": "Test"}, "Prompt 3"),
    ({"situation": "Workers Compensation", "level": "Structure", "file_type": "Medical Records", "data": "Test"}, "Prompt 4"),
    ({"situation": "Workers Compensation", "level": "Summarize", "file_type": "Summons", "data": "Test"}, "Prompt 5"),
])
def test_valid_prompts(client, payload, expected):
    response = client.post("/api/get-prompt", json=payload)
    assert response.status_code == 200
    assert response.get_json()["prompt"] == expected

def test_invalid_prompt(client):
    payload = {
        "situation": "General Liability",
        "level": "Structure",
        "file_type": "Summons",
        "data": "Test"
    }
    response = client.post("/api/get-prompt", json=payload)
    assert response.status_code == 400
    assert response.get_json()["error"] == "Invalid Prompt"

@pytest.mark.parametrize("payload", [
    {"situation": "Commercial Auto", "level": "Structure", "file_type": "Summary Report"},  # missing data
    {"level": "Structure", "file_type": "Summary Report", "data": "Test"},  # missing situation
    {},  # all missing
    {"situation": "Commercial Auto", "level": "", "file_type": "Summary Report", "data": "Test"}  # empty field
])
def test_missing_fields(client, payload):
    response = client.post("/api/get-prompt", json=payload)
    assert response.status_code == 400
    assert response.get_json()["error"] == "Missing Data"

def test_non_json_body(client):
    response = client.post("/api/get-prompt", data="Just a string", content_type="text/plain")
    assert response.status_code in (400, 500)
    assert "error" in response.get_json()
