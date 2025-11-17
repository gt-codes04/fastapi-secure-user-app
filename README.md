FastAPI Secure User App

This project implements a secure user management API using FastAPI, SQLAlchemy, and PostgreSQL. It focuses on secure password handling, database integration, input validation, and proper API structuring. The application includes full unit and integration test coverage and uses Docker for containerization. Continuous Integration is configured through GitHub Actions to run tests automatically on every push.

Project Overview

The application supports secure user creation with the following key features:

Password hashing using Passlib (bcrypt)

Validation of usernames, emails, and passwords

Enforcement of unique usernames

Clean separation of models, schemas, security utilities, and CRUD operations

API routes built using FastAPI’s router system

Full testing setup using pytest

A CI pipeline that installs dependencies, runs tests, and builds a Docker image

Technologies Used

FastAPI

SQLAlchemy

PostgreSQL

Pydantic

Passlib (bcrypt)

Pytest

Docker

GitHub Actions

Running the Application Locally
1. Create and activate a virtual environment

Windows (PowerShell):

python -m venv .venv
.venv\Scripts\activate


macOS/Linux:

python3 -m venv .venv
source .venv/bin/activate

2. Install dependencies
pip install -r requirements.txt

Running PostgreSQL Locally

The app needs a running PostgreSQL instance. The easiest option is Docker:

docker run --name fastapi-secure-user-db `
  -e POSTGRES_USER=postgres `
  -e POSTGRES_PASSWORD=postgres `
  -e POSTGRES_DB=app_db `
  -p 5432:5432 -d postgres:16

Starting the Application
uvicorn app.main:app --reload


API URL:

http://localhost:8000


Docs (Swagger UI):

http://localhost:8000/docs

Running Tests Locally
1. Start a separate test PostgreSQL instance
docker run --name test-db `
  -e POSTGRES_USER=postgres `
  -e POSTGRES_PASSWORD=postgres `
  -e POSTGRES_DB=test_db `
  -p 5433:5432 -d postgres:16

2. Set the test database URL

Windows (PowerShell):

$env:TEST_DATABASE_URL="postgresql://postgres:postgres@localhost:5433/test_db"

3. Run pytest
pytest


All tests should pass.

Docker Image

The application is fully containerized.

Build the image manually
docker build -t fastapi-secure-user-app .

Run the container with a PostgreSQL network
docker network create fastapi-secure-user-net

docker run --name fastapi-secure-user-db --network fastapi-secure-user-net `
  -e POSTGRES_USER=postgres `
  -e POSTGRES_PASSWORD=postgres `
  -e POSTGRES_DB=app_db `
  -p 5432:5432 -d postgres:16

docker run --name fastapi-secure-user-app --network fastapi-secure-user-net `
  -p 8000:8000 fastapi-secure-user-app

GitHub Actions CI/CD

A GitHub Actions workflow is included under:

.github/workflows/ci.yml


The pipeline performs the following steps on every push:

Set up Python

Install dependencies

Start a PostgreSQL service container

Run all unit and integration tests

Build a Docker image

The workflow will only succeed if all tests pass.

Project Structure
fastapi-secure-user-app/
│
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── db.py
│   ├── security.py
│   └── routers/
│       └── users.py
│
├── tests/
│   ├── unit/
│   └── integration/
│
├── Dockerfile
├── requirements.txt
└── .github/
    └── workflows/
        └── ci.yml

Notes

Passwords are securely hashed and never stored in plain text.

Integration tests use a real PostgreSQL instance to ensure correctness.

The project follows FastAPI best practices for modularity and clarity.
The CI workflow ensures consistent test execution across all pushes.