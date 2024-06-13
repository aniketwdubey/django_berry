Strawberry GraphQL + Django: Simplify book database management with this powerful integration.

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

The project structure is as follows:


- `book/`: Contains the Django app for adding, updating, deleting books.
- `django_berry/`: Main project directory.
- `db.sqlite3`: SQLite database file.
- `manage.py`: Django's command-line utility for administrative tasks.

## Features

- Users can add, update, delete books.
- **GraphQL API**: The API is implemented using the Strawberry framework, providing a GraphQL endpoint for interacting with the blog data.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/django_berry.git
    ```

2. Navigate to the project directory:

    ```bash
    cd django_berry
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Apply migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```


## Usage

1. Run the development server:

    ```bash
    python manage.py runserver
    ```

2. Access the GraphQL endpoint at `http://localhost:8000/graphql/` to interact with the API.
   Perform CRUD Operations using GraphQL API


## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature-name`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


