from flask import Flask, jsonify, request

app = Flask(__name__)

orders = []

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    orders.append(data)
    return jsonify({"message": "Order created!", "order": data})

@app.route('/orders', methods=['GET'])
def list_orders():
    return jsonify(orders)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
