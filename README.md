# NAME : PRAJAPATI MITKUMAR JAYANTIBHAI
# ENROLLMENT NO. : 202326900094



# FastAPI – Student CRUD Application

A university student management REST API built with FastAPI and Python, utilizing local in-memory storage (no database) and an industry-standard layered architecture (**Models → Routes → Controllers**).

---

## 📁 Project Architecture & Folder Structure

```
student-crud/
├── controllers/
│   └── student_controller.py   # CRUD/business logic & in-memory collection
├── models/
│   └── student_model.py        # Student dictionary builder function
├── routes/
│   └── student_routes.py        # REST API endpoints, HTTP verbs, status codes
├── tests/
│   ├── __init__.py
│   └── test_student_crud.py    # Automated pytest test suite
├── main.py                     # FastAPI application setup and router inclusion
├── requirements.txt            # Project dependencies
├── test_api_checklist.py       # Standalone 10-point checklist test runner
└── README.md                   # Documentation and usage guide
```

### Responsibility of Each Layer
- **Models (`models/student_model.py`)**: Provides a simple function for building student dictionaries.
- **Controllers (`controllers/student_controller.py`)**: Encapsulates all business logic, auto-incrementing ID management, and in-memory operations on the student collection.
- **Routes (`routes/student_routes.py`)**: Declares API routes, HTTP verbs, dictionary request/response data, and query parameter filtering.
- **`main.py`**: Initializes the FastAPI app, configures lifespan hooks, seeds sample data, and registers routes.

---

## 🚀 Setup & Execution

### 1. Create and Activate Virtual Environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
uvicorn main:app --reload
```

The application will start at: `http://127.0.0.1:8000`

For local development, run the server through Uvicorn as shown above. The application code does not hardcode a host or port; Render supplies those values through `render.yaml`.

## Deployment and CI/CD

The included `render.yaml` configures the service for Render. In Render, create a new Blueprint from this repository or use the file's build and start commands.

The GitHub Actions workflow at `.github/workflows/ci-cd.yml` runs the test suite for pull requests and pushes to `main`. To enable automatic deployment after a successful push to `main`:

1. Create a Render deploy hook for the web service.
2. Add it to the GitHub repository as the `RENDER_DEPLOY_HOOK_URL` secret.
3. Push to `main`.

---

## 📖 API Documentation & Swagger UI

FastAPI automatically generates interactive Swagger documentation:
- **Interactive Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc Documentation**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📡 REST API Reference

| # | Operation | HTTP Verb | Endpoint | Success Status | Error Status | Description |
|---|---|---|---|---|---|---|
| 1 | Create Student | `POST` | `/students` | `201 Created` | `422 Unprocessable` | Create a new student record |
| 2 | Read All Students | `GET` | `/students` | `200 OK` | `422` (bad query) | Retrieve all students (with search/pagination) |
| 3 | Read Student by ID | `GET` | `/students/{id}` | `200 OK` | `404 Not Found` | Retrieve a single student by unique ID |
| 4 | Update Student | `PUT` | `/students/{id}` | `200 OK` | `404 Not Found`, `422` | Update an existing student by ID |
| 5 | Delete Student | `DELETE` | `/students/{id}` | `204 No Content` | `404 Not Found` | Delete a student by ID (empty response body) |

### Sample Request Body (`POST /students`)
```json
{
  "name": "Rahul Patel",
  "email": "rahul@example.com",
  "course": "B.Tech Computer Engineering",
  "semester": 5
}
```

### Bonus Features Included
- **Search & Filtering**:
  - Filter by name: `GET /students?name=Rahul`
  - Filter by course: `GET /students?course=Computer`
  - Filter by semester: `GET /students?semester=5`
- **Pagination**:
  - `GET /students?skip=0&limit=10`

---

## 🧪 Testing

### Running the Pytest Suite
```bash
pytest -v
```

### Running the 10-Point Checklist Verification Script
```bash
python test_api_checklist.py
```

### Test Checklist Results (Section 7)

| # | Test Case | Expected Result | Status |
|---|---|---|---|
| 1 | Create a valid student | 201 Created + created student | ✅ PASSED |
| 2 | Create a student with invalid data | Validation error / 422 | ✅ PASSED |
| 3 | Get all students | 200 OK + list of students | ✅ PASSED |
| 4 | Get an existing student ID | 200 OK + student | ✅ PASSED |
| 5 | Get a non-existing student ID | 404 Not Found | ✅ PASSED |
| 6 | Update an existing student | 200 OK + updated student | ✅ PASSED |
| 7 | Update a non-existing student ID | 404 Not Found | ✅ PASSED |
| 8 | Delete an existing student | 204 No Content | ✅ PASSED |
| 9 | Delete a non-existing student ID | 404 Not Found | ✅ PASSED |
| 10 | Verify deleted student cannot be retrieved | 404 Not Found | ✅ PASSED |
