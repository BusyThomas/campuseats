# Assignment 5 --- Member 4

## Curl API Tests

This file contains the `curl` commands used to test the REST API.

> Replace `<BASE_URL>` with the actual URL/port of the running backend
> before executing the commands.

------------------------------------------------------------------------

## 1. Check Server

``` bash
curl -i <BASE_URL>/
```

**Purpose:** Verify that the server is running and responding.

------------------------------------------------------------------------

## 2. GET Request

``` bash
curl -i -X GET "<BASE_URL>/orders"
```

**Purpose:** Fetch the list of orders.

------------------------------------------------------------------------

## 3. GET a Single Resource

``` bash
curl -i -X GET "<BASE_URL>/orders/<ORDER_ID>"
```

**Purpose:** Fetch one order using its ID.

------------------------------------------------------------------------

## 4. POST Request

``` bash
curl -i -X POST "<BASE_URL>/orders"   -H "Content-Type: application/json"   -d '{
    "product": "Test Product",
    "quantity": 2
  }'
```

**Purpose:** Create a new order.

------------------------------------------------------------------------

## 5. PUT Request

``` bash
curl -i -X PUT "<BASE_URL>/orders/<ORDER_ID>"   -H "Content-Type: application/json"   -d '{
    "product": "Updated Product",
    "quantity": 3
  }'
```

**Purpose:** Update an existing order.

------------------------------------------------------------------------

## 6. DELETE Request

``` bash
curl -i -X DELETE "<BASE_URL>/orders/<ORDER_ID>"
```

**Purpose:** Delete an existing order.

------------------------------------------------------------------------

## 7. OPTIONS Request

``` bash
curl -i -X OPTIONS "<BASE_URL>/orders"
```

**Purpose:** Check the HTTP methods supported by the endpoint.

------------------------------------------------------------------------

## 8. Request with Query Parameters

``` bash
curl -i -G "<BASE_URL>/orders"   --data-urlencode "page=1"   --data-urlencode "limit=10"
```

**Purpose:** Test query parameters for pagination/filtering.

------------------------------------------------------------------------

## 9. Request with Authorization Header

``` bash
curl -i -X GET "<BASE_URL>/orders"   -H "Authorization: Bearer <TOKEN>"
```

**Purpose:** Test an authenticated API request.

------------------------------------------------------------------------

## 10. Invalid Request

``` bash
curl -i -X POST "<BASE_URL>/orders"   -H "Content-Type: application/json"   -d '{}'
```

**Purpose:** Verify that invalid/missing data is rejected correctly.

------------------------------------------------------------------------

## 11. Save Response Headers and Body

``` bash
curl -i "<BASE_URL>/orders"
```

The `-i` option displays both:

-   HTTP response status
-   Response headers
-   Response body

------------------------------------------------------------------------

## Test Result Table

  ----------------------------------------------------------------------------------------
  Test            Method         Endpoint                    Expected       Actual Result
                                                             Result         
  --------------- -------------- --------------------------- -------------- --------------
  Server check    GET            `/`                         200 OK         Pending

  List orders     GET            `/orders`                   200 OK         Pending

  Get order       GET            `/orders/<ORDER_ID>`        200 OK         Pending

  Create order    POST           `/orders`                   201 Created    Pending

  Update order    PUT            `/orders/<ORDER_ID>`        200 OK         Pending

  Delete order    DELETE         `/orders/<ORDER_ID>`        200/204        Pending

  OPTIONS         OPTIONS        `/orders`                   200 OK         Pending

  Query           GET            `/orders?page=1&limit=10`   200 OK         Pending
  parameters                                                                

  Authorization   GET            `/orders`                   200 OK/401     Pending

  Invalid request POST           `/orders`                   400/422        Pending
  ----------------------------------------------------------------------------------------

------------------------------------------------------------------------

## Notes

1.  Start the backend server before running the commands.
2.  Replace `<BASE_URL>` with the actual API URL.
3.  Replace `<ORDER_ID>` with an actual order ID.
4.  Replace `<TOKEN>` with a valid authentication token if
    authentication is enabled.
5.  After executing each command, record the actual status code and
    response in the transcript document.
