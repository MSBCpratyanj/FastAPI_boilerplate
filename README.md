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
1. **Clone the repository:**
   ```sh
   git clone https://github.com/MSBCpratyanj/FastAPI_boilerplate.git
   cd FastAPI_boilerplate
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
   or
    ```sh
   uv add -r requirements.txt
   ```

3. **Set up environment variables:**
   Copy `.env.example` to `.env` and update the necessary values.

4. **Run the application:**
   ```sh
   uvicorn main:app --reload
   ```
   For UV
   ```sh
   uv run uvicorn main:app --reload
   ```

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
  - **Create a new migration:**
    ```sh
    alembic revision --autogenerate -m "Initial migration"
    ```
  - **Apply migrations:**
    ```sh
    alembic upgrade head
    ```

