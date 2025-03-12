# Flask MySQL REST API

## Project Overview
This project is a REST API built using Flask and MySQL to manage employee payslip records. It supports CRUD operations and includes automated testing with `pytest`.

## Prerequisites
- Python 3.12+
- MySQL Server
- Postman (for testing API requests)
- Virtual environment (recommended)

## Setup Instructions
### 1. Clone the Repository
```sh
 git clone <repository-url>
 cd <repository-folder>
```

### 2. Create a Virtual Environment
```sh
python -m venv venv
```
Activate it:
- **Windows (PowerShell)**: `venv\Scripts\activate`
- **Linux/Mac**: `source venv/bin/activate`

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Configure the Database
Modify the `authentication` dictionary in `database_connection_restAPI.py` with your MySQL credentials:
```python
authentication = {
    "host": "localhost",
    "user": "root",
    "password": "your_password",
    "database": "library_database"
}
```
Run the script to initialize the database:
```sh
python database_connection_restAPI.py
```

### 5. Run the Flask API
```sh
python database_connection_restAPI.py
```
The server will start at `http://127.0.0.1:5000`.

## API Endpoints
| Method | Endpoint             | Description |
|--------|----------------------|-------------|
| GET    | `/payslip`           | Get all payslips |
| GET    | `/payslip/<emp_id>`  | Get a specific payslip by ID |
| POST   | `/payslip`           | Add a new payslip |
| PUT    | `/payslip/<emp_id>`  | Update an employee's salary |
| DELETE | `/payslip/<emp_id>`  | Delete a payslip |

### Example Requests (Using Postman or cURL)
#### Get all payslips:
```sh
GET http://127.0.0.1:5000/payslip
```
#### Add a new payslip:
```sh
POST http://127.0.0.1:5000/payslip
Content-Type: application/json

{
    "emp_id": 3,
    "emp_first_name": "John",
    "emp_last_name": "Doe",
    "emp_salary": 50000
}
```

## Running Tests
This project includes `pytest` for unit testing.

### Install `pytest`
```sh
pip install pytest
```

### Run the Tests
```sh
pytest test_mysql_restAPI.py -v
```
If all tests pass, the output will confirm success.

## Troubleshooting
- If you get `ModuleNotFoundError: No module named 'mysql'`, install MySQL Connector:
  ```sh
  pip install mysql-connector-python
  ```
- If the database is not found, ensure MySQL is running and `library_database` exists.

## License
This project is licensed under the MIT License.

