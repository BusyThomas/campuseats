# CURL Test Transcript

This document records the CURL requests used for testing the API and the corresponding responses.

> Replace each `PASTE ACTUAL TERMINAL OUTPUT HERE` section with the real output from your terminal after running the command.

## 1. Health Check

### Request

```bash
curl -i http://localhost:8000/
```

### Response

```text
PASTE ACTUAL TERMINAL OUTPUT HERE
```

---

## 2. Create Order

### Request

```bash
curl -i -X POST http://localhost:8000/orders \
-H "Content-Type: application/json" \
-d '{
  "item": "Laptop",
  "quantity": 1
}'
```

### Response

```text
PASTE ACTUAL TERMINAL OUTPUT HERE
```

---

## 3. Get All Orders

### Request

```bash
curl -i http://localhost:8000/orders
```

### Response

```text
PASTE ACTUAL TERMINAL OUTPUT HERE
```

---

## 4. Get Order by ID

### Request

```bash
curl -i http://localhost:8000/orders/1
```

### Response

```text
PASTE ACTUAL TERMINAL OUTPUT HERE
```

---

## 5. Update Order

### Request

```bash
curl -i -X PUT http://localhost:8000/orders/1 \
-H "Content-Type: application/json" \
-d '{
  "item": "Laptop",
  "quantity": 2
}'
```

### Response

```text
PASTE ACTUAL TERMINAL OUTPUT HERE
```

---

## 6. Delete Order

### Request

```bash
curl -i -X DELETE http://localhost:8000/orders/1
```

### Response

```text
PASTE ACTUAL TERMINAL OUTPUT HERE
```

---

## 7. Invalid Request

### Request

```bash
curl -i -X POST http://localhost:8000/orders \
-H "Content-Type: application/json" \
-d '{}'
```

### Response

```text
PASTE ACTUAL TERMINAL OUTPUT HERE
```

---

## Test Summary

| Test | Method | Endpoint | Expected Status | Actual Status |
|---|---|---|---:|---:|
| Health Check | GET | `/` | 200 | |
| Create Order | POST | `/orders` | 201 | |
| Get Orders | GET | `/orders` | 200 | |
| Get Order | GET | `/orders/{id}` | 200 | |
| Update Order | PUT | `/orders/{id}` | 200 | |
| Delete Order | DELETE | `/orders/{id}` | 204 | |
| Invalid Request | POST | `/orders` | 400 | |
