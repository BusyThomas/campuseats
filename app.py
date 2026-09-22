import hashlib
from flask import request, jsonify, Response

# --- Caching & Idempotency Helpers ---

idempotency_cache = {}

def generate_etag(data_dict):
    """Generate an MD5 hash of the dictionary to use as an ETag."""
    # Ensure stable sorting so identical dictionaries produce the same hash
    data_string = str(sorted(data_dict.items())).encode('utf-8')
    return hashlib.md5(data_string).hexdigest()


# --- Route Implementations ---

@app.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    order = store.get_order(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
        
    current_etag = generate_etag(order)
    client_etag = request.headers.get('If-None-Match')
    
    # Return 304 if the client already has the latest version
    if client_etag == current_etag:
        return Response(status=304)
        
    response = jsonify(order)
    response.headers['ETag'] = current_etag
    return response, 200


@app.route('/orders/<order_id>', methods=['PUT'])
def update_order(order_id):
    order = store.get_order(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    current_etag = generate_etag(order)
    client_etag = request.headers.get('If-Match')

    # Return 412 if the client is trying to update an outdated version
    if client_etag and client_etag != current_etag:
        return jsonify({"error": "Precondition Failed: ETag mismatch"}), 412

    update_data = request.json
    updated_order = store.update_order(order_id, update_data)
    
    new_etag = generate_etag(updated_order)
    response = jsonify(updated_order)
    response.headers['ETag'] = new_etag
    return response, 200


@app.route('/orders', methods=['POST'])
def create_order():
    idempotency_key = request.headers.get('Idempotency-Key')
    
    # Check for a cached response using the Idempotency-Key
    if idempotency_key and idempotency_key in idempotency_cache:
        cached = idempotency_cache[idempotency_key]
        return jsonify(cached['body']), cached['status']

    order_data = request.json
    new_order = store.create_order(order_data)
    
    # Cache the successful response to prevent future duplicates
    if idempotency_key:
        idempotency_cache[idempotency_key] = {
            'body': new_order,
            'status': 201
        }
        
    return jsonify(new_order), 201
