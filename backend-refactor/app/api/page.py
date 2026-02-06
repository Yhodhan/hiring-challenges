import os 
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

current_dir = os.path.dirname(os.path.realpath(__file__))
temp_path = os.path.join(current_dir, "../", "templates")

@router.get("", response_class=HTMLResponse, tags=["index"])
async def get_page(request: Request):
    templates = Jinja2Templates(temp_path)
    return templates.TemplateResponse("index.html", {"request": request}) 
