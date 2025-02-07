from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import mysql.connector
from data.dao.dao_armas import DaoArmas
from data import database 
from fastapi.responses import RedirectResponse


app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


inventory = {
    "AK-47": None,
    "AWP": None,
    "Desert Eagle": None,
    "M4A1": None,
    "Glock/USP": None,
}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Ruta principal"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/inventario", response_class=HTMLResponse)
async def inventario(request: Request):
    """Página para gestionar el inventario"""
    return templates.TemplateResponse("inventario.html", {"request": request, "inventory": inventory})

@app.post("/inventario")
async def update_inventory(
    request: Request,
    weapon: str = Form(...),
    skin: str = Form(...),
    float_value: float = Form(...),
    condition: str = Form(...),
    price: float = Form(...),
):
    """Actualiza el inventario con los datos seleccionados"""
    inventory[weapon] = {
        "skin": skin,
        "float": float_value,
        "condition": condition,
        "price": price,
    }
    return templates.TemplateResponse("inventario.html", {"request": request, "inventory": inventory})

@app.get("/resumen", response_class=HTMLResponse)
async def get_resumen(request: Request):
    """Genera el resumen del inventario final (vista previa antes de abrir cajas)"""
    total = sum(item["price"] for item in inventory.values() if item)
    return templates.TemplateResponse("resumen.html", {"request": request, "inventory": inventory, "total": total})

dao_armas = DaoArmas()

@app.get("/stats", response_class=HTMLResponse)
async def stats(request: Request):
    armas = dao_armas.get_all(database.connection())
    return templates.TemplateResponse("stats.html", {"request": request, "armas": armas})


@app.post("/stats")
async def calculate_rank(request: Request, faceit_elo: int = Form(...)):
    """Calcula el rango basado en el ELO de Faceit"""
    if faceit_elo < 500:
        rango = "Nivel 1"
    elif 501 <= faceit_elo < 750:
        rango = "Nivel 2"
    elif 751 <= faceit_elo < 900:
        rango = "Nivel 3"
    elif 901 <= faceit_elo < 1050:
        rango = "Nivel 4"
    elif 1051 <= faceit_elo < 1200:
        rango = "Nivel 5"
    elif 1201 <= faceit_elo < 1350:
        rango = "Nivel 6"
    elif 1351 <= faceit_elo < 1530:
        rango = "Nivel 7"
    elif 1531 <= faceit_elo < 1750:
        rango = "Nivel 8"
    elif 1751 <= faceit_elo < 2000:
        rango = "Nivel 9"
    else:
        rango = "Nivel 10"
    return templates.TemplateResponse("stats.html", {"request": request, "rango": rango, "elo": faceit_elo})

@app.post("/armas/create")
async def create_arma(request: Request, nombre: str = Form(...), skin: str = Form(...), precio: str = Form(...), float_skin: str = Form(...), stattrack: bool = Form(False)):
    dao_armas.insert(database.connection(), nombre, skin, precio, float_skin, stattrack) 
    return RedirectResponse(url="/stats", status_code=303)

@app.post("/armas/update")
async def update_arma(request: Request, id: int = Form(...), new_nombre: str = Form(...)):
    dao_armas.update(database.connection(), id, new_nombre)
    return RedirectResponse(url="/stats", status_code=303)

@app.post("/armas/delete")
async def delete_arma(request: Request, id: int = Form(...)):
    dao_armas.delete(database.connection(), id)
    return RedirectResponse(url="/stats", status_code=303)