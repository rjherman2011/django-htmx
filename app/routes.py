from app.crud import CRUD
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.config import Settings

from datetime import date

settings = Settings()
templates = Jinja2Templates(directory=settings.TEMPLATE_DIR)
router = APIRouter()

@router.get("/")
def index(request: Request):
    db = CRUD().with_table("artist_info")
    random_artist = db.get_random_item()
    return templates.TemplateResponse(f"main.html", 
                                      {
                                          "request": request,
                                          "page_title": "index",
                                          "page_description": "Build with TailwindCSS and htmx",
                                          "random_artist": random_artist
                                        })

@router.get("/Date")
def date(requeste: Request):
    today = date.today()

    return today