# FastAPI Beyond CRUD

FastAPI is a modern framework for building web APIs in Python. It is a tool to create these APIs easily and quickly. It's like a special kitchen where you can prepare the dishes (APIs) faster, with fewer mistakes, and serve them to customers (applications). It's named FastAPI because it's very fast at handling requests, thanks to a technology called ASGI (Asynchronous Server Gateway Interface).

<p align="center">
  <img src="https://github.com/user-attachments/assets/398d5b4f-0efd-448a-8963-e005e73d3814" alt="FastAPI">
</p>

ASGI is a standard for a Python web applications to handle both synchronous and asynchronous tasks. Think of it as a bridge between a web server (like Uvicorn) and your Python application.

### Difference between WSGI and ASGI:-

* WSGI stands for Web Server Gateway Interface.
* Handles one request at a time per worker(synchronous).
* Struggles with modern requirements like real-time updates
  
* ASGI handles multiple requests simultaneously (asynchronous).
* Designed for real-time features and high-performance systems.
* Supports modern protocols like WebSockets

### How Does ASGI Work?

Imagine a busy restaurant:

* WSGI: A waiter takes one order, delivers it to the kitchen, waits for it to finish, and only then takes another order.
* ASGI: The waiter takes an order, passes it to the kitchen, and while the kitchen works on it, they take more orders.


FastAPI checks if the data sent to your API is valid. For example, if your API expects a number, and someone sends text, FastAPI will show an error automatically.


RestFox is a tool designed to help developers test and work with APIs. Developers often need to test APIs to make sure they work correctly. RestFox allows you to do this without needing to write extra code.

Pydantic is a Python library used in FastAPI to handle data validation and serialization. Think of it as a filter and organizer for data:

* It ensures that the data your API receives is in the correct format.
* It transforms the data into structured Python objects you can easily work with.

CRUD is an acronym for four functions that are used to manipulate data in a data storage application.

* CREATE - create a resource
* READ - read a resource
* UPDATE - update a resource
* DELETE - delete a resource

## What is a RESOURCE?

The data that an API provides or allows us to manipulate. This is accessible through an endpoint.


In FastAPI, the model_dump() method is part of Pydantic models and is used to convert a Pydantic object into a dictionary. This is helpful when you want to access or manipulate the data of a model in a simple, key-value format (like JSON).

A PATCH request is one of the HTTP methods used in web development. It is used to partially update data on a server. Unlike a PUT request, which typically replaces the entire resource, a PATCH request modifies only the fields you specify, leaving the rest of the data unchanged.

FastAPI supports various types of databases, including relational/SQL databases and non-relational/NoSQL databases. I am trying to using a relational database specifically PostgreSQL. PostgreSQL is an open-source relational database management system. It is a tool for storing, managing and retrieving data in an organized way using tables. 

While using PostgreSQL, we shall need to choose a way to interact with the database using the Python language. That introduces us to the concept of an Object Relational mapper (ORM).

An Object-Relational Mapper(ORM) is a tool that helps developers interact with a database using objects instead of writing SQL queries. It serves as a bridge between your programming language (like Python) and your database (like PostgreSQL or MySQL).


## How does ORM work?

Think of an ORM as a translator:

* In Code: You work with objects (like classes and objects in Python).
* Behind the Scenes: The ORM converts those objects into SQL queries and runs them in the database.
* Result: The ORM converts the database's response (rows and columns) back into objects that you can use in your code.


SQLAlchemy is the most popular ORM for Python, mapping objects to database tables and providing a high-level SQL language. While SQLAlchemy is powerful, SQLModel offers a seamless integration with SQLAlchemy and Pydantic.


A .env file is created when working with PostgreSQL in FastAPI to manage sensitive configuration information and enhance security, flexibility, and maintainability of the application. It stores sensitive data like:-

* Database connection details: DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD.
* API keys or secrets

It should not be shared with anyone.

An async DB API is a way to interact with a database in an asynchronous manner, enabling non-blocking operations. This is especially useful in modern web frameworks like FastAPI, which use asynchronous programming to handle multiple requests efficiently.


