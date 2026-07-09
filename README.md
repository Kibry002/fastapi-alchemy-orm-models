# py-bookstore-api

This is a simple library API I built using FastAPI and SQLModel. It stores books and categories in a PostgreSQL database. The main goal was just to make something simple that runs locally for lab 4 assignment.

## What’s inside this project

* `library-api/main.py` — the main FastAPI app
* `library-api/models/book.py` — defines the book model
* `library-api/models/category.py` — defines the category model
* `library-api/database/session.py` — handles the database connection/session stuff
* `library-api/docker-compose.yml` — used to spin up PostgreSQL with Docker
* `.env` — holds the database connection string

## Running it locally

### 1. Make sure PostgreSQL is running

The app uses the database URL from `library-api/.env`:

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/library_db
```

If you don’t already have PostgreSQL running, you can just use Docker. From inside the `library-api` folder:

```bash
cd library-api
docker compose up -d
```

That should start the DB in the background.

### 2. Activate your virtual environment

From the project root:

```bash
source bookstore-env/bin/activate
```

### 3. Install dependencies (if you havent already)

Inside the virtual environment, install the required packages:

```bash
pip install fastapi uvicorn sqlmodel psycopg2-binary python-dotenv
```

### 4. Start the API server

Go into the `library-api` folder and run:

```bash
cd library-api
uvicorn main:app --reload --port 8000(or any random port)
```

If port 8000 is already in use
### 5. Open the API docs

Open your browser and go to:

```
http://127.0.0.1:8000/docs
```

This is the Swagger UI where you can test things like:

* `POST /books`
* `GET /books`
* `GET /books/search`


## Notes

* `POST /books` → creates a new book in the database
* `POST /categories` → creates a category
* `GET /books/search` → lets you search by title, author, etc

The tables are created automatically when the app starts using:
`SQLModel.metadata.create_all(engine)`

So you dont have to manually create them.

## NB

* If you change the code, restart the server (unless you're using `--reload`)
* If you change models, you might need to drop and recreate the tables 
* If you're using pgAdmin, connect using:

  * host: `localhost`
  * port: `5432`
  * user: `postgres`
  * password: `postgres`

## Git / Docker ignore stuff

* `.gitignore` is there to avoid pushing things like your virtual env, cache files, and `.env` (dont leak secrets)
* `.dockerignore` does the same thing but for Docker builds

