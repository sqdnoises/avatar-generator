import uvicorn
from os import urandom
from base64 import b64encode
from fastapi import FastAPI, Response
from generate import generateImage

def random():
    return b64encode(urandom(16)).decode()

app = FastAPI(openapi_url = "")

@app.get("/{id}")
async def id(id: str, size: int = 512, square: bool = False):
    return Response(content=generateImage(id, size, square), media_type="image/svg+xml")

@app.get("/")
async def root(size: int = 512, square: bool = False):
    return Response(content=generateImage(random(), size, square), media_type="image/svg+xml")

@app.get("/favicon.ico")
async def favicon():
    return "/"

uvicorn.run(app, port=5050)