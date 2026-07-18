# Calculator with GitHub Actions

A simple Python calculator project that demonstrates **Continuous Integration (CI)** using **GitHub Actions**.

Whenever code is pushed to the repository, GitHub Actions automatically:
- Checks out the repository
- Sets up Python
- Installs project dependencies
- Runs unit tests using `pytest`

This project was created to understand the fundamentals of GitHub Actions and CI pipelines.

---

## Project Structure

```text
Calculator-Github_Actions/
│
├── .github/
│   └── workflows/
│       └── python-ci.yml
│
├── calculator.py
├── test_calculator.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Division by zero handling
- Unit testing with Pytest
- Automated testing using GitHub Actions

---

## Technologies Used

- Python 3
- Pytest
- Git
- GitHub Actions

---

## Installation

Clone the repository:

```bash
git clone https://github.com/hrshtmlng/Calculator-Github_Actions.git
```

Move into the project directory:

```bash
cd Calculator-Github_Actions
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

### Linux/macOS

```bash
source .venv/bin/activate
```

### Windows

```cmd
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Calculator

```bash
python calculator.py
```

Example output:

```text
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0
```

---

## Running Tests

Run all unit tests:

```bash
pytest
```

Expected output:

```text
======================== test session starts ========================

collected 5 items

test_calculator.py .....                     [100%]

======================== 5 passed ========================
```

---

## GitHub Actions Workflow

The workflow is located at:

```text
.github/workflows/python-ci.yml
```

It performs the following steps automatically on every push to the `main` branch:

1. Checkout the repository
2. Set up Python
3. Install dependencies
4. Run all unit tests using Pytest

If all tests pass, the workflow succeeds. If any test fails, the workflow is marked as failed.

---

## Learning Outcomes

This project helped in understanding:

- Git basics
- GitHub repository management
- Unit testing with Pytest
- Continuous Integration (CI)
- GitHub Actions workflows
- Automated testing on every code push

---

## Future Improvements

- Add code linting using Flake8
- Test against multiple Python versions
- Add code coverage reporting
- Expand calculator functionality

---

## Author

**Harshit Malang**

GitHub: https://github.com/hrshtmlng