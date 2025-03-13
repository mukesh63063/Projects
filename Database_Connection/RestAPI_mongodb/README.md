# Flask MongoDB Payslip API

This is a simple RESTful API built with Flask and MongoDB to manage employee payslip records. It supports CRUD (Create, Read, Update, Delete) operations for payslip data.

## Features
- **GET /payslip**: Retrieve all payslip records.
- **GET /payslip/<emp_id>**: Retrieve a specific payslip by employee ID.
- **POST /payslip**: Add a new payslip record.
- **PUT /payslip/<emp_id>**: Update an employee's salary.
- **DELETE /payslip/<emp_id>**: Delete a payslip record.

## Prerequisites
- Python 3.8+
- MongoDB installed and running locally
- `mongosh` or `mongo` shell (optional, for manual database interaction)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
