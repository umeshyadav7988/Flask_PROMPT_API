# Flask Prompt API 🔥

This is a Flask-based API built using **MVC architecture** that matches system prompts based on input filters. The API uses a **service layer**, **view layer**, and includes full **automated testing with `pytest`**.

---

## 📬 Maintainer

- **Name:** Umesh 
- **Email:** [umeshyadav7988@gmail.com](mailto:umeshyadav7988@gmail.com)
- **GitHub:** [@umeshyadav7988](https://github.com/umeshyadav7988)

---

## 📁 Project Structure

```

flask\_prompt\_api/
├── app.py
├── services/
│   └── prompt\_service.py
├── views/
│   └── prompt\_view\.py
├── tests/
│   └── test\_api.py
├── Screenshots/
│   └── (All test run screenshots)
└── README.md

````

---

##  API Endpoint

### `POST /api/get-prompt`

#### 🔸 Request JSON:

```json
{
  "situation": "Commercial Auto",
  "level": "Structure",
  "file_type": "Summary Report",
  "data": "..."
}
````

#### 🔸 Response:

* If matched:

```json
{
  "prompt": "Prompt 1"
}
```

* If input is invalid:

```json
{
  "error": "Invalid Prompt"
}
```

* If any field is missing or empty:

```json
{
  "error": "Missing Data"
}
```

---

## ✅ Matching Prompt Logic

| Situation            | Level     | File Type       | Prompt   |
| -------------------- | --------- | --------------- | -------- |
| Commercial Auto      | Structure | Summary Report  | Prompt 1 |
| General Liability    | Summarize | Deposition      | Prompt 2 |
| Commercial Auto      | Summarize | Summons         | Prompt 3 |
| Workers Compensation | Structure | Medical Records | Prompt 4 |
| Workers Compensation | Summarize | Summons         | Prompt 5 |

---

## 🧪 Automated Testing

* Written with [`pytest`](https://docs.pytest.org/)
* Covers:

  * ✅ Valid prompt matches
  * ❌ Invalid prompt errors
  * ❌ Missing field errors
  * ❌ Non-JSON request handling

### Run tests:

```bash
# From project root
set PYTHONPATH=.
pytest -v
```

### 📸 Test Result Screenshots

All test run screenshots are attached in the `Screenshots/` folder for verification and demonstration purposes.

---

##  Setup Instructions

1. **Clone the Repo:**

```bash
git clone https://github.com/umeshyadav7988/Flask_PROMPT_API.git
cd Flask_PROMPT_API
```

2. **Create Virtual Environment:**

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. **Install Dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run Flask App:**

```bash
python app.py
```

5. **Run Tests:**

```bash
set PYTHONPATH=.
pytest -v
```



