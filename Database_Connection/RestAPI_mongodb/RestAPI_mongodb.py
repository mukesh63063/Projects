from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Database Connection
authentication = {
    "host": "localhost",
    "port": 27017,
    "database": "library_database"
}

def get_db_connection():
    client = MongoClient(host=authentication['host'], port=authentication['port'])
    return client[authentication['database']]

# Initialize Database (MongoDB doesn't require explicit table creation)
def initialize_db():
    db = get_db_connection()
    # In MongoDB, collections are created automatically when data is inserted
    # We can ensure the collection exists by checking or creating an index if needed
    db.payslip.create_index("emp_id", unique=True)  # Optional: Ensure emp_id is unique
    # No need to define schema beforehand as MongoDB is schemaless

# Route: Get all payslip records
@app.route('/payslip', methods=['GET'])
def get_payslips():
    db = get_db_connection()
    records = db.payslip.find()  # Fetch all documents from payslip collection
    result = [
        {
            "emp_id": r["emp_id"],
            "emp_first_name": r["emp_first_name"],
            "emp_last_name": r["emp_last_name"],
            "emp_salary": float(r["emp_salary"])  # Convert Decimal to float for JSON
        } for r in records
    ]
    return jsonify(result)

# Route: Get a single payslip by emp_id
@app.route('/payslip/<int:emp_id>', methods=['GET'])
def get_payslip(emp_id):
    db = get_db_connection()
    record = db.payslip.find_one({"emp_id": emp_id})  # Find document by emp_id

    if record:
        result = {
            "emp_id": record["emp_id"],
            "emp_first_name": record["emp_first_name"],
            "emp_last_name": record["emp_last_name"],
            "emp_salary": float(record["emp_salary"])  # Convert Decimal to float
        }
        return jsonify(result)
    else:
        return jsonify({"error": "Payslip not found"}), 404

# Route: Add a new payslip record
@app.route('/payslip', methods=['POST'])
def add_payslip():
    data = request.json
    db = get_db_connection()

    try:
        # Insert document into payslip collection
        payslip_data = {
            "emp_id": data["emp_id"],
            "emp_first_name": data["emp_first_name"],
            "emp_last_name": data["emp_last_name"],
            "emp_salary": data["emp_salary"]
        }
        db.payslip.insert_one(payslip_data)
    except Exception as err:
        return jsonify({"error": str(err)}), 400

    return jsonify({"message": "Payslip added successfully"}), 201

# Route: Update an employee's salary
@app.route('/payslip/<int:emp_id>', methods=['PUT'])
def update_salary(emp_id):
    data = request.json
    db = get_db_connection()

    # Update document in payslip collection
    result = db.payslip.update_one(
        {"emp_id": emp_id},
        {"$set": {"emp_salary": data["emp_salary"]}}
    )

    if result.matched_count > 0:
        return jsonify({"message": "Salary updated successfully"})
    else:
        return jsonify({"error": "Payslip not found"}), 404

# Route: Delete a payslip record
@app.route('/payslip/<int:emp_id>', methods=['DELETE'])
def delete_payslip(emp_id):
    db = get_db_connection()

    # Delete document from payslip collection
    result = db.payslip.delete_one({"emp_id": emp_id})

    if result.deleted_count > 0:
        return jsonify({"message": "Payslip deleted successfully"})
    else:
        return jsonify({"error": "Payslip not found"}), 404

if __name__ == '__main__':
    initialize_db()  # Ensure DB is ready
    app.run(debug=True)