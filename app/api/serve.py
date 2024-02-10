from fastapi import APIRouter, Depends

from app.dependencies import get_gpt_model, get_gpt_encoder, get_gpt_decoder
from pydantic import BaseModel

serve_router = APIRouter()


# Simple GET endpoint
@serve_router.get("/hello")
def hello_world():
    return {"message": "Hello, world!"}
