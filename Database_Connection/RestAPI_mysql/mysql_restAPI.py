from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database Connection
authentication = {
    "host": "localhost",
    "user": "root",
    "password": "123456789",
    "database": "library_database"
}


def get_db_connection():
    return mysql.connector.connect(**authentication)


# Initialize Database
def initialize_db():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS payslip (
            emp_id INT PRIMARY KEY,
            emp_first_name VARCHAR(25),
            emp_last_name VARCHAR(25),
            emp_salary NUMERIC
        )
    """)

    connection.commit()
    cursor.close()
    connection.close()


# Route: Get all payslip records
@app.route('/payslip', methods=['GET'])
def get_payslips():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM payslip")
    records = cursor.fetchall()
    cursor.close()
    connection.close()

    result = [{"emp_id": r[0], "emp_first_name": r[1], "emp_last_name": r[2], "emp_salary": r[3]} for r in records]
    return jsonify(result)


# Route: Get a single payslip by emp_id
@app.route('/payslip/<int:emp_id>', methods=['GET'])
def get_payslip(emp_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM payslip WHERE emp_id = %s", (emp_id,))
    record = cursor.fetchone()

    cursor.close()
    connection.close()

    if record:
        result = {
            "emp_id": record[0],
            "emp_first_name": record[1],
            "emp_last_name": record[2],
            "emp_salary": record[3]
        }
        return jsonify(result)
    else:
        return jsonify({"error": "Payslip not found"}), 404


# Route: Add a new payslip record
@app.route('/payslip', methods=['POST'])
def add_payslip():
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        insert_query = "INSERT INTO payslip (emp_id, emp_first_name, emp_last_name, emp_salary) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query,
                       (data["emp_id"], data["emp_first_name"], data["emp_last_name"], data["emp_salary"]))
        connection.commit()
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 400
    finally:
        cursor.close()
        connection.close()

    return jsonify({"message": "Payslip added successfully"}), 201


# Route: Update an employee's salary
@app.route('/payslip/<int:emp_id>', methods=['PUT'])
def update_salary(emp_id):
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()

    update_query = "UPDATE payslip SET emp_salary = %s WHERE emp_id = %s"
    cursor.execute(update_query, (data["emp_salary"], emp_id))
    connection.commit()

    cursor.close()
    connection.close()
    return jsonify({"message": "Salary updated successfully"})


# Route: Delete a payslip record
@app.route('/payslip/<int:emp_id>', methods=['DELETE'])
def delete_payslip(emp_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    delete_query = "DELETE FROM payslip WHERE emp_id = %s"
    cursor.execute(delete_query, (emp_id,))
    connection.commit()

    cursor.close()
    connection.close()
    return jsonify({"message": "Payslip deleted successfully"})


if __name__ == '__main__':
    initialize_db()  # Ensure DB is ready
    app.run(debug=True)
