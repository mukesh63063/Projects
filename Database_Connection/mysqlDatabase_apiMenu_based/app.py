from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="library_database"
)

@app.route('/books', methods=['GET'])
def get_books():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM post_man WHERE status = 'available'")
    books = cursor.fetchall()
    return jsonify(books)

@app.route('/search', methods=['GET'])
def search_books():
    query = request.args.get('query')
    cursor = db.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM post_man WHERE title LIKE %s OR author LIKE %s OR genre LIKE %s",
        (f"%{query}%", f"%{query}%", f"%{query}%")
    )
    books = cursor.fetchall()
    return jsonify(books)

@app.route('/borrow/<int:book_id>', methods=['POST'])
def borrow_book(book_id):
    cursor = db.cursor()
    cursor.execute("UPDATE post_man SET status = 'borrowed' WHERE id = %s AND status = 'available'", (book_id,))
    db.commit()
    if cursor.rowcount > 0:
        return jsonify({"message": "Book borrowed successfully"}), 200
    else:
        return jsonify({"error": "Book is already borrowed or does not exist"}), 400

@app.route('/return/<int:book_id>', methods=['POST'])
def return_book(book_id):
    cursor = db.cursor()
    cursor.execute("UPDATE post_man SET status = 'available' WHERE id = %s AND status = 'borrowed'", (book_id,))
    db.commit()
    if cursor.rowcount > 0:
        return jsonify({"message": "Book returned successfully"}), 200
    else:
        return jsonify({"error": "Book is not borrowed or does not exist"}), 400

@app.route('/add_book', methods=['POST'])
def add_book():
    data = request.json
    cursor = db.cursor()
    query = "INSERT INTO post_man (title, author, genre, status) VALUES (%s, %s, %s, 'available')"
    values = (data['title'], data['author'], data['genre'])
    cursor.execute(query, values)
    db.commit()
    if cursor.rowcount > 0:
        return jsonify({"message": "Book added successfully"}), 201
    else:
        return jsonify({"error": "Failed to add book"}), 400

@app.route('/update_book/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    cursor = db.cursor()
    query = "UPDATE post_man SET title = %s, author = %s, genre = %s WHERE id = %s"
    values = (data['title'], data['author'], data['genre'], book_id)
    cursor.execute(query, values)
    db.commit()
    if cursor.rowcount > 0:
        return jsonify({"message": "Book updated successfully"}), 200
    else:
        return jsonify({"error": "Failed to update book or book does not exist"}), 400

@app.route('/partial_update_book/<int:book_id>', methods=['PATCH'])
def partial_update_book(book_id):
    data = request.json
    cursor = db.cursor()
    fields_to_update = []
    values = []

    if 'title' in data:
        fields_to_update.append("title = %s")
        values.append(data['title'])
    if 'author' in data:
        fields_to_update.append("author = %s")
        values.append(data['author'])
    if 'genre' in data:
        fields_to_update.append("genre = %s")
        values.append(data['genre'])

    if fields_to_update:
        query = f"UPDATE post_man SET {', '.join(fields_to_update)} WHERE id = %s"
        values.append(book_id)
        cursor.execute(query, tuple(values))
        db.commit()
        if cursor.rowcount > 0:
            return jsonify({"message": "Book updated successfully"}), 200
        else:
            return jsonify({"error": "Failed to update book or book does not exist"}), 400
    else:
        return jsonify({"error": "No fields to update"}), 400

@app.route('/remove_book/<int:book_id>', methods=['DELETE'])
def remove_book(book_id):
    cursor = db.cursor()
    query = "DELETE FROM post_man WHERE id = %s"
    cursor.execute(query, (book_id,))
    db.commit()
    if cursor.rowcount > 0:
        return jsonify({"message": "Book removed successfully"}), 200
    else:
        return jsonify({"error": "Failed to remove book or book does not exist"}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if data and data['username'] == 'admin' and data['password'] == 'admin123':
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 400

if __name__ == '__main__':
    app.run(debug=True)
