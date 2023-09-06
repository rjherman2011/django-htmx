from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.config import Settings
from app.routes import router

settings = Settings()

def get_app() -> FastAPI:
    """Create a FastAPI app with the specified settings."""

    app = FastAPI(**settings.fastapi_kwargs)

    app.include_router(router)

    app.mount("/static", StaticFiles(directory=settings.STATIC_DIR), name="static")

    return app


app = get_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)