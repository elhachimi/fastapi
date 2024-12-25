from fastapi import FastAPI

from src.api.modules.main import api_router


app = FastAPI()

app.include_router(api_router)