pydantic-settings is a Python library that makes it easy to manage configurations from various sources, like environment variables, .env files, or even hardcoded defaults. The SettingsConfigDict in pydantic-settings is a simple way to customize how your settings class works. It is used to configure things like where to load settings from (e.g. .env files), environment variable prefixes.


The async engine in SQLAlchemy (and libraries like SQLModel, which build on it) allows you to perform database operations asynchronously. This means that instead of blocking the program while waiting for a database operation to complete, the engine can perform other tasks during that time. This is particularly useful for modern web applications that need to handle many simultaneous requests efficiently.


An asynccontextmanager is a decorator provided by the contextlib module. It helps create asynchronous context mangers that can set up and clean up resources in a structured and clean way.


Lifespan is a way to define application-wide setup and teardown in FastAPI.

It's like saying:
* "When my app starts, do some setup."
* "When my app stops, do some cleanup."


UUID fields are helpful for creating unique identifier for records, ensuring they are unique across different systems without relying on sequential numeric IDs like INTEGER or BIGINT.


An AsyncSession is a special kind of session used to interact with a database asynchronously in Python applications. It's part of the SQLAlchemy library, which allows you to manage database operations efficiently, without blocking the rest of your program.


Dependency Injection (DI) in FastAPI is a way of providing the components (like database connections, authentication services, or any other utility) that your application needs, automatically.


A session in FastAPI when working with PostgreSQL is like a temporary workspace or a conversation between your application and the database. It's where all the interactions with the database happen during a request.


Alembic is a lightweight database migration tool for SQLAlchemy, which is a Python library used for interacting the databases. In simple terms, Alembic helps you manage changes to your database schema over time.


A migration is the process of making changes to your database schema. The schema is like the structure of your databases -- for e.g., adding or removing tables, changing columns, or modifying data types.

## JWT Authentication

JWT authentication is a method to verify the identity of users and securely share information between parties.

JWT stands for JSON Web Token, a standard for transmitting claims (information) among two parties. It is like a digital ID card given to users after they log in. It contains information about the user and is securely signed, so others can verify it hasn't been tampered with.

It looks like a long string of text and consists of three parts:
* Header: Explains how token is structured.
* Payload: Contains user information (e.g. user ID, email) and other data.
* Signature: Ensures the token is authentic and hasn't been changed.

### How JWT Authentication Works?

* A user sends their username and password to the server.
* The server checks the credentials (username and password) in the database. If correct, the server creates a JWT.
* The server sends the JWT back to their user. This is the user's "proof of login"
* When the user makes requests (like accessing protected routes), they attach the JWT in the Authorization header.
* The server checks if the JWT is valid (by verifying the signature). If valid, the user is allowed access. If not access is denied.

### HTTP Bearer Authentication

HTTP Bearer Authentication is a way for your application (client) to prove its identity to the server by sending a special token with every request. It's like showing a ticket to get access to a resource. 

How does it work?

* Bearer Token:
  - A Bearer Token is a unique string that proves you have permission to access certain data or perform actions on the server.
  - Think of it as a "digital key" or "access card."

* How the Token is Used:
  - When the client (e.g. your app or browser) sends a request to the server, it includes the token in the HTTP Authorization header.
  
* How the Server validates the Token:
  - The server checks if the token is valid.
  - If the token is valid, the server allows access to the requested resource.
  - If the token is invalid or missing, the server denies access, often returning a 401 Unauthorized error.

#### Steps of HTTP Bearer Authentication

* Login to Get a Token:
  - The client logs in by sending their credentials (e.g., username and password) to the server.
  - If the credentials are correct, the server generates a token and sends it back to the client.
  
* Send the Token with Requests:
  - For every request to a protected endpoint, the client includes the token in the Authorization header.

* Server Verifies the Token:
  - The server validates the token:
    - Is the token expired?
    - Is the token correct?
  - If valid, the server processes the request
  - If not, it denies access

* Access Protected Resources:
  - Once authenticated, the client can access the protected resources or performs actions allowed by the token.


## Token Pair
A Token Pair consists of two tokens - an access token and a refresh token. These tokens work together to securely manage user authentication and improve the user experience without requiring frequent logins.

* Access Token
  - Allows the client (e.g. your app) to access protected resources (like user data) on the server.
  - Access tokens expire quickly (e.g. in 5-15 minutes) for security reasons.
  - Sent in the Authorization header for each request to prove the user's identity.

