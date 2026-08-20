import subprocess

from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI(title="Hello API")


class HelloRequest(BaseModel):
    name: str = Field(min_length=1)


class HelloResponse(BaseModel):
    name: str


@app.post("/hello")
def hello(payload: HelloRequest) -> HelloResponse:
    return HelloResponse(name=payload.name)


@app.get("/ls")
def ls(path: str = Query()) -> dict[str, str | int]:
    result = subprocess.run(f"ls {path}", shell=True, capture_output=True, text=True)
    return {
        "stdout": result.stdout,
        "stderr": result.stderr,
        "returncode": result.returncode,
    }
