import unittest
import json
import uuid

# Import your Flask app and cache (adjust the import path based on your project structure)
from app import app, idempotency_cache

class TestIdempotency(unittest.TestCase):
    def setUp(self):
        """Set up a test client before each test."""
        app.testing = True
        self.client = app.test_client()
        
        # Clear the idempotency cache before each test to ensure a clean state
        idempotency_cache.clear()

    def test_idempotent_post_request(self):
        """Test that identical POST requests with the same Idempotency-Key return the cached response."""
        # 1. Setup mock order payload and generate a unique key
        payload = {
            "customer_name": "Test User",
            "items": [{"name": "Pizza", "quantity": 1}]
        }
        test_key = str(uuid.uuid4())
        headers = {
            "Content-Type": "application/json",
            "Idempotency-Key": test_key
        }

        # 2. Send the first POST request
        response_1 = self.client.post('/orders', data=json.dumps(payload), headers=headers)
        
        # Verify initial creation was successful
        self.assertEqual(response_1.status_code, 201)
        data_1 = json.loads(response_1.data)
        self.assertIn("customer_name", data_1)

        # 3. Send the exact same POST request with the same Idempotency-Key
        response_2 = self.client.post('/orders', data=json.dumps(payload), headers=headers)
        
        # 4. Verify the second response matches the first perfectly
        self.assertEqual(response_2.status_code, 201)
        data_2 = json.loads(response_2.data)
        
        # The IDs and content should be exactly the same, proving a duplicate wasn't created
        self.assertEqual(data_1, data_2)

    def test_missing_idempotency_key(self):
        """Test that requests without an Idempotency-Key are processed normally (or fail if your design strictly requires it)."""
        payload = {
            "customer_name": "Another User",
            "items": [{"name": "Burger", "quantity": 2}]
        }
        headers = {
            "Content-Type": "application/json"
        }

        # Send request without the key
        response_1 = self.client.post('/orders', data=json.dumps(payload), headers=headers)
        self.assertEqual(response_1.status_code, 201)
        data_1 = json.loads(response_1.data)

        # Send again without the key
        response_2 = self.client.post('/orders', data=json.dumps(payload), headers=headers)
        self.assertEqual(response_2.status_code, 201)
        data_2 = json.loads(response_2.data)

        # Because there is no idempotency key, the server processes it twice, 
        # meaning they should get different unique Order IDs (assuming your store assigns unique IDs).
        # We assert they are NOT the same order.
        if "id" in data_1 and "id" in data_2:
            self.assertNotEqual(data_1["id"], data_2["id"])

if __name__ == '__main__':
    unittest.main()
