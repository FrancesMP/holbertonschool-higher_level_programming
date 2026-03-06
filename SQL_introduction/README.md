<div align="center">

# 🗄️ SQL Introduction

![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Holberton](https://img.shields.io/badge/Holberton-School-FF0000?style=for-the-badge)

*A complete introduction to SQL and relational databases*

</div>

---

## 📖 What is this project about?

This project is a hands-on introduction to **SQL** and **MySQL**. The goal is to understand how to interact with a relational database from scratch — creating databases and tables, inserting data, reading it, filtering it, modifying it, deleting it, and running calculations on it.

Everything revolves around two tables: `first_table` and `second_table`, inside the database `hbtn_0c_0`.

---

## 🚀 How to Run a Script

```bash
cat script.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

> ⚠️ The database name is **always passed as an argument** to the command — never hardcoded inside the SQL file. This way the same script works on any database.

---

## 📂 Concepts Covered

### 🏗️ 1. Managing Databases & Tables

Before touching any data, you need to set up the structure first.

| Action | SQL Statement |
|--------|--------------|
| List all databases | `SHOW DATABASES;` |
| Create a database (safe) | `CREATE DATABASE IF NOT EXISTS hbtn_0c_0;` |
| Delete a database | `DROP DATABASE hbtn_0c_0;` |
| List all tables | `SHOW TABLES;` |
| See full table structure | `SHOW CREATE TABLE first_table;` |
| Create a table | `CREATE TABLE IF NOT EXISTS my_table (...);` |

> 💡 `IF NOT EXISTS` prevents errors when running a script multiple times — the operation is simply skipped if it already exists.

> 💡 `SHOW CREATE TABLE` is used instead of `DESCRIBE` or `EXPLAIN`, which are **forbidden** in this project.

---

### 🔍 2. Reading Data — SELECT

The most used command in SQL. Fetches data based on specific criteria.

```sql
-- Read everything
SELECT * FROM first_table;

-- Pick specific columns
SELECT score, name FROM second_table;

-- Filter with a condition
SELECT score, name FROM second_table WHERE score > 9;

-- Sort results — DESC = highest to lowest, ASC = lowest to highest
SELECT score, name FROM second_table ORDER BY score DESC;

-- Exclude NULL and empty values
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '';

-- Count matching records
SELECT COUNT(*) FROM first_table WHERE id = 89;
```

> 💡 **`NULL` vs `''`** — `NULL` means the field was never filled in. `''` means it was filled in with nothing (empty string). Both need to be excluded for clean data.

---

### ✏️ 3. Writing Data — INSERT / UPDATE / DELETE

```sql
-- Insert a single row
INSERT INTO first_table (id, name) VALUES (89, 'Best School');

-- Insert multiple rows at once
INSERT INTO second_table (id, name, score)
VALUES (1, 'John', 10),
       (2, 'Alex', 3),
       (3, 'Bob', 14),
       (4, 'George', 8);

-- Update a value (without hardcoding the id)
UPDATE second_table SET score = 10 WHERE name = 'Bob';

-- Delete rows matching a condition
DELETE FROM second_table WHERE score < 6;
```

> ⚠️ **Always use a `WHERE` clause with `DELETE`.** Without it, `DELETE FROM table` wipes the entire table instantly with no confirmation.

> 💡 Using `WHERE name = 'Bob'` instead of `WHERE id = 3` avoids hardcoding a value that could change — this is the concept behind the *no cheating* task.

---

### 📊 4. Aggregating Data — COUNT / AVG / GROUP BY

Used when you want statistics on the data rather than the raw rows.

```sql
-- Compute the average score
SELECT AVG(score) AS average FROM second_table;

-- Count records grouped by score, sorted by frequency
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
```

> 💡 `GROUP BY` groups rows that share the same value in a column.  
> 💡 `COUNT(*)` counts how many rows are in each group.  
> 💡 `AS` renames the output column — mandatory here because the checker verifies the **exact column name** (`average`, `number`).

---

## 📋 Project Rules

- ✅ All SQL keywords in **UPPERCASE** (`SELECT`, `WHERE`, `INSERT`...)
- ✅ Every file starts with a `--` comment describing what the script does
- ✅ No use of `DESCRIBE` or `EXPLAIN`
- ✅ Database name never hardcoded inside the scripts
- ✅ All files end with a new line

---

## 👤 Author

**BigSi** — Holberton School France