
# Request 1

## Command

```bash
curl -i https://jsonplaceholder.typicode.com/users/1
```

## Full Response

```text
HTTP/2 200 
date: Sun, 16 Aug 2026 09:49:39 GMT
content-type: application/json; charset=utf-8
content-length: 509
access-control-allow-credentials: true
cache-control: max-age=43200
etag: W/"1fd-+2Y3G3w049iSZtw5t1mzSnunngE"
expires: -1
nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}
pragma: no-cache
report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=2zdKTr9VSfmctvojKLSbD4JyFeW06hb2VUxynVKj1R4%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1786754565"}],"max_age":3600}
reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=2zdKTr9VSfmctvojKLSbD4JyFeW06hb2VUxynVKj1R4%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1786754565"
server: cloudflare
vary: Origin, Accept-Encoding
via: 2.0 heroku-router
x-content-type-options: nosniff
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 999
x-ratelimit-reset: 1786754590
age: 3817
accept-ranges: bytes
cf-cache-status: HIT
cf-ray: a2bf87c3b88937a5-BOM
alt-svc: h3=":443"; ma=86400

{
  "id": 1,
  "name": "Leanne Graham",
  "username": "Bret",
  "email": "Sincere@april.biz",
  "address": {
    "street": "Kulas Light",
    "suite": "Apt. 556",
    "city": "Gwenborough",
    "zipcode": "92998-3874",
    "geo": {
      "lat": "-37.3159",
      "lng": "81.1496"
    }
  },
  "phone": "1-770-736-8031 x56442",
  "website": "hildegard.org",
  "company": {
    "name": "Romaguera-Crona",
    "catchPhrase": "Multi-layered client-server neural-net",
    "bs": "harness real-time e-markets"
  }
}
```

Status: 200 OK

# Request 2

## Command

```bash
curl -i https://jsonplaceholder.typicode.com/users/2
```

## Full Response

```text
HTTP/2 200 
date: Sun, 16 Aug 2026 09:50:40 GMT
content-type: application/json; charset=utf-8
content-length: 509
access-control-allow-credentials: true
cache-control: max-age=43200
etag: W/"1fd-XTG63SYhaP/Uo6/vgmARnL3rpBk"
expires: -1
nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}
pragma: no-cache
report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=Na8sQ0dGJO16UrwjH3bPMevqhFZ7w%2FCtVnj8yFsR%2Fmw%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1786773780"}],"max_age":3600}
reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=Na8sQ0dGJO16UrwjH3bPMevqhFZ7w%2FCtVnj8yFsR%2Fmw%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1786773780"
server: cloudflare
vary: Origin, Accept-Encoding
via: 2.0 heroku-router
x-content-type-options: nosniff
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 997
x-ratelimit-reset: 1786773823
age: 13544
accept-ranges: bytes
cf-cache-status: HIT
cf-ray: a2bf893faf2a35d2-BOM
alt-svc: h3=":443"; ma=86400

{
  "id": 2,
  "name": "Ervin Howell",
  "username": "Antonette",
  "email": "Shanna@melissa.tv",
  "address": {
    "street": "Victor Plains",
    "suite": "Suite 879",
    "city": "Wisokyburgh",
    "zipcode": "90566-7771",
    "geo": {
      "lat": "-43.9509",
      "lng": "-34.4618"
    }
  },
  "phone": "010-692-6593 x09125",
  "website": "anastasia.net",
  "company": {
    "name": "Deckow-Crist",
    "catchPhrase": "Proactive didactic contingency",
    "bs": "synergize scalable supply-chains"
  }
}
```

Status: 200 OK

# Request 3

## Command

```bash
curl -i https://jsonplaceholder.typicode.com/posts/1
```

## Full Response

```text
HTTP/2 200 
date: Sun, 16 Aug 2026 10:05:24 GMT
content-type: application/json; charset=utf-8
content-length: 292
access-control-allow-credentials: true
cache-control: max-age=43200
etag: W/"124-yiKdLzqO5gfBrJFrcdJ8Yq0LGnU"
expires: -1
nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}
pragma: no-cache
report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=vm67FVLNHsCgrFgubRa04ooDeMKdgwXS9H3i2IbjuoY%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1785194657"}],"max_age":3600}
reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=vm67FVLNHsCgrFgubRa04ooDeMKdgwXS9H3i2IbjuoY%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1785194657"
server: cloudflare
vary: Origin, Accept-Encoding
via: 2.0 heroku-router
x-content-type-options: nosniff
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 999
x-ratelimit-reset: 1785194663
age: 10013
accept-ranges: bytes
cf-cache-status: HIT
cf-ray: a2bf9ed10be9d263-BOM
alt-svc: h3=":443"; ma=86400

{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}
```

Status: 200 OK

# Request 4

## Command

```bash
curl -i https://jsonplaceholder.typicode.com/comments/1
```

## Full Response

```text
HTTP/2 200 
date: Sun, 16 Aug 2026 10:05:52 GMT
content-type: application/json; charset=utf-8
content-length: 268
access-control-allow-credentials: true
cache-control: max-age=43200
etag: W/"10c-KJ4I9RM/+33TKdV8CFsIvqsDSP0"
expires: -1
nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}
pragma: no-cache
report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=fme9KWPtRae%2BTDbkMNDQyAZ9LCFiWVshhPWbhNDRo3A%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1786874572"}],"max_age":3600}
reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=fme9KWPtRae%2BTDbkMNDQyAZ9LCFiWVshhPWbhNDRo3A%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1786874572"
server: cloudflare
vary: Origin, Accept-Encoding
via: 2.0 heroku-router
x-content-type-options: nosniff
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 999
x-ratelimit-reset: 1786874624
age: 179
accept-ranges: bytes
cf-cache-status: HIT
cf-ray: a2bf9f861bcde5cc-BOM
alt-svc: h3=":443"; ma=86400

{
  "postId": 1,
  "id": 1,
  "name": "id labore ex et quam laborum",
  "email": "Eliseo@gardner.biz",
  "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
}
```

Status: 200 OK

# Request 5 — Deliberate Failure

## Command

```bash
curl -i https://jsonplaceholder.typicode.com/users/99999
```

## Full Response

```text
HTTP/2 404 
date: Sun, 16 Aug 2026 10:06:33 GMT
content-type: application/json; charset=utf-8
content-length: 2
access-control-allow-credentials: true
cache-control: max-age=43200
etag: W/"2-vyGp6PvFo4RvsFtPoIWeCReyIC8"
expires: -1
nel: {"report_to":"heroku-nel","response_headers":["Via"],"max_age":3600,"success_fraction":0.01,"failure_fraction":0.1}
pragma: no-cache
report-to: {"group":"heroku-nel","endpoints":[{"url":"https://nel.heroku.com/reports?s=3INSzsH%2BnnpNolfKQW6IczFsKKu7bQlhznFc8AK0z7U%3D\u0026sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d\u0026ts=1786863559"}],"max_age":3600}
reporting-endpoints: heroku-nel="https://nel.heroku.com/reports?s=3INSzsH%2BnnpNolfKQW6IczFsKKu7bQlhznFc8AK0z7U%3D&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&ts=1786863559"
server: cloudflare
vary: Origin, Accept-Encoding
via: 2.0 heroku-router
x-content-type-options: nosniff
x-powered-by: Express
x-ratelimit-limit: 1000
x-ratelimit-remaining: 999
x-ratelimit-reset: 1786863582
age: 11233
cf-cache-status: HIT
cf-ray: a2bfa0811ff9d263-BOM
alt-svc: h3=":443"; ma=86400

{}
```

Status: 404 Not Found

This request was deliberately made for a non-existent user to demonstrate an HTTP 404 response.
