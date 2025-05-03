from flask import Flask, request, jsonify

app = Flask(__name__)
users = {'user1': 'password123', 'user2': 'securepass'}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if username in users and users[username] == password:
        # Trả token giả định; thực tế nên dùng JWT
        return jsonify({'message': 'Login successful', 'token': 'fake-jwt-token'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/validate', methods=['POST'])
def validate_token():
    token = request.headers.get('Authorization')
    if token == 'fake-jwt-token':
        return jsonify({'valid': True}), 200
    return jsonify({'valid': False}), 401

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
