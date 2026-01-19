# Text Transform API (Python / FastAPI)

A small REST API built with Python and FastAPI that performs text transformations.  
Currently supports Caesar cipher encryption.

## About the project
This project was created to demonstrate backend development fundamentals using Python.
The focus is on clean code, clear separation between business logic and API layer, and basic testing.

The API exposes an endpoint that accepts text and a shift value, then returns the transformed result.

## Features
- Caesar cipher text transformation
- Preserves uppercase, lowercase, and non-alphabetic characters
- Input validation using Pydantic
- REST API built with FastAPI
- Unit tests for core logic

## Project structure
```
text-transform-api/
├── app/
│ ├── init.py
│ ├── main.py # FastAPI application and routes
│ └── caesar.py # Caesar cipher logic
├── tests/
│ └── test_caesar.py # Unit tests
├── requirements.txt
└── README.md
```

## How to run

Install dependencies:
```bash
pip install -r requirements.txt

Start the development server:
uvicorn app.main:app --reload

The API will be available at:
http://127.0.0.1:8000

Interactive API documentation:
http://127.0.0.1:8000/docs

Example request:
{
  "text": "Hello World",
  "shift": 3
}

Example response:
{
  "result": "Khoor Zruog"
}

Testing
Unit tests are included for the Caesar cipher logic.

Run tests with:
pytest
