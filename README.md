# Meal Planner API

FastAPI backend scaffold for the meal planner project.

## Setup

1. Create and activate a virtual environment.
2. Install dependencies with `pip install -r requirements.txt`.
3. Copy `.env.example` to `.env` and set the required values.
4. Start the API with `uvicorn app.main:app --reload`.

The default database is a local SQLite file. To use PostgreSQL, set `DATABASE_URL`
to a SQLAlchemy URL such as
`postgresql+psycopg://username:password@localhost:5432/mealplanner`. The database
must exist before starting the application; `sql/01_create_database.sql` can be
used to create it.

API documentation is available at `/docs`; the health endpoint is `/health`.

Run tests with `pytest`.
