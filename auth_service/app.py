from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    return jsonify({"message": f"User {data['username']} registered!"})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    return jsonify({"token": "fake-jwt-token-for-" + data['username']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
