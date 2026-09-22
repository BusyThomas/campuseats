# HTTP Headers Table

This document describes the important HTTP headers used by the API, their purpose, and example values.

| Header | Direction | Purpose | Example |
|---|---|---|---|
| `Content-Type` | Request / Response | Specifies the format of the request or response body. | `application/json` |
| `Accept` | Request | Tells the server which response format the client accepts. | `application/json` |
| `Authorization` | Request | Sends authentication credentials/token to the server. | `Bearer <JWT_TOKEN>` |
| `Cache-Control` | Response | Controls caching behavior of the response. | `no-cache` |
| `ETag` | Response | Identifies a specific version of a resource for cache validation. | `"abc123"` |
| `If-None-Match` | Request | Allows the client to ask whether a cached resource is still valid. | `"abc123"` |
| `If-Match` | Request | Used to perform conditional updates and prevent lost updates. | `"abc123"` |
| `Idempotency-Key` | Request | Prevents duplicate processing of the same operation during retries. | `order-123-abc` |
| `Retry-After` | Response | Tells the client how long to wait before retrying. | `30` |
| `X-RateLimit-Limit` | Response | Shows the maximum number of requests allowed in the rate-limit window. | `100` |
| `X-RateLimit-Remaining` | Response | Shows how many requests remain in the current rate-limit window. | `95` |
| `X-RateLimit-Reset` | Response | Indicates when the rate-limit window resets. | `1727000000` |
| `Access-Control-Allow-Origin` | Response | Controls which origins are allowed to access the API from a browser. | `https://example.com` |
| `Access-Control-Allow-Methods` | Response | Specifies HTTP methods allowed for CORS requests. | `GET, POST, PUT, DELETE` |
| `Access-Control-Allow-Headers` | Response | Specifies request headers allowed in CORS requests. | `Content-Type, Authorization` |
| `X-Content-Type-Options` | Response | Prevents browsers from MIME-type sniffing. | `nosniff` |
| `X-Frame-Options` | Response | Helps prevent clickjacking by controlling iframe embedding. | `DENY` |
| `Content-Security-Policy` | Response | Defines allowed sources for browser-executed content. | `default-src 'self'` |

## Header Categories

### 1. Content Negotiation

#### Content-Type

Indicates the media type of the request or response body.

Example:

```http
Content-Type: application/json
```

#### Accept

Indicates the response formats accepted by the client.

Example:

```http
Accept: application/json
```

### 2. Authentication

#### Authorization

Used to send the authentication token.

Example:

```http
Authorization: Bearer <JWT_TOKEN>
```

### 3. Caching

#### Cache-Control

Controls whether and how a response can be cached.

Example:

```http
Cache-Control: no-cache
```

#### ETag

Provides a unique identifier for a particular version of a resource.

Example:

```http
ETag: "abc123"
```

#### If-None-Match

Used with an ETag to check whether the client's cached copy is still valid.

Example:

```http
If-None-Match: "abc123"
```

#### If-Match

Used for conditional requests. The server performs the update only if the resource still has the expected ETag.

Example:

```http
If-Match: "abc123"
```

### 4. Retry and Idempotency

#### Idempotency-Key

Provides a unique key for an operation so that retrying the same request does not create duplicate operations.

Example:

```http
Idempotency-Key: order-123-abc
```

#### Retry-After

Specifies how long the client should wait before retrying a request.

Example:

```http
Retry-After: 30
```

### 5. Rate Limiting

#### X-RateLimit-Limit

Shows the maximum number of requests allowed during the rate-limit period.

Example:

```http
X-RateLimit-Limit: 100
```

#### X-RateLimit-Remaining

Shows the number of requests remaining.

Example:

```http
X-RateLimit-Remaining: 95
```

#### X-RateLimit-Reset

Shows when the rate-limit window resets.

Example:

```http
X-RateLimit-Reset: 1727000000
```

### 6. CORS

#### Access-Control-Allow-Origin

Specifies which origin is allowed to access the API.

Example:

```http
Access-Control-Allow-Origin: https://example.com
```

#### Access-Control-Allow-Methods

Specifies the HTTP methods allowed through CORS.

Example:

```http
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
```

#### Access-Control-Allow-Headers

Specifies which request headers are allowed.

Example:

```http
Access-Control-Allow-Headers: Content-Type, Authorization
```

### 7. Security Headers

#### X-Content-Type-Options

Prevents MIME-type sniffing.

Example:

```http
X-Content-Type-Options: nosniff
```

#### X-Frame-Options

Controls whether the API response can be displayed inside a frame.

Example:

```http
X-Frame-Options: DENY
```

#### Content-Security-Policy

Defines which sources the browser is allowed to load content from.

Example:

```http
Content-Security-Policy: default-src 'self'
```

## Example HTTP Exchange

### Request

```http
POST /orders HTTP/1.1
Host: localhost:8000
Content-Type: application/json
Accept: application/json
Authorization: Bearer <JWT_TOKEN>
Idempotency-Key: order-123-abc

{
  "item": "Laptop",
  "quantity": 1
}
```

### Response

```http
HTTP/1.1 201 Created
Content-Type: application/json
Cache-Control: no-cache
ETag: "abc123"
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 99
X-Content-Type-Options: nosniff

{
  "id": 1,
  "item": "Laptop",
  "quantity": 1
}
```

## Notes

- `Content-Type` describes the body format.
- `Authorization` is used for authenticated requests.
- `ETag`, `If-None-Match`, and `If-Match` support conditional requests and caching/concurrency control.
- `Idempotency-Key` is useful for safely retrying operations such as order creation.
- Rate-limit headers communicate API usage limits to clients.
- CORS headers control browser-based cross-origin requests.
- Security headers provide additional protection against common browser-based attacks.
