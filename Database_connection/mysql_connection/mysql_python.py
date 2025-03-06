# Step 1: Import required library
import mysql.connector

# Step 2: Take authentication details
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456789',
    'database': 'library_database'
}

# Establish a connection
conn = mysql.connector.connect(**db_config)

# Step 3: Create table (if not exists) and insert data
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        author VARCHAR(255),
        year INT
    )
""")

# Insert data into the table
insert_query = "INSERT INTO books (title, author, year) VALUES (%s, %s, %s)"
data = [
    ("The Alchemist", "Paulo Coelho", 1988),
    ("1984", "George Orwell", 1949),
    ("To Kill a Mockingbird", "Harper Lee", 1960),
    ('Data science', 'Denial', 2025)
]

cursor.executemany(insert_query, data)  # Insert multiple rows

# Step 4: Update and fetch data
update_query = "UPDATE books SET year = 1990 WHERE title = 'The Alchemist'"
cursor.execute(update_query)

# Fetch all data
cursor.execute("SELECT * FROM books")
records = cursor.fetchall()
print("\nBook Records:")
for row in records:
    print(row)

# Step 5: Commit changes and close connection
conn.commit()
cursor.close()
conn.close()
print("\n Database operation completed successfully!")


'''
Output
------
Book Records:
(1, 'The Alchemist', 'Paulo Coelho', 1990)
(2, '1984', 'George Orwell', 1949)
(3, 'To Kill a Mockingbird', 'Harper Lee', 1960)
(4, 'The Alchemist', 'Paulo Coelho', 1990)
(5, '1984', 'George Orwell', 1949)
(6, 'To Kill a Mockingbird', 'Harper Lee', 1960)
(7, 'The Alchemist', 'Paulo Coelho', 1990)
(8, '1984', 'George Orwell', 1949)
(9, 'To Kill a Mockingbird', 'Harper Lee', 1960)
(10, 'Data science', 'Denial', 2025)
(11, 'The Alchemist', 'Paulo Coelho', 1990)
(12, '1984', 'George Orwell', 1949)
(13, 'To Kill a Mockingbird', 'Harper Lee', 1960)
(14, 'Data science', 'Denial', 2025)
(15, 'The Alchemist', 'Paulo Coelho', 1990)
(16, '1984', 'George Orwell', 1949)
(17, 'To Kill a Mockingbird', 'Harper Lee', 1960)
(18, 'Data science', 'Denial', 2025)

 Database operation completed successfully!

'''



