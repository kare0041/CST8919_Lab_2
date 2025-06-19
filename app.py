from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # In a real application, you would check credentials against a database
    if username == 'admin' and password == 'password123':
        # Log successful login
        print(f"INFO: Successful login for user: {username}")
        return jsonify({"message": "Login successful"}), 200
    else:
        # Log failed login
        print(f"WARNING: Failed login attempt for user: {username}")
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True) 