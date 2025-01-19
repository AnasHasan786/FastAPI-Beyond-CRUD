# FastAPI Beyond CRUD 🚀

FastAPI is a modern framework for building web APIs in Python. It is a tool to create these APIs easily and quickly. It's like a special kitchen where you can prepare the dishes (APIs) faster, with fewer mistakes, and serve them to customers (applications). It's named **FastAPI** because it's very fast at handling requests, thanks to a technology called **ASGI** (Asynchronous Server Gateway Interface).

<p align="center">
  <img src="https://datascientest.com/en/files/2023/10/fastAPI-1.webp" alt="FastAPI" width="800" height="200">
</p>

---

### Difference between WSGI and ASGI ⚡

| **Feature** | **WSGI** | **ASGI** |
|-------------|----------|----------|
| **Protocol** | Synchronous | Asynchronous |
| **Request Handling** | One at a time | Multiple simultaneously |
| **Performance** | Struggles with real-time updates | Optimized for real-time features |
| **Supports WebSockets** | No | Yes |

---

### How Does ASGI Work? 🛠️

Imagine a busy restaurant:

- **WSGI**: A waiter takes one order, delivers it to the kitchen, waits for it to finish, and only then takes another order.
- **ASGI**: The waiter takes an order, passes it to the kitchen, and while the kitchen works on it, they take more orders.

---

### FastAPI Features ✨

- **Fast**: Very fast due to ASGI support.
- **Data Validation**: Automatically checks if the data sent to your API is valid using Pydantic.
- **Easy to Use**: With automatic API documentation (Swagger UI).

---

## Concepts 💡

### CRUD (Create, Read, Update, Delete) 🔄

CRUD is an acronym for four functions that are used to manipulate data in a data storage application:

- **CREATE** - Create a resource
- **READ** - Read a resource
- **UPDATE** - Update a resource
- **DELETE** - Delete a resource

---

### What is a RESOURCE? 🛠️

A **Resource** in FastAPI is the data that an API provides or allows us to manipulate. This is accessible through an endpoint.

---

### Handling Data with Pydantic 🧑‍💻

`Pydantic` helps ensure that the data your API receives is in the correct format, transforming it into structured Python objects for easy manipulation.

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str
    price: float
```

### PATCH Request 📝

A **PATCH** request is used to partially update data on a server. It only modifies the fields you specify.

---

## PostgreSQL Integration 🗃️

When working with PostgreSQL, you'll need an **Object Relational Mapper (ORM)** to interact with the database using Python objects instead of raw SQL queries.

### ORM (SQLAlchemy) 🧑‍💻

`SQLAlchemy` is the most popular ORM for Python. It bridges the gap between your Python application and PostgreSQL, allowing you to query and modify your data using Python code.

---

### Managing Secrets with `.env` 🔒

Using an `.env` file helps manage sensitive configuration information like database credentials:

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=mydb
DB_USER=myuser
DB_PASSWORD=mypassword
```

Make sure to keep this file secure and avoid sharing it.

---

## Asynchronous Database Operations ⚡

FastAPI supports asynchronous database interactions using async DB APIs, ensuring non-blocking operations for high-performance applications.

```python
from sqlalchemy.ext.asyncio import AsyncSession

async with AsyncSession(engine) as session:
    result = await session.execute(select(User).filter_by(name='John'))
    user = result.scalars().first()
```

---

## JWT Authentication 🔑

### How JWT Works 🛡️

JWT (JSON Web Token) authentication verifies the identity of users and securely shares information between parties.

- **Header**: Describes how the token is structured.
- **Payload**: Contains user information (e.g., user ID, email).
- **Signature**: Ensures the token is authentic and hasn't been tampered with.

```json
{
  "header": {
    "alg": "HS256",
    "typ": "JWT"
  },
  "payload": {
    "sub": "1234567890",
    "name": "John Doe",
    "iat": 1516239022
  },
  "signature": "somerandomsignature"
}
```

---

## Token Pair: Access & Refresh Tokens 🔄

- **Access Token**: Used to access protected resources, expires in 5-15 minutes.
- **Refresh Token**: Used to obtain a new Access Token when the current one expires.

---

## Redis for Token Revocation 🧑‍💼

**Redis** is a fast, in-memory key-value store often used for session management. It helps with token revocation by allowing fast access to check whether a token has been invalidated.

```python
import redis

r = redis.Redis(host='localhost', port=6379, db=0)
r.set('user_token_123', 'valid', ex=3600)
```

---

## Role-Based Access Control (RBAC) 🔒

RBAC ensures users can only access resources or perform actions they're authorized for. 

### Example Roles:
- **Admin**: Full access to create, read, update, and delete resources.
- **User**: Can only read or create certain resources.
- **Guest**: Can only view public data.

---

## SQL Electron ⚡

**SQL Electron** is an open-source SQL client for easy management of your databases. It allows you to run SQL queries and manage databases through an intuitive interface.

---

## Reverse Relationships & Lazy Loading 🛠️

- **Reverse Relationships**: Access related data without explicitly defining the relationship in both tables.
- **Lazy Loading**: Fetch data only when needed, improving performance by reducing the initial load time.

```python
# Example of Lazy Loading
session.query(Parent).filter(Parent.id == 1).one()
```

---

## Middleware 🧑‍💻

Middleware in FastAPI sits between the client and your routes, allowing you to process requests and responses.

```python
from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def add_custom_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Custom-Header"] = "Hello"
    return response
```

---

## Conclusion 🎉

FastAPI is a powerful, fast, and modern framework for building APIs. It simplifies the creation of APIs with features like asynchronous programming, data validation, and easy integration with databases like PostgreSQL. By leveraging tools like JWT, Redis, and Role-Based Access Control (RBAC), you can ensure secure and efficient user management in your application.
