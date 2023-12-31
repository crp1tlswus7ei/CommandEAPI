import typing
from typing import Union
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
#
from starlette.middleware.base import BaseHTTPMiddleware, DispatchFunction, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp

class ErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Union[Response, JSONResponse]:
        try:
            return await call_next(request)
        except Exception as e: 
            return JSONResponse(status_code=500, content={'error': str(e)})
        
# Este hermoso codigo nos maneja los errores que no tengamos cotrolados en toda la basse de datos