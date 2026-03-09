from fastapi import FastAPI, Request, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.exceptions import RequestValidationError

from plant_api.services.plant_service import PlantService
from plant_api.database.memory_db import MemoryDB
from plant_api.models.schemas import PlantCreateSchema

app = FastAPI(
    title="Plant API",
    description="API สำหรับจัดการข้อมูลพืช Flower และ Tree",
    version="1.0.0"
)

templates = Jinja2Templates(directory="plant_api/templates")
app.mount("/static", StaticFiles(directory="plant_api/static"), name="static")

repository = MemoryDB()
service = PlantService(repository)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Handle Pydantic validation errors"""
    errors = []
    for error in exc.errors():
        field = error["loc"][1] if len(error["loc"]) > 1 else "unknown"
        msg_type = error["type"]
        
        if msg_type == "value_error.number.not_gt":
            errors.append(f"{field}: ตัวเลขต้องมากกว่า 0")
        elif msg_type == "string_type":
            errors.append(f"{field}: ต้องเป็นข้อความ")
        elif msg_type == "int_type":
            errors.append(f"{field}: ต้องเป็นตัวเลข")
        elif msg_type == "enum":
            errors.append(f"{field}: ต้องเป็น flower หรือ tree")
        elif msg_type == "missing":
            errors.append(f"{field}: จำเป็น")
        else:
            errors.append(f"{field}: {error['msg']}")
    
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": " | ".join(errors)},
    )


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
    """
    return service.get_all_plants()


@app.post("/plants", status_code=status.HTTP_201_CREATED, tags=["Plants"], summary="เพิ่มพืชใหม่")
def add_plant(data: PlantCreateSchema):
    """
    เพิ่มพืชใหม่ลงในระบบ
    
    **Request body:**
    - `id`: (int) ID ของพืช (ต้องมากกว่า 0)
    - `name`: (str) ชื่อพืช
    - `scientific_name`: (str) ชื่อวิทยาศาสตร์ของพืช
    - `biome`: (str) ไบโอมที่พืชนั้นอยู่
    - `type`: (str) ประเภทพืช: "flower" หรือ "tree"
    
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
    try:
        result = service.add_plant(data.model_dump())
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=result
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="เกิดข้อผิดพลาดในระบบ"
        )