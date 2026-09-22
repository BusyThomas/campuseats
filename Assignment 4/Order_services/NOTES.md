# CS543 Web Services — Assignment 5
# Final Team Notes

> This is the single final `NOTES.md` for the complete team submission.
> Do not create separate `NOTES.md` files for individual members.

---

## 1. Team Work Distribution

| Member | Work |
|---|---|
| Member 1 | Part A — HTTP method semantics, safe/idempotent methods, query parameters, OPTIONS/Allow, full HTTP exchange |
| Member 2 | Part B — HTTP headers, content negotiation, status codes, authorization, ETag, rate limiting, CORS, security headers |
| Member 3 | Part C — conditional GET, conditional writes, Idempotency-Key retry safety, retry plan |
| Member 4 | Part D/evidence — curl testing, HTTP transcript, header table, testing/documentation evidence |

The final document combines all members' work.

---

# Part A — HTTP Methods & Message Semantics

## A1 — HTTP Method Map

| Action | HTTP Method | URL |
|---|---|---|
| Create an order | POST | `/orders` |
| List/filter orders | GET | `/orders?status={status}` |
| Get one order | GET | `/orders/{orderId}` |
| Cancel an order | POST | `/orders/{orderId}/cancellation` |

The collection resource `/orders` uses GET for reading/listing and POST for creating.

The individual resource `/orders/{orderId}` uses GET for reading one order.

Cancellation is represented as a sub-resource because it is an action on an existing order.

## A2 — Non-CRUD Action

Cancellation is modeled as:

```http
POST /orders/{orderId}/cancellation
```

This keeps the action attached to the order resource instead of using an action-style URL such as:

```text
POST /cancelOrder
```

## A3 — Safe and Idempotent Methods

| Endpoint | Safe? | Idempotent? | Reason |
|---|---|---|---|
| `GET /orders` | Yes | Yes | Only reads/list orders. |
| `GET /orders/{orderId}` | Yes | Yes | Only reads one order. |
| `POST /orders` | No | No | Creates an order. Repeating it can create another order unless the same idempotency key is reused. |
| `POST /orders/{orderId}/cancellation` | No | No | Changes order state and a repeated cancellation can produce a conflict. |

The GET endpoints do not change stored order state.

Order creation uses `Idempotency-Key` so a retry with the same key returns the original order instead of creating a duplicate.

## A4 — Query Parameters

The order collection remains a pure GET/read operation.

Filtering is performed through query parameters:

```http
GET /orders?status=PLACED
```

The service supports:

- `PLACED`
- `CANCELLED`

as valid `status` values.

The REST design can use query parameters for pagination and sorting as well:

```http
GET /orders?status=PLACED&page=1&limit=10&sort=createdAt
```

Only `status` is currently implemented in the service.

## A5 — OPTIONS and Allow

The `/orders` resource supports OPTIONS.

Request:

```http
OPTIONS /orders HTTP/1.1
Host: localhost:5000
```

Response:

```http
HTTP/1.1 204 No Content
Allow: GET, POST, OPTIONS
```

The `Allow` header tells the client which methods are supported.

For constrained clients that cannot directly send certain HTTP methods, `X-HTTP-Method-Override` can be documented as a fallback mechanism. It is not required for the current `/orders` implementation.

## A6 — Complete HTTP Exchange

### Request

```http
POST /orders HTTP/1.1
Host: localhost:5000
Content-Type: application/json
Accept: application/json
Idempotency-Key: order-001

{
  "userId": "CE-STU-33217",
  "cartId": "CART-1001",
  "deliveryAddressId": "ADDR-204",
  "paymentMethod": "UPI",
  "couponCode": "SAVE10"
}
```

### Response

```http
HTTP/1.1 201 Created
Content-Type: application/json
Location: http://localhost:5000/orders/ORD-1001

{
  "orderId": "ORD-1001",
  "status": "PLACED",
  "totalAmount": 349.0,
  "estimatedDeliveryMinutes": 25
}
```

The `Location` header identifies the newly created order resource.

---

# Part B — HTTP Headers and Status Codes

## B1 — Content-Type and Accept

Requests carrying JSON should use:

```http
Content-Type: application/json
```

Clients can request JSON using:

```http
Accept: application/json
```

If a client requests an unsupported response representation, the API should return:

```http
406 Not Acceptable
```

## B2 — Status Codes

| Status | Meaning | Usage |
|---:|---|---|
| 200 | OK | Successful read/update |
| 201 | Created | Successful order creation |
| 204 | No Content | OPTIONS response |
| 400 | Bad Request | Malformed request |
| 401 | Unauthorized | Missing/invalid authentication |
| 404 | Not Found | Resource does not exist |
| 409 | Conflict | Current resource state prevents operation |
| 412 | Precondition Failed | `If-Match` condition failed |
| 422 | Unprocessable Entity | Valid request rejected by domain |
| 429 | Too Many Requests | Rate limit exceeded |

A successful create returns `201 Created` with a `Location` header.

## B3 — Authorization

Protected endpoints use:

```http
Authorization: Bearer <token>
```

A missing or invalid token should result in:

```http
401 Unauthorized
```

## B4 — ETag

`ETag` identifies a particular representation/version of a resource.

Example:

```http
ETag: "abc123"
```

When the resource changes, its ETag must change.

## B5 — Rate Limiting

Useful response headers include:

```http
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1727000000
```

When the limit is exceeded:

```http
HTTP/1.1 429 Too Many Requests
Retry-After: 30
```

`Retry-After` tells the client when it can retry.

## B6 — CORS and Security Headers

Typical CORS headers:

```http
Access-Control-Allow-Origin: https://example.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
```

Security headers include:

```http
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Content-Security-Policy: default-src 'self'
```

These should be listed as implemented only after verifying the actual application configuration.

---

# Part C — Conditional Requests and Retry Safety

## C1 — Conditional GET

A client can send:

```http
If-None-Match: "abc123"
```

If the resource has not changed, the server returns:

```http
HTTP/1.1 304 Not Modified
```

The `304` response has no response body.

## C2 — Conditional Write

A client can send:

```http
If-Match: "abc123"
```

The server performs the write only if the current resource ETag matches.

If it does not match:

```http
HTTP/1.1 412 Precondition Failed
```

This prevents a client from overwriting a newer version of the resource.

## C3 — Idempotency-Key

Order creation uses:

```http
Idempotency-Key: order-123-abc
```

The first request creates the order.

A repeated request using the same key returns the original order instead of creating a duplicate.

## C4 — Safe Retry Plan

| Operation | Retry rule |
|---|---|
| GET | Safe to retry |
| POST `/orders` | Retry only with the same `Idempotency-Key` |
| POST cancellation | Retry only when the application's cancellation semantics make the retry safe |
| Request returning 4xx | Do not automatically retry |
| Dependency timeout | Retry according to bounded exponential backoff |
| Rate-limit 429 | Wait for `Retry-After` before retrying |

The existing payment-service call uses a timeout and bounded retry with exponential backoff and jitter. A 4xx response from the dependency is not retried.

---

# Part D — Testing and Documentation Evidence

## D1 — Curl Testing

The API can be tested with:

```bash
curl -i <BASE_URL>/orders
```

For creating an order:

```bash
curl -i -X POST "<BASE_URL>/orders" -H "Content-Type: application/json" -H "Accept: application/json" -H "Idempotency-Key: order-001" -d '{
  "userId": "USER-1001",
  "cartId": "CART-1001",
  "deliveryAddressId": "ADDR-1001",
  "paymentMethod": "UPI"
}'
```

The `-i` option displays the HTTP status line and response headers.

## D2 — Required Evidence

The final curl transcript should show:

1. Successful create
2. `Location` header
3. Same request repeated with the same `Idempotency-Key`
4. Conditional GET returning `304`
5. Conditional update returning `412`
6. Malformed request
7. Missing resource
8. Missing/invalid authentication
9. Rate-limit response if implemented
10. OPTIONS response with `Allow`

## D3 — Header Table

| Header | Direction | Purpose | Example |
|---|---|---|---|
| `Content-Type` | Request/Response | Body format | `application/json` |
| `Accept` | Request | Accepted response format | `application/json` |
| `Authorization` | Request | Authentication | `Bearer <token>` |
| `Cache-Control` | Response | Cache behavior | `no-cache` |
| `ETag` | Response | Resource version identifier | `"abc123"` |
| `If-None-Match` | Request | Conditional GET | `"abc123"` |
| `If-Match` | Request | Conditional write | `"abc123"` |
| `Idempotency-Key` | Request | Prevent duplicate processing | `order-123-abc` |
| `Retry-After` | Response | Retry timing | `30` |
| `X-RateLimit-Limit` | Response | Request limit | `100` |
| `X-RateLimit-Remaining` | Response | Remaining requests | `95` |
| `X-RateLimit-Reset` | Response | Rate-limit reset time | `1727000000` |
| `Access-Control-Allow-Origin` | Response | CORS origin | `https://example.com` |
| `Access-Control-Allow-Methods` | Response | CORS methods | `GET, POST, PUT, DELETE` |
| `Access-Control-Allow-Headers` | Response | CORS request headers | `Content-Type, Authorization` |
| `X-Content-Type-Options` | Response | Prevent MIME sniffing | `nosniff` |
| `X-Frame-Options` | Response | Frame protection | `DENY` |
| `Content-Security-Policy` | Response | Browser content policy | `default-src 'self'` |

---

# Final Endpoint Method Map

| Endpoint | Method | Purpose |
|---|---|---|
| `/orders` | GET | List/filter orders |
| `/orders` | POST | Create order |
| `/orders` | OPTIONS | Discover supported methods |
| `/orders/{orderId}` | GET | Read one order |
| `/orders/{orderId}/cancellation` | POST | Cancel order |

---

# Final Team File Checklist

- `app.py`
- `openapi.yaml`
- `models.py`
- `store.py`
- `errors.py`
- `tests/test_orders.py`
- `NOTES.md`
- `curl-transcript.txt`
- `headers-table.md`

> Important: examples above that describe headers such as ETag, Authorization, rate-limit, CORS, and security headers must be matched against the actual implementation before submission. Documentation alone does not implement a feature.
