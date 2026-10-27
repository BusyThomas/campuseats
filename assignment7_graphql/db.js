import mysql from "mysql2/promise";

// Connection settings can be overridden with environment variables.
export const pool = mysql.createPool({
  host: process.env.DB_HOST || "localhost",
  port: Number(process.env.DB_PORT || 3306),
  user: process.env.DB_USER || "root",
  password: process.env.DB_PASSWORD || "admin123",
  database: process.env.DB_NAME || "campuseats_graphql",
  waitForConnections: true,
  connectionLimit: 5,
});
