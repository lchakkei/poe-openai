import os
import nest_asyncio

DEFAULT_MODEL = os.getenv("BOT", default="gpt-3.5-turbo")
LISTEN_PORT = int(os.getenv("PORT", default=10000))
BASE_URL = os.getenv("BASE", default="https://api.poe.com/bot/")

from fastapi import FastAPI, Request, Header, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

from typing import AsyncGenerator
import json

from fastapi_poe.types import ProtocolMessage
from fastapi_poe.client import get_bot_response

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}