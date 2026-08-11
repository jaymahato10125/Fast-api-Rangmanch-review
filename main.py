from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables
from routes.reviews import router as reviews_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code here
    create_tables()
    print("Tables created successfully.")
    yield
    # Shutdown code here
    print("Shutting down the application.")

app = FastAPI(
    title="Rangmanch Review API", 
    description="Theatre reviews API for Pune Rangmanch",
    lifespan=lifespan
    )
app.include_router(reviews_router)

@app.get("/")
def root():
    return {"message": "Welcome to the Rangmanch Review API"}
