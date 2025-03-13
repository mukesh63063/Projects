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

# Create table if it doesn't exist                                                                      CREATE TABLE IF NOT EXISTS books
cursor.execute("""
    create table if not exists books(                                            
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        author VARCHAR(255),
        year INT
    )
""")

# Insert data into the table
insert_query = "INSERT INTO books (title, author, year) VALUES (%s, %s, %s)"
data = [
    ("GenAI", "Omkar", 1900)
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


# Basic commands 
# ----------------
# First Open cmd or any eviroment, if you use cmd then execute this command <mysql -u root -p >. You use instead root your database name. And enter your database password.
# show databases;
# use database name;
# show tables;
# select * from tableName;

