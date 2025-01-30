# FastAPI Application

This is a simple FastAPI application to demonstrate the basics of FastAPI, including creating endpoints, handling requests, and managing dependencies using Poetry.

## Prerequisites

- Python 3.8 or higher
- Poetry

## Installation

1. **Install Poetry**: If you haven't already installed Poetry, you can do so by pasting the below command in your terminal:
   ```sh
   pip install poetry
   ```
   or 

   ```sh
   curl -sSL https://install.python-poetry.org | python -
   ```


2. **Clone the repository**:
   ```sh
   git clone https://github.com/deedee-code/Python-Journey.git
   cd into this folder
   ```

3. **Initialize the Poetry project**: If the project has not been initialized with Poetry yet, run the following command to create a `pyproject.toml` file:
   ```sh
   poetry init
   ```
   Follow the prompts to complete the initialization process.

4. **Install the dependencies**:
   ```sh
   poetry install
   ```

5. **Activate the virtual environment**:
   ```sh
   poetry shell
   ```

## Running the Application

To run the FastAPI application, use the following command:
```sh
poetry run uvicorn main:app --reload
```

This will start the FastAPI server on `http://127.0.0.1:8000`.

To view the documentation, open `http://127.0.0.1:8000/docs`.


- **data.py**: Contains user dummy data.
- **main.py**: Contains the FastAPI application with various endpoints.
- **validators.py**: Contains the Pydantic models for request validation.
- **pyproject.toml**: Contains the project dependencies and configuration for Poetry.

## Endpoints

### GET /
Returns a greeting message.

### GET /users
Returns a list of all users.

### GET /users/
Returns users by gender using query parameters.

### GET /users/{user_age}
Returns a user by their age.

### POST /create-user
Creates a new user using a Pydantic model.

### PATCH /users/{user}
Updates an existing user's information using the request body.

### DELETE /users/delete_user/{user_name}
Deletes a user by their name.

### GET /users/search/
Search user by keyword

### POST /users/create_user
Create multiple users

### GET /users/count/
Count users by gender

## Adding Dependencies

To add new dependencies to the project, use the following command:
```sh
poetry add <package-name>
```

To add development dependencies, use:
```sh
poetry add --dev <package-name>
```

## License

This project is licensed under the MIT License.
