# CampusEats Secured REST API – CS543 Assignment 09

## Team Members
- Shirish Meshram – 20252651051
- Deepamoni Boro – 20252651018
- Aman Chouhan – 20252651006
- Sanu Sawarnakar – 20252651048

## Overview
This folder extends the CampusEats Menu Service from Assignment 8. It keeps the same menu service and routes, and adds password hashing, JWT login, authentication middleware, and role-based authorization.

## Demo accounts
| Username | Password | Role |
|---|---|---|
| customer | customer123 | customer |
| restaurant | restaurant123 | restaurant |

Passwords are hashed using bcryptjs before they are stored in the in-memory users list. These are demonstration credentials only.

## Setup
1. Open a terminal in the `assignment9` folder.
2. Install dependencies:
   `npm install`
3. Copy `.env.example` to `.env`.
4. Set a private value for `JWT_SECRET` in `.env` (do not commit `.env`).
5. Start the server:
   `npm start`

Server: `http://localhost:3000`

## Routes and access rules
| Method | Path | Access | Description |
|---|---|---|---|
| POST | `/login` | Public | Verify credentials and return a JWT |
| GET | `/items` | Any authenticated user | Get all menu items |
| GET | `/items/:id` | Any authenticated user | Get one menu item |
| POST | `/items` | `restaurant` or `admin` role | Add a menu item |

The read routes require authentication only. The write route requires authentication first and then the `restaurant` or `admin` role.

## Test with curl (PowerShell)
Run each command in a terminal after starting the server.

### 1. No token – expect 401
```powershell
curl.exe -i http://localhost:3000/items
```

### 2. Login as customer – copy the token from the response
```powershell
curl.exe -i -X POST http://localhost:3000/login -H "Content-Type: application/json" -d "{\"username\":\"customer\",\"password\":\"customer123\"}"
```

### 3. Authenticated read – expect 200
Replace `CUSTOMER_TOKEN` with the token returned above.
```powershell
curl.exe -i http://localhost:3000/items -H "Authorization: Bearer CUSTOMER_TOKEN"
```

### 4. Login as restaurant – expect token, then write – expect 201
```powershell
curl.exe -i -X POST http://localhost:3000/login -H "Content-Type: application/json" -d "{\"username\":\"restaurant\",\"password\":\"restaurant123\"}"
```
Replace `RESTAURANT_TOKEN` with the returned token.
```powershell
curl.exe -i -X POST http://localhost:3000/items -H "Authorization: Bearer RESTAURANT_TOKEN" -H "Content-Type: application/json" -d "{\"name\":\"Paneer Roll\",\"price\":120,\"available\":true}"
```

### 5. Customer attempts write – expect 403
Replace `CUSTOMER_TOKEN` with the customer token.
```powershell
curl.exe -i -X POST http://localhost:3000/items -H "Authorization: Bearer CUSTOMER_TOKEN" -H "Content-Type: application/json" -d "{\"name\":\"Masala Dosa\",\"price\":90,\"available\":true}"
```

## Answers to assignment questions

### 1. Which routes require only authentication, and which also require a role?
- `GET /items` – authentication required; any valid logged-in user.
- `GET /items/:id` – authentication required; any valid logged-in user.
- `POST /items` – authentication and `restaurant` or `admin` role required.
- `POST /login` – public route; credentials are checked to issue a token.

### 2. Show one 401 and one 403 from your demo. Why did the server return that code?
- **401 Unauthorized:** `GET /items` without a Bearer token returns 401 because the request has not provided valid authentication.
- **403 Forbidden:** `POST /items` with a valid customer token returns 403 because the user is authenticated but does not have the required restaurant/admin role.

### 3. What is inside your JWT payload? Why is it safe to trust the role claim on the server, and why must the secret stay out of your code?
The JWT payload contains the user's `id` and `role`. The server trusts the role only after verifying the token signature using `jwt.verify` and the private secret. The secret must stay outside the source code so that someone who gets access to the repository cannot use it to create forged tokens. The `.env` file is ignored by Git, while `.env.example` contains only a blank placeholder.

## Demo evidence still to add
Capture screenshots for all five cases: (1) request without token → 401, (2) successful login → token, (3) request with token → 200, (4) restaurant role write → 201, and (5) customer role write → 403. Add the short demo video link and screenshots before final submission.
