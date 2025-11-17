from fastapi import FastAPI

from .db import Base, engine
from .routers import users

# Create database tables
Base.metadata.create_all(bind=engine)

# This MUST be named "app" because uvicorn looks for "app.main:app"
app = FastAPI(title="FastAPI Secure User App")


@app.get("/")
def root():
    return {"message": "OK"}


# Include the users router
app.include_router(users.router)