* Refresh Token
  - Used to get a new Access Token when the current one expires.
  - Refresh tokens last longer (e.g. days, weeks, or months) because they're only exchanged between the client and server during token renewal.


## Revoking Tokens using Redis
Redis is a super-fast ,in memory database that stores data in key-value pairs.

It is commonly used for:
- Caching: Store frequently accessed data for quick retrieval
- Session Management: Track user sessions
- Data Expiry: Set a time-to-live (TTL) for temporary data.
  
Redis is perfect for managing tokens because:
- It's very fast.
- It can handle token expiration and revocation efficiently.

Token Revocation means "invalidating" a token before it expires.
This is important for security, for example:
- A user logs out
- A token is compromised (e.g. stolen)
- A session is terminated
  
When a token is revoked, the server ensures it cannot be used anymore.

Redis is ideal for managing tokens because:
- You can store tokens in Redis with a time-to-live (TTL) that matches their expiration time.
- You can delete tokens from Redis when revoking them, effectively invalidating them.


## Role-Based Access Control (RBAC)
Role-Based Access Control (RBAC) in FastAPI is a way to manage and enforce permissions for different users of your application based on their roles. It ensures that users can only access resources or perform actions they are authorized for.

RBAC means assigning specific roles to users, and each role has a set of permissions. For example:-
* Admin: Can create, read, update, and delete any resource.
* User: Can only read or create certain resources.
* Guest: Can only view public data.


## SQL Electron
SQL Electron or Sqlelectron is an open-source, lightweight, and user-friendly SQL client tool. It is designed to help developers and database administrators connect to various databases, run SQL queries, and manage databases through an intuitive graphical user interface (GUI).


## Reverse relationships
Reverse relationships are a way of navigating from one table to another in the opposite direction of a database relationship. This allow us to access related data without explicitly defining that relationship in both tables.


## Lazy loading
Lazy loading is a way of loading data on-demand rather than upfront. It means related data is not fetched from the database until you actually access it. 

This is useful when you're working with large datasets or relationships between tables. Instead of loading all the related data immediately, SQLModel will only fetch the data when you specifically need it.


## Middleware
Middleware is like a "filter" that sits between your FastAPI app and the client making the request. It lets you process requests before they reach your routes and modify responses before they are sent back to the client.

Think of middleware as a pipeline where:-
* A client sends a request - Middleware intercepts it.
* Middleware processes or checks the request.
* The request continues to your API's route (if allowed).
* After your API processes the request and generates a response, the middleware can modify the response before sending it back to the client.

FastAPI middleware is based on ASGI middleware, which is designed for asynchronous web servers. Middleware is implemented using a function or a class.

**Note**: We cannot raise exceptions and return them as responses within our middleware so we have to go ahead and return jsonResponse


## It's dangerous package
The It's dangerous package in Python is a library designed to handle secure data serialization and deserialization, ensuring that data remains safe when being transferred or stored. It is often used in web applications for tasks like creating and verifying secure tokens.


## Background Tasks with Celery and Redis
If you have a task in your app that takes a long time, like sending emails, processing a big file, or doing calculations, you don't want the user to wait for it to finish. Instead you can offload it to a background worker.

Celery is a tool that allows you to perform these tasks in the background. It lets your application do heavy work (like sending emails) outside the main request-response cycle so the app remains fast.

Celery runs tasks using workers. Workers are processes that listen for jobs and execute them.

Redis is a super-fast-in-memory database. It can act as a message broker for Celery. This means Redis stores and passes messages(tasks) from your app to Celery workers.

How Celery, Redis and Your App work together?

* App Sends Task: You send a task (e.g., send an email) from your FastAPI app to Celery.
* Redis Stores Task: Redis acts as a middleman and holds the task in a queue.
* Celery Worker Executes: Celery workers listen to Redis. Once they get a task, they execute it in the background.
* Task Completes: The task finishes (e.g., the email is sent), and the result is saved if needed.


## Flower
Flower is a real-time monitoring tool for Celery tasks. It provides a simple web-based UI to monitor and inspect the tasks, workers, and the overall status of your Celery system.
