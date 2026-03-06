# Python - Object-Relational Mapping

This project covers the fundamentals of connecting Python applications to MySQL databases using both raw SQL queries (MySQLdb) and Object-Relational Mapping (SQLAlchemy).

## Learning Objectives
- Connect to MySQL database from Python scripts
- Execute SQL queries (SELECT, INSERT) using MySQLdb
- Use SQLAlchemy ORM to map Python classes to database tables
- Prevent SQL injection attacks
- Perform CRUD operations using both methods

## Requirements
- Python 3.8.5
- MySQLdb 2.0.x
- SQLAlchemy 1.4.x
- MySQL Server 8.0
- Ubuntu 20.04 LTS

## Project Structure
- `0-select_states.py` - List all states using MySQLdb
- `1-filter_states.py` - Filter states starting with 'N'
- `2-my_filter_states.py` - Filter states by name (vulnerable to SQL injection)
- `3-my_safe_filter_states.py` - Safe version using parameterized queries
- `4-cities_by_state.py` - List all cities with state names
- `5-filter_cities.py` - List cities of a specific state
- `model_state.py` - State class definition for SQLAlchemy
- `7-model_state_fetch_all.py` - List all states using SQLAlchemy
- `8-model_state_fetch_first.py` - Print first state

## Usage
```bash
# Example for task 0
./0-select_states.py root root hbtn_0e_0_usa

# Example for task 7 (SQLAlchemy)
./7-model_state_fetch_all.py root root hbtn_0e_6_usa