from fastapi import APIRouter
from fastapi import FastAPI, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
#
from config.database import Session
from models.command import Command as CommandModel
#
from services.command import CommandService
#
from schemas.command import Command

command_router = APIRouter()

@command_router.get('/commands/', tags=['Commands'], response_model=List[Command], status_code=200)
def get_commands() -> List[Command]:
    db = Session()
    result = CommandService(db).get_commands()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@command_router.get('/commands/{id}', tags=['Commands'], response_model=Command, status_code=200)
def get_command(id: int = Path(ge=1, le=200)) -> Command:
    db = Session()
    result = CommandService(db).get_command() # filtrado por id, y first para que nos lo acomode por id DE PARTE DE SERVICES
    if not result:
        return JSONResponse(status_code=404, content={"message": "No encontrado."})
        #
    return JSONResponse(status_code=200, content=jsonable_encoder(result)) #jsonable es para que no nos de error a la hora de mandar el result
    
@command_router.get('/commands', tags=['Commands'], response_model=List[Command])
def get_command_by_category(category: str) -> List[Command]:
    db = Session()
    result = CommandService(db).get_command_by_category(category)
    if not result:
        return JSONResponse(status_code=404, content={"message": "No existe la categoria."})
        #
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@command_router.post('/commands/', tags=['Commands'], status_code=201, response_model=dict)
def create_command(command: Command) -> dict:
    db = Session()
    CommandService(db).create_command(command)
    return JSONResponse(status_code=201, content={"message": "Se registro el comando."})

@command_router.put('/commands/{id}', tags=['Commands'], status_code=200, response_model=dict)
def update_command(id: int, command: Command) -> dict:
    db = Session()
    result = CommandService(db).get_command(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "No encontrado."})
    CommandService(db).update_command(id, command)
    return JSONResponse(status_code=200, content={"message": "Se modifico el comando."})

@command_router.delete('/commands{id}', tags=['Commands'], status_code=200)
def delete_command(id: int):
    db = Session()
    result: CommandModel = db.query(CommandModel).filter(CommandModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "No encontrado."})
    CommandService(db).delete_command(id)
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el comando."})