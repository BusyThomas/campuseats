# CampusEats REST API – Assignment 8

## Team Members

* Shirish Meshram – 20252651051
* Deepamoni Boro – 20252651018
* Aman Chouhan – 20252651006
* Sanu Sawarnakar – 20252651048

## Project Overview

This project implements the CampusEats Menu Service as a REST API using Node.js and Express.js.

The application allows users to:

* View all available food items.
* Retrieve a specific food item using its ID.
* Add new food items through a form.

The application uses an in-memory array to store menu items.

## Technologies Used

* Node.js
* Express.js
* HTML
* CSS
* JavaScript Fetch API

## How to Run

1. Open the terminal inside the `assignment8` folder.

2. Install dependencies:

   `npm install`

3. Start the server:

   `node server.js`

4. Open the application in your browser:

   `http://localhost:3000`

## API Routes

| HTTP Method | Endpoint     | Description                           |
| ----------- | ------------ | ------------------------------------- |
| GET         | `/items`     | Retrieves all menu items.             |
| GET         | `/items/:id` | Retrieves a specific menu item by ID. |
| POST        | `/items`     | Adds a new menu item.                 |

## Answers to Assignment Questions

### 1. Which CampusEats service did you pick, and what are its routes (method + path)?

We selected the **Menu Service**.

The implemented routes are:

* `GET /items` – Retrieves all menu items.
* `GET /items/:id` – Retrieves a particular menu item using its ID.
* `POST /items` – Creates and adds a new menu item.

### 2. Which status codes did you return, and for which outcomes (200 / 201 / 404 / 422)?

The following HTTP status codes are used:

* **200 OK:** Returned when menu items are successfully retrieved.
* **201 Created:** Returned when a new menu item is successfully added.
* **404 Not Found:** Returned when the requested item ID does not exist.
* **422 Unprocessable Entity:** Returned when required fields are missing or the submitted data is invalid.

### 3. Where did you use req.params and where req.body? Why does POST need express.json()?

* **req.params:** Used in the `GET /items/:id` route to retrieve the item ID from the URL.
* **req.body:** Used in the `POST /items` route to access the data submitted by the user, such as name, price and availability.
* **express.json():** It is middleware that parses incoming JSON request bodies and makes the parsed data available through `req.body`. It is required to process JSON data sent by the frontend using the POST request.

## Screenshots

The before-and-after screenshots are available in the `screenshots` folder.

* `before.png` – Displays the initial menu with the default food items.
* `after.png` – Displays the menu after successfully adding a new food item.

## Demonstration Video

Google Drive Demo Video:

https://drive.google.com/file/d/18544Pijf2GNaV-19FDboZIhGDk27KW8_/view

## Conclusion

The CampusEats Menu Service successfully demonstrates REST API implementation using Express.js, including GET and POST requests, input validation, appropriate HTTP status codes and frontend integration.
