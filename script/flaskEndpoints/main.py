from flask import Flask, jsonify, request
import snowflake.connector

app = Flask(__name__)

# Конфигурация за връзка със Snowflake
SNOWFLAKE_CONFIG = {
    "user": "your_user",
    "password": "your_password",
    "account": "your_account",
    "warehouse": "your_warehouse",
    "database": "your_database",
    "schema": "your_schema"
}

def get_snowflake_connection():
    return snowflake.connector.connect(**SNOWFLAKE_CONFIG)

# Функция за изпълнение на SQL заявки
def execute_query(query, params=None, fetch_one=False):
    conn = get_snowflake_connection()
    cursor = conn.cursor()
    cursor.execute(query, params or [])
    result = cursor.fetchone() if fetch_one else cursor.fetchall()
    cursor.close()
    conn.close()
    return result

# ------------------ GET заявки ------------------
@app.route('/attractions', methods=['GET'])
def get_attractions():
    query = "SELECT * FROM attractions"
    results = execute_query(query)
    return jsonify(results)

@app.route('/attractions/<int:id>', methods=['GET'])
def get_attraction(id):
    query = "SELECT * FROM attractions WHERE id = %s"
    result = execute_query(query, (id,), fetch_one=True)
    if not result:
        return jsonify({"error": "Not Found"}), 404
    return jsonify(result)

@app.route('/employees', methods=['GET'])
def get_employees():
    query = "SELECT * FROM employees"
    results = execute_query(query)
    return jsonify(results)

@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    query = "SELECT * FROM employees WHERE id = %s"
    result = execute_query(query, (id,), fetch_one=True)
    if not result:
        return jsonify({"error": "Not Found"}), 404
    return jsonify(result)

@app.route('/sales', methods=['GET'])
def get_sales():
    query = "SELECT * FROM sales"
    results = execute_query(query)
    return jsonify(results)

@app.route('/sales/<int:id>', methods=['GET'])
def get_sale(id):
    query = "SELECT * FROM sales WHERE id = %s"
    result = execute_query(query, (id,), fetch_one=True)
    if not result:
        return jsonify({"error": "Not Found"}), 404
    return jsonify(result)

@app.route('/tickets', methods=['GET'])
def get_tickets():
    query = "SELECT * FROM tickets"
    results = execute_query(query)
    return jsonify(results)

@app.route('/tickets/<int:id>', methods=['GET'])
def get_ticket(id):
    query = "SELECT * FROM tickets WHERE id = %s"
    result = execute_query(query, (id,), fetch_one=True)
    if not result:
        return jsonify({"error": "Not Found"}), 404
    return jsonify(result)

@app.route('/events', methods=['GET'])
def get_events():
    query = "SELECT * FROM events"
    results = execute_query(query)
    return jsonify(results)

@app.route('/events/<int:id>', methods=['GET'])
def get_event(id):
    query = "SELECT * FROM events WHERE id = %s"
    result = execute_query(query, (id,), fetch_one=True)
    if not result:
        return jsonify({"error": "Not Found"}), 404
    return jsonify(result)

@app.route('/visitors', methods=['GET'])
def get_visitors():
    query = "SELECT * FROM visitors"
    results = execute_query(query)
    return jsonify(results)

@app.route('/visitors/<int:id>', methods=['GET'])
def get_visitor(id):
    query = "SELECT * FROM visitors WHERE id = %s"
    result = execute_query(query, (id,), fetch_one=True)
    if not result:
        return jsonify({"error": "Not Found"}), 404
    return jsonify(result)

@app.route('/financial', methods=['GET'])
def get_financial():
    query = "SELECT * FROM financial"
    results = execute_query(query)
    return jsonify(results)

@app.route('/financial/<int:id>', methods=['GET'])
def get_financial_record(id):
    query = "SELECT * FROM financial WHERE id = %s"
    result = execute_query(query, (id,), fetch_one=True)
    if not result:
        return jsonify({"error": "Not Found"}), 404
    return jsonify(result)

# ------------------ POST заявки ------------------
@app.route('/tickets', methods=['POST'])
def create_ticket():
    data = request.get_json()
    query = "INSERT INTO tickets (visitor_id, attraction_id, price) VALUES (%s, %s, %s)"
    execute_query(query, (data['visitor_id'], data['attraction_id'], data['price']))
    return jsonify({"message": "Ticket created successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
