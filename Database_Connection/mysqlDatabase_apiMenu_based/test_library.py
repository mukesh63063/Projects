import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"

# Fixture to set up a test book and return its ID
@pytest.fixture(scope="module")
def book_id():
    # Add a test book
    data = {"title": "Test Book", "author": "Test Author", "genre": "Fiction"}
    add_response = requests.post(f"{BASE_URL}/add_book", json=data)
    assert add_response.status_code == 201, "Failed to add test book"

    # Fetch the book ID from the /books endpoint (since /add_book doesn't return it)
    books_response = requests.get(f"{BASE_URL}/books")
    assert books_response.status_code == 200
    books = books_response.json()
    assert len(books) > 0, "No books found after adding"
    return books[0]["id"]  # Return the ID of the first book

def test_get_books():
    response = requests.get(f"{BASE_URL}/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_search_books():
    response = requests.get(f"{BASE_URL}/search", params={"query": "Test"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_borrow_book(book_id):
    response = requests.post(f"{BASE_URL}/borrow/{book_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Book borrowed successfully"

def test_return_book(book_id):
    # Ensure the book is borrowed first
    requests.post(f"{BASE_URL}/borrow/{book_id}")
    response = requests.post(f"{BASE_URL}/return/{book_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Book returned successfully"

def test_add_book():
    data = {"title": "New Book", "author": "New Author", "genre": "New Genre"}
    response = requests.post(f"{BASE_URL}/add_book", json=data)
    assert response.status_code == 201
    assert response.json()["message"] == "Book added successfully"

def test_update_book(book_id):
    data = {"title": "Updated Book", "author": "Updated Author", "genre": "Updated Genre"}
    response = requests.put(f"{BASE_URL}/update_book/{book_id}", json=data)
    assert response.status_code == 200
    assert response.json()["message"] == "Book updated successfully"

def test_partial_update_book(book_id):
    data = {"title": "Partially Updated Book"}
    response = requests.patch(f"{BASE_URL}/partial_update_book/{book_id}", json=data)
    assert response.status_code == 200
    assert response.json()["message"] == "Book updated successfully"

def test_remove_book(book_id):
    response = requests.delete(f"{BASE_URL}/remove_book/{book_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Book removed successfully"

def test_login_success():
    data = {"username": "admin", "password": "admin123"}
    response = requests.post(f"{BASE_URL}/login", json=data)
    assert response.status_code == 200
    assert response.json()["message"] == "Login successful"

def test_login_failure():
    data = {"username": "wrong", "password": "wrong"}
    response = requests.post(f"{BASE_URL}/login", json=data)
    assert response.status_code == 400
    assert response.json()["error"] == "Invalid username or password"