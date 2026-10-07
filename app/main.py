from fastapi import FastAPI

from app.api.routes import health, meal_plans, users
from app.db.base import Base
from app.db.session import engine
from app.models import meal_plan, user

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Meal Planner API")

app.include_router(health.router)
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(meal_plans.router, prefix="/meal-plans", tags=["meal-plans"])
