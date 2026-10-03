from fastapi import FastAPI
from fastapi.responses import RedirectResponse


app = FastAPI(
    title="FastAPI - Student CRUD Application",
    description="A university student management REST API built with FastAPI using local in-memory storage.",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)


@app.get("/", include_in_schema=False)
def root_redirect():
    """Redirect root path to interactive Swagger documentation."""
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
