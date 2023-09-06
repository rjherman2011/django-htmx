from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.config import Settings

settings = Settings()
templates = Jinja2Templates(directory=settings.TEMPLATE_DIR)
router = APIRouter()

@router.get("/")
def index(request: Request):
    return templates.TemplateResponse(f"main.html", 
                                      {
                                          "request": request,
                                          "page_title": "index",
                                          "page_description": "Build with TailwindCSS and htmx"
                                        })