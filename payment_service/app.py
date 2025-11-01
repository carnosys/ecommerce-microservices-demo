from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/pay', methods=['POST'])
def pay():
    data = request.json
    return jsonify({"status": "Payment successful", "amount": data.get("amount")})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
