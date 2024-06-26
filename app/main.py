from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from .library.helpers import *
from app.routers import unsplash

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(unsplash.router)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = openfile("home.md")
    return templates.TemplateResponse("page.html",
                                      {"request": request, "data": data})


@app.get("/page/{page_name}", response_class=HTMLResponse)
async def page(request: Request, page_name: str):
    data = openfile(page_name + ".md")
    return templates.TemplateResponse("page.html",
                                      {"request": request, "data": data})
