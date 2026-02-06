from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

@router.get("", response_class=HTMLResponse, tags=["index"])
async def get_page(request: Request):
    templates = Jinja2Templates("../templates")
    return templates.TemplateResponse("index.html", {"request": request}) 
