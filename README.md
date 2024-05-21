# Authentication API

This is a simple Flask-based authentication API that allows users to sign up and log in. The API uses SQLite for the database, Flask-Bcrypt for password hashing, and Flask-JWT-Extended for handling JSON Web Tokens (JWT).

## Features

- User registration (sign up)
- User authentication (log in)
- Password hashing
- JWT token generation for authenticated users

## Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-RESTful
- Flask-JWT-Extended
- Flask-Bcrypt
- SQLAlchemy-serializer
- Pipenv

## Setup

1. Clone the repository:

```bash
git clone
```

2. Create a virtual environment and activate it

```bash
pipenv install
pipenv shell
```

3. Run the migrations.

```bash
flask db upgrade head
```

4. Set up the environment variables:

```bash
export FLASK_APP=app.py
export FLASK_RUN_PORT=5555
```

The application will be running `http://127.0.0.1:5555/`

## API Endpoints

### Sign Up

- **URL:** `/signup`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "username": "your_username",
        "password": "your_password"
    }
    ```
- **Response:**
    - **Success (201):**
        ```json
        {
            "id": 1,
            "username": "your_username"
        }
        ```
    - **Failure (400):**
        ```json
        {
            "message": "Error message"
        }
        ```

### Log In

- **URL:** `/login`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "username": "your_username",
        "password": "your_password"
    }
    ```
- **Response:**
    - **Success (200):**
        ```json
        {
            "message": "Logged In Successfully",
            "access_token": "jwt_token"
        }
        ```
    - **Failure (401):**
        ```json
        {
            "message": "Login Failed"
        }
        ```


