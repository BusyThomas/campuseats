# CampusEats - Assignment 7: GraphQL (Dish service)

**How to run:** `mysql -u root -p < schema.sql && npm install && npm start` -> open http://localhost:4000
(DB settings via env vars if needed: `DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`)

## Team (TEAM-07)

| Roll No | Name |
|---|---|
| 20252651056 | Shirish |
| 20252651016 | Deepamoni |
| 20252651006 | Aman Chouhan |
| 20252651048 | Sanu Swarnakar |

## Files in this folder

- `schema.graphql` - `Dish` type, `Query` (list / by-id) and `Mutation` (`addDish`)
- `server.js` + `db.js` - Apollo Server with resolvers over MySQL (`mysql2`)
- `schema.sql` - `dishes` table + 4 seed rows
- `public/index.html` - plain HTML/CSS page: lists dishes, one button fires the mutation
- `screenshots/` - before / after screenshots of the mutation

## Example operations

```graphql
query { dishes { id name price available } }

mutation {
  addDish(input: { name: "Paneer Roll", price: 90 }) { id name price }
}
```

## Answers

**1. Which CampusEats service did you pick?**
The Menu / food service. We modelled a `Dish` (the `FOOD_ITEM` entity from our ER diagram) with fields `id, name, description, price, available`, stored in a MySQL table `dishes`.

**2. Name one field a client can skip and one it cannot.**
- Can skip: `description` - it is declared `String` (nullable), so a dish can be added without it (e.g. "Cold Coffee" has `NULL`).
- Cannot skip: `name` (`String!`) - `!` means non-null, so the server rejects `addDish` without it. Same for `price: Float!`. The `!` gives clients a guarantee about what they will always receive and forces the server to validate required input before it touches the database.

**3. Map it to SQL.**
- `dish(id: ID!)` query -> the `id` argument becomes the **WHERE** clause: `SELECT ... FROM dishes WHERE id = ?`. (The `dishes` list query has no WHERE - it is a plain `SELECT ... ORDER BY id`.)
- The **INSERT** is run by the `Mutation.addDish` resolver in `server.js`: `INSERT INTO dishes (name, description, price, available) VALUES (?, ?, ?, ?)`, followed by a `SELECT ... WHERE id = insertId` to return the new row.
