from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from plant_api.services.plant_service import PlantService
from plant_api.database.memory_db import MemoryDB

app = FastAPI(
    title="Plant API",
    description="API สำหรับจัดการข้อมูลพืช Flower และ Tree",
    version="1.0.0"
)

templates = Jinja2Templates(directory="plant_api/templates")
app.mount("/static", StaticFiles(directory="plant_api/static"), name="static")

repository = MemoryDB()
service = PlantService(repository)


@app.get("/", response_class=HTMLResponse, tags=["Web"])
def home(request: Request):
    """
    หน้า Home แสดงข้อมูลพืชทั้งหมด
    """
    plants = service.get_all_plants()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "plants": plants}
    )


@app.get("/plants", tags=["Plants"], summary="ดึงพืชทั้งหมด")
def get_plants():
    """
    ดึงข้อมูลพืชทั้งหมดในระบบ
    
    **Returns:**
    - List of plants with id, name, scientific_name
    """
    return service.get_all_plants()


@app.post("/plants", tags=["Plants"], summary="เพิ่มพืชใหม่")
def add_plant(data: dict):
    """
    เพิ่มพืชใหม่ลงในระบบ
    
    **Request body:**
    - `id`: (int) ID ของพืช
    - `name`: (str) ชื่อพืช
    - `scientific_name`: (str) ชื่อวิทยาศาสตร์ของพืช
    - `biome`: (str) ไบโอมที่พืชนั้นอยู่ (เช่น Tropical, Temperate, Desert, etc.)
    - `type`: (str) ประเภทพืช: "flower" หรือ "tree"
    - `created_at`: (str) วันที่เพิ่มข้อมูล (ISO format) - ถ้าไม่ใส่จะใช้เวลาปัจจุบัน
    
    **Example:**
    ```json
    {
        "id": 1,
        "name": "Rose",
        "scientific_name": "Rosa",
        "biome": "Temperate",
        "type": "flower"
    }
    ```
    """
    return service.add_plant(data)