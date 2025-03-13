# Library Management System

A simple Flask-based REST API for managing a library database, with a command-line client and automated tests using Robot Framework and Pytest.

## Overview

This project consists of:
- **app.py**: Flask API server for managing books (CRUD operations, borrow/return, login).
- **client.py**: Command-line interface to interact with the API.
- **test_library.robot**: Automated tests using Robot Framework.
- **test_library.py**: Automated tests using Pytest.
- **requirements.txt**: List of Python dependencies.

The system uses a MySQL database (`library_database`) with a `post_man` table to store book information.

## Prerequisites

- Python 3.12+
- MySQL server (e.g., MySQL 8.0+)
- Virtual environment (recommended)

## Setup

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
