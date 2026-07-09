# py-bookstore-api

This is a simple library API built with FastAPI and SQLModel. It stores books and categories in PostgreSQL, and it is designed to be easy to run locally for your assignment.

## What this project contains

- `library-api/main.py` — the FastAPI application
- `library-api/models/book.py` — book data model
- `library-api/models/category.py` — category data model
- `library-api/database/session.py` — database session setup
- `library-api/docker-compose.yml` — PostgreSQL service definition
- `.env` — database connection configuration

## Running the project locally

### 1. Make sure PostgreSQL is available

This project uses the database URL from `library-api/.env`:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/library_db
```

If you want to use Docker to run PostgreSQL, go into the `library-api` folder and start the service:

```bash
cd library-api
docker compose up -d
```

### 2. Activate the Python virtual environment

From the project root:

```bash
source bookstore-env/bin/activate
```

### 3. Install dependencies (if needed)

If you have not already installed the app dependencies, install them inside the virtual environment. For example:

```bash
pip install fastapi uvicorn sqlmodel psycopg2-binary python-dotenv
```

### 4. Start the API server

From the `library-api` folder:

```bash
cd library-api
uvicorn main:app --reload --port 8000
```

### 5. Open the API docs

In your browser, go to:

```
http://127.0.0.1:8000/docs
```

This is where you can test endpoints like `POST /books`, `GET /books`, and `GET /books/search`.

## Notes for the assignment

- `POST /books` creates a new book record in PostgreSQL.
- `POST /categories` creates a category record.
- `GET /books/search` searches by query, author, and title.
- The project automatically creates database tables on startup via `SQLModel.metadata.create_all(engine)`.

## Tips

- If you make any code changes, restart the uvicorn server or use `--reload`.
- If the database schema changes, you may need to drop and recreate tables or restart the DB service.
- If you use pgAdmin, connect to the database at `localhost:5432` using `postgres` / `postgres`.

## Git / Docker ignore files

- `.gitignore` hides local files like the virtual environment, Python cache, and `.env`.
- `.dockerignore` ignores the same local files when building or using Docker contexts.
