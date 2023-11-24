from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
#
from config.database import engine, Base#
from middlewares.error_handler import ErrorHandler
# from middlewares.jwt_bearer import JWTBearer
from routers.command import command_router
from routers.login_users import login_router

app = FastAPI()
app.title = "Ellay"
app.version = "1.0.0 Beta"
#
app.add_middleware(ErrorHandler)
# app.add_middleware(JWTBearer) Tenemos error aca de TypeError!
app.include_router(command_router)
app.include_router(login_router)

Base.metadata.create_all(bind=engine)