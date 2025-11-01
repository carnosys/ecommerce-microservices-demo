from flask import Flask, jsonify, request, Response
import requests
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Use the exact hostnames that Docker Compose provides.
# Option A (recommended): use service names from docker-compose (e.g. product_service).
# Option B: if you prefer container_name values (product-service), use those instead.
SERVICE_MAP = {
    'auth':    ('auth_service', 5001),
    'user':    ('user_service', 5002),
    'product': ('product_service', 5003),
    'order':   ('order_service', 5004),
    'payment': ('payment_service', 5005),
    'notify':  ('notification_service', 5006),
}

# If you want default root paths for short aliases (so /product returns /products), set defaults:
DEFAULT_PATHS = {
    'product': '/products',
    'user': '/users',
    'order': '/orders',
    'notify': '/notify',
    'payment': '/pay',
    'auth': '/',   # auth will expect explicit paths like /login or /signup
}

def forward_request(service_host, service_port, path):
    url = f'http://{service_host}:{service_port}{path}'
    logging.info(f"Forwarding {request.method} {request.path} -> {url}")
    # build headers excluding Host
    headers = {k: v for k, v in request.headers.items() if k.lower() != 'host'}
    try:
        resp = requests.request(
            method=request.method,
            url=url,
            headers=headers,
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False,
            params=request.args,
            timeout=5
        )
    except requests.exceptions.RequestException as e:
        logging.error(f"Error forwarding to {url}: {e}")
        return jsonify({"error": "upstream service unavailable", "detail": str(e)}), 502

    # Filter out hop-by-hop headers
    excluded = {'content-encoding', 'content-length', 'transfer-encoding', 'connection'}
    response_headers = [(name, value) for name, value in resp.headers.items() if name.lower() not in excluded]
    return Response(resp.content, resp.status_code, response_headers)

# Generic proxy for /<service>/<path>
@app.route('/<service>/<path:subpath>', methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"])
def proxy_with_path(service, subpath):
    if service not in SERVICE_MAP:
        return jsonify({"error": f"Unknown service '{service}'"}), 404
    host, port = SERVICE_MAP[service]
    return forward_request(host, port, f'/{subpath}')

# Root-proxy for /<service>  (for convenience, forwards to a default path if available)
@app.route('/<service>', methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"])
def proxy_root(service):
    if service not in SERVICE_MAP:
        return jsonify({"error": f"Unknown service '{service}'"}), 404
    host, port = SERVICE_MAP[service]
    default_path = DEFAULT_PATHS.get(service, '/')
    return forward_request(host, port, default_path)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the API Gateway"})

@app.route('/health')
def health():
    return jsonify({"status": "Gateway running"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
