import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"

# Test getting all payslips
def test_get_all_payslips():
    response = requests.get(f"{BASE_URL}/payslip")
    assert response.status_code == 200

# Test adding a new payslip
def test_add_payslip():
    payload = {
        "emp_id": 4,
        "emp_first_name": "John",
        "emp_last_name": "Doe",
        "emp_salary": 50000
    }
    response = requests.post(f"{BASE_URL}/payslip", json=payload)
    assert response.status_code == 201

# Test getting a specific payslip
def test_get_payslip_by_id():
    response = requests.get(f"{BASE_URL}/payslip/4")  # ID must exist in DB
    assert response.status_code == 200

# Test updating salary
def test_update_salary():
    payload = {"emp_salary": 55000}
    response = requests.put(f"{BASE_URL}/payslip/4", json=payload)
    assert response.status_code == 200

# Test deleting a payslip
def test_delete_payslip():
    response = requests.delete(f"{BASE_URL}/payslip/4")
    assert response.status_code == 200
