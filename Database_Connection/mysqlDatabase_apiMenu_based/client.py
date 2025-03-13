import requests

BASE_URL = "http://127.0.0.1:5000"


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    response = requests.post(f"{BASE_URL}/login", json={"username": 'admin', "password": 'admin123'})
    if response.status_code == 200:
        print(response.json()["message"])
        main()
    else:
        print(response.json()["error"])
        login()

def view_books():
    response = requests.get(f"{BASE_URL}/books")
    if response.status_code == 200:
        books = response.json()
        print("\nAvailable Books:")
        for book in books:
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")
    else:
        print("Error fetching books.")

def search_books():
    query = input("Enter title, author, or genre to search: ")
    response = requests.get(f"{BASE_URL}/search", params={"query": query})
    if response.status_code == 200:
        books = response.json()
        if books:
            print("\nSearch Results:")
            for book in books:
                print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}")
        else:
            print("No books found.")
    else:
        print("Error searching books.")

def borrow_book():
    book_id = int(input("Enter the ID of the book to borrow: "))
    response = requests.post(f"{BASE_URL}/borrow/{book_id}")
    if response.status_code == 200:
        print(response.json()["message"])
    else:
        print(response.json()["error"])

def return_book():
    book_id = int(input("Enter the ID of the book to return: "))
    response = requests.post(f"{BASE_URL}/return/{book_id}")
    if response.status_code == 200:
        print(response.json()["message"])
    else:
        print(response.json()["error"])


def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    genre = input("Enter genre: ")
    response = requests.post(f"{BASE_URL}/add_book", json={"title": title, "author": author, "genre": genre})
    if response.status_code == 201:
        print(response.json()["message"])
    else:
        print("Error adding book.")

def update_book():
    book_id = int(input("Enter the ID of the book to update: "))
    title = input("Enter new title: ")
    author = input("Enter new author: ")
    genre = input("Enter new genre: ")
    response = requests.put(f"{BASE_URL}/update_book/{book_id}",
                            json={"title": title, "author": author, "genre": genre})
    if response.status_code == 200:
        print(response.json()["message"])
    else:
        print("Error updating book.")

def remove_book():
    book_id = int(input("Enter the ID of the book to remove: "))
    response = requests.delete(f"{BASE_URL}/remove_book/{book_id}")
    if response.status_code == 200:
        print(response.json()["message"])
    else:
        print("Error removing book.")

def main():
    while True:
        print("\nLibrary Management System")
        print("1. View Available Books")
        print("2. Search for a Book")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Add a New Book")
        print("6. Update Book Details")
        print("7. Remove a Book")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_books()
        elif choice == '2':
            search_books()
        elif choice == '3':
            borrow_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            add_book()
        elif choice == '6':
            update_book()
        elif choice == '7':
            remove_book()
        elif choice == '8':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    login()
