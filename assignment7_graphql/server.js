import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import express from "express";
import cors from "cors";
import { ApolloServer } from "@apollo/server";
import { expressMiddleware } from "@apollo/server/express4";
import { pool } from "./db.js";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const typeDefs = fs.readFileSync(path.join(__dirname, "schema.graphql"), "utf8");

const COLUMNS = "id, name, description, price, available";

const resolvers = {
  // MySQL returns DECIMAL as string and BOOLEAN as 0/1, so convert for GraphQL types
  Dish: {
    price: (d) => Number(d.price),
    available: (d) => Boolean(d.available),
  },

  Query: {
    // SELECT all rows
    dishes: async () => {
      const [rows] = await pool.query(`SELECT ${COLUMNS} FROM dishes ORDER BY id`);
      return rows;
    },
    // SELECT ... WHERE id = ?
    dish: async (_, { id }) => {
      const [rows] = await pool.query(`SELECT ${COLUMNS} FROM dishes WHERE id = ?`, [id]);
      return rows[0] || null;
    },
  },

  Mutation: {
    // INSERT a row, then read it back
    addDish: async (_, { input }) => {
      const { name, price, description = null, available = true } = input;
      const [result] = await pool.query(
        "INSERT INTO dishes (name, description, price, available) VALUES (?, ?, ?, ?)",
        [name, description, price, available]
      );
      const [rows] = await pool.query(`SELECT ${COLUMNS} FROM dishes WHERE id = ?`, [result.insertId]);
      return rows[0];
    },
  },
};

const app = express();
const server = new ApolloServer({ typeDefs, resolvers });
await server.start();

app.use("/graphql", cors(), express.json(), expressMiddleware(server));
app.use(express.static(path.join(__dirname, "public")));

const PORT = process.env.PORT || 4000;
app.listen(PORT, () => {
  console.log(`CampusEats GraphQL ready -> http://localhost:${PORT}  (API: /graphql)`);
});
