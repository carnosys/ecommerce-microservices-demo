import redis
from flask import Flask, request, jsonify

app = Flask(__name__)

# Connect to the redis_cache service (Docker Compose hostname = service name)
r = redis.Redis(host='redis_cache', port=6379, decode_responses=True)

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json
    email = data.get('email')
    # Example usage: push to Redis queue
    r.publish('notifications', f"Send email to {email}")
    return jsonify({"message": f"Notification queued for {email}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006)
