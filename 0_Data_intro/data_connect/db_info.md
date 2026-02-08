# PostgreSQL Database Guide

## What is PostgreSQL?

PostgreSQL is a powerful, open-source object-relational database management system (ORDBMS) that has been in active development for over 30 years. It's known for its reliability, feature robustness, and performance.

## Key Benefits of PostgreSQL

### 1. **ACID Compliance**
- Ensures data integrity through Atomicity, Consistency, Isolation, and Durability
- Reliable transactions even under system failures

### 2. **Advanced Features**
- Support for JSON/JSONB data types for NoSQL-like functionality
- Full-text search capabilities (vector stores)
- Window functions and common table expressions (CTEs)
- Custom data types and functions

### 3. **Scalability & Performance**
- Excellent performance for complex queries
- Support for parallel query execution
- Advanced indexing options (B-tree, Hash, GiST, GIN, BRIN)
- Table partitioning for large datasets

### 4. **Standards Compliance**
- Strong adherence to SQL standards
- ANSI SQL compliance with many extensions

### 5. **Cost-Effective**
- Completely free and open-source
- No licensing fees, even for commercial use
- Large community support

## PostgreSQL vs Other Database Systems

| Feature | PostgreSQL | MySQL | SQLite | Oracle |
|---------|------------|-------|---------|---------|
| **Cost** | Free | Free/Paid | Free | Expensive |
| **ACID Compliance** | Full | Partial | Full | Full |
| **JSON Support** | Native | Basic | Limited | Good |
| **Complex Queries** | Excellent | Good | Limited | Excellent |
| **Scalability** | High | High | Low | Very High |
| **Learning Curve** | Moderate | Easy | Easy | Steep |

## Connecting to PostgreSQL in Python

### Method 1: Using psycopg2 (Most Popular)

#### Installation
```bash
pip install psycopg2-binary
```

#### Basic Connection
```python
import psycopg2
from psycopg2 import sql

# Connection parameters
conn_params = {
    'host': 'localhost',
    'database': 'your_database',
    'user': 'your_username',
    'password': 'your_password',
    'port': '5432'
}

try:
    # Establish connection
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()
    
    # Execute a query
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print(f"PostgreSQL version: {version[0]}")
    
    # Close connections
    cursor.close()
    conn.close()
    
except psycopg2.Error as e:
    print(f"Error connecting to PostgreSQL: {e}")
```

### Method 2: Using SQLAlchemy (ORM Approach)

#### Installation
```bash
pip install sqlalchemy psycopg2-binary
```

#### Basic Usage
```python
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Create engine
engine = create_engine('postgresql://username:password@localhost:5432/database_name')

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Execute raw SQL
result = session.execute(text("SELECT * FROM your_table"))
for row in result:
    print(row)

session.close()
```

#### Using SQLAlchemy with Models
```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100))

# Create engine and session
engine = create_engine('postgresql://username:password@localhost:5432/database_name')
Session = sessionmaker(bind=engine)
session = Session()

# Query using ORM
users = session.query(User).filter(User.name.like('%john%')).all()
for user in users:
    print(f"Name: {user.name}, Email: {user.email}")

session.close()
```

### Method 3: Using asyncpg (Async Support)

#### Installation
```bash
pip install asyncpg
```

#### Basic Async Connection
```python
import asyncio
import asyncpg

async def main():
    # Connect to database
    conn = await asyncpg.connect(
        host='localhost',
        port=5432,
        user='your_username',
        password='your_password',
        database='your_database'
    )
    
    # Execute query
    rows = await conn.fetch('SELECT * FROM your_table')
    for row in rows:
        print(row)
    
    # Close connection
    await conn.close()

# Run the async function
asyncio.run(main())
```

## Best Practices for Python-PostgreSQL Connection

### 1. **Use Connection Pooling**
```python
from psycopg2 import pool

# Create connection pool
connection_pool = psycopg2.pool.SimpleConnectionPool(
    1, 20,  # min and max connections
    host='localhost',
    database='your_database',
    user='your_username',
    password='your_password'
)
```

### 2. **Handle Exceptions Properly**
```python
import psycopg2

try:
    conn = psycopg2.connect(...)
    cursor = conn.cursor()
    # Your database operations
    conn.commit()
except psycopg2.DatabaseError as e:
    conn.rollback()
    print(f"Database error: {e}")
except Exception as e:
    print(f"General error: {e}")
finally:
    if conn:
        cursor.close()
        conn.close()
```

### 3. **Use Environment Variables for Credentials**
```python
import os
import psycopg2

conn = psycopg2.connect(
    host=os.getenv('DB_HOST', 'localhost'),
    database=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    port=os.getenv('DB_PORT', '5432')
)
```

### 4. **Parameterized Queries (Prevent SQL Injection)**
```python
# Safe way to pass parameters
cursor.execute(
    "SELECT * FROM users WHERE name = %s AND age > %s",
    (username, min_age)
)

# Using named parameters
cursor.execute(
    "SELECT * FROM users WHERE name = %(name)s AND age > %(age)s",
    {'name': username, 'age': min_age}
)
```

## Common PostgreSQL Python Operations

### Insert Data
```python
cursor.execute(
    "INSERT INTO users (name, email) VALUES (%s, %s)",
    ("John Doe", "john@example.com")
)
conn.commit()
```

### Bulk Insert
```python
data = [
    ("Alice", "alice@example.com"),
    ("Bob", "bob@example.com"),
    ("Charlie", "charlie@example.com")
]

cursor.executemany(
    "INSERT INTO users (name, email) VALUES (%s, %s)",
    data
)
conn.commit()
```

### Update Data
```python
cursor.execute(
    "UPDATE users SET email = %s WHERE name = %s",
    ("newemail@example.com", "John Doe")
)
conn.commit()
```

### Delete Data
```python
cursor.execute(
    "DELETE FROM users WHERE name = %s",
    ("John Doe",)
)
conn.commit()
```

This guide provides a comprehensive overview of PostgreSQL and its Python integration. Choose the connection method that best fits your project's requirements!
