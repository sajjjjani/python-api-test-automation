
# Python API Test Automation

A beginner-friendly API automation testing project built with Python, Pytest, and Requests. It tests REST API endpoints using JSONPlaceholder, a public fake API for testing and prototyping.

## Tech Stack

- Python
- Pytest
- Requests
- JSONPlaceholder REST API
- Git and GitHub

## Project Structure

```text
python-api-test-automation/
├── conftest.py
├── requirements.txt
├── README.md
└── tests/
    ├── __init__.py
    ├── test_get_requests.py
    ├── test_post_requests.py
    ├── test_update_requests.py
    └── test_delete_requests.py
```

## Test Coverage

| HTTP Method | Coverage |
|---|---|
| GET | Retrieve a single post |
| GET | Verify a nonexistent post returns 404 |
| GET | Retrieve multiple posts using parametrized tests |
| POST | Create a post and validate the response |
| POST | Observe API behavior when the title is missing |
| PUT | Update a post and validate the response |
| PATCH | Update a post's title |
| DELETE | Send a delete request and validate the response |

The current test suite contains 10 test cases, including parametrized GET tests.

## Setup and Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd python-api-test-automation
```

### 2. Create and activate a virtual environment

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Run the Tests

Run the complete test suite:

```bash
python -m pytest -v
```

## Test Results

The current local test run passes all 10 tests.

## Notes and Limitations

JSONPlaceholder is a mock API. POST, PUT, PATCH, and DELETE requests simulate API behavior; changes are not permanently stored. Its behavior may differ from a production API, including how it handles incomplete payloads.

## Learning Objectives

- Send HTTP requests using Python Requests
- Validate HTTP status codes and JSON responses
- Write automated tests using Pytest
- Use parametrized tests
- Reuse configuration with a Pytest fixture
- Organize tests by HTTP method