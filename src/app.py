from os import urandom
from base64 import b64encode

import uvicorn
from fastapi import FastAPI, Response

from generate import generate_avatar_svg


def random_string() -> str:
    """Return a random string."""
    return b64encode(urandom(16)).decode()


# Set OpenAPI URL to nothing to disable documentation routes
app = FastAPI(openapi_url="")


@app.get("/{seed}")
async def with_seed(seed: str, size: int = 512, square: bool = False) -> Response:
    """Generate an avatar using the given seed."""
    return Response(content=generate_avatar_svg(seed, size, square), media_type="image/svg+xml")


@app.get("/")
async def random(size: int = 512, square: bool = False) -> Response:
    """Generate an avatar randomly."""
    return Response(content=generate_avatar_svg(random_string(), size, square), media_type="image/svg+xml")


@app.get("/favicon.ico")
async def favicon() -> str:
    """The favicon? lmao"""
    return "/"


if __name__ == "__main__":
    uvicorn.run(app, port=5050)
