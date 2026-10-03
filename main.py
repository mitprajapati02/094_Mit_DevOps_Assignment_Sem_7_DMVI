"""Main FastAPI application entrypoint."""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from controllers.student_controller import seed_sample_students
from routes.student_routes import router as student_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan context to seed initial data on startup."""
    # Seed sample student records on startup for immediate testing
    seed_sample_students()
    yield


app = FastAPI(
    title="FastAPI - Student CRUD Application",
    description="PRAJAPATI MITKUMAR JAYANTIBHAI. ENROLL: 202326900094, Assignment . A university student management REST API built with FastAPI using local in-memory storage. ",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(student_router)


@app.get("/", include_in_schema=False)
def root_redirect():
    """Redirect root path to interactive Swagger documentation."""
    return RedirectResponse(url="/docs")
