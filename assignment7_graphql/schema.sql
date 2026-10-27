-- CampusEats - Assignment 7 (GraphQL)
-- Run:  mysql -u root -p < schema.sql

CREATE DATABASE IF NOT EXISTS campuseats_graphql;
USE campuseats_graphql;

DROP TABLE IF EXISTS dishes;

CREATE TABLE dishes (
  id          INT AUTO_INCREMENT PRIMARY KEY,
  name        VARCHAR(100)  NOT NULL,
  description VARCHAR(255)  NULL,
  price       DECIMAL(8,2)  NOT NULL,
  available   BOOLEAN       NOT NULL DEFAULT TRUE
);

INSERT INTO dishes (name, description, price, available) VALUES
  ('Veg Burger',    'Aloo tikki burger with cheese', 60.00, TRUE),
  ('Masala Dosa',   'Crispy dosa with potato masala', 80.00, TRUE),
  ('Cold Coffee',   NULL,                             50.00, TRUE),
  ('Chole Bhature', 'Sold out for today',            100.00, FALSE);
