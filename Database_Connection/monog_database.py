# Step 1: Import required library
from pymongo import MongoClient

# Step 2: Take authentication details
db_config = {
    'host': 'localhost',
    'port': 27017,  # default MongoDB port
    'database': 'library_database'
}

# Establish a connection
client = MongoClient(host=db_config['host'],
                     port=db_config['port']
                )
db = client[db_config['database']]

# Step 3: Create collection (if not exists) and insert data
books_collection = db['books']  # MongoDB uses collections instead of tables

# Insert data into the collection
data = [
    {"title": "DevOps", "author": "Mukesh Amabani", "year": 2025}
]

# Insert multiple documents (equivalent to rows)
insert_result = books_collection.insert_many(data)
print(f"Inserted document IDs: {insert_result.inserted_ids}")

# Step 4: Update and fetch data
# Update document (similar to UPDATE in SQL)
update_query = {"title": "The Alchemist"}
update_values = {"$set": {"year": 1990}}
books_collection.update_one(update_query, update_values)

# Fetch all data (similar to SELECT * FROM)
records = books_collection.find()
print("\nBook Records:")
for record in records:
    print(record)

# Step 5: Close connection
client.close()
print("\nDatabase operation completed successfully!")