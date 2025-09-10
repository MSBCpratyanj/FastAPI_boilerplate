# FastAPI Project - Backend

## Description
This is a boilerplate project for building a backend using FastAPI. It includes essential configurations, modules, and utilities to get you started quickly.

## Features
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **Docker**: Containerization support for easy deployment.
- **Alembic**: Database migration tool.
- **Pydantic**: Data validation and parsing using Python type annotations.
- **SQLAlchemy**: ORM for database interactions.
- **Security**: Basic authentication and authorization using JWT tokens.
- **Logging**: Configured logging for better debugging and monitoring.

## Installation

### Option 1: Using `pip`

1.  **Create virtual environment**
    ``` sh
    python -m venv .venv
    ```
2.  **Activate environment**

    ``` sh
    .venv\Scripts\activate   # Windows
    source .venv/bin/activate  # Linux/Mac
    ```

3.  **Install dependencies**

    ``` sh
    pip install -r requirements.txt
    ```

4.  **Set up environment variables**

    -   Update `.env` with your configuration values (DB URL, JWT
        secret, etc.).

------------------------------------------------------------------------

### Option 2: Using `uv` (recommended ⚡)

[`uv`](https://github.com/astral-sh/uv) is a modern, fast Python package
manager.

1.  **Initialize environment**

    ``` sh
    uv init
    ```

2.  **Install dependencies**

    ``` sh
    uv add -r requirements.txt
    ```

3.  **Run the app**

    ``` sh
    uv run uvicorn main:app --reload
    ```

✅ `uv` automatically handles virtual environments, caching, and
dependency resolution.
## Usage
- **API Endpoints:**
  - **Auth Module:**
    - `/auth/login`: POST - User login
    - `/auth/register`: POST - User registration
  - **User Module:**
    - `/user/list`: GET - List all users
    - `/user/create`: POST - Create a new user
    - `/user/{user_id}`: GET - Get user details by ID

- **Database Migrations:**
  - **Create alembic init:**
    ```sh
    alembic init app/alembic
    ```
  - **Create a new migration:**
    ```sh
    alembic revision --autogenerate -m "Initial migration"
    ```
  - **Apply migrations:**
    ```sh
    alembic upgrade head
    ```
## Code Linting
We use Ruff to keep our Python code clean and consistent.

### Run the following commands to use Ruff:

```sh
pip install ruff      # Install Ruff

python -m ruff --version    # Check Ruff version

python -m ruff check        # Lint all Python files

python -m ruff check --fix  # Automatically fix issues
```

