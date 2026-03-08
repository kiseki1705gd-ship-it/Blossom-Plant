from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from plant_api.services.plant_service import PlantService
from plant_api.database.memory_db import MemoryDB

app = FastAPI()

templates = Jinja2Templates(directory="plant_api/templates")
app.mount("/static", StaticFiles(directory="plant_api/static"), name="static")

repository = MemoryDB()
service = PlantService(repository)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    plants = service.get_all_plants()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "plants": plants}
    )


@app.get("/plants")
def get_plants():
    return service.get_all_plants()


@app.post("/plants")
def add_plant(data: dict):
    return service.add_plant(data)