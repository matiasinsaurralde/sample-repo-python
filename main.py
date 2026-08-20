import re
import subprocess

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

# Absolute or relative paths only; no shell metacharacters or ls flags.
_SAFE_PATH = re.compile(r"^(?!\-)[A-Za-z0-9._/\-]+$")

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
    if not _SAFE_PATH.fullmatch(path):
        raise HTTPException(status_code=400, detail="invalid path")
    result = subprocess.run(
        ["ls", "--", path],
        capture_output=True,
        text=True,
        shell=False,
    )
    return {
        "stdout": result.stdout,
        "stderr": result.stderr,
        "returncode": result.returncode,
    }
