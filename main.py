from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Hello API")


class HelloRequest(BaseModel):
    name: str = Field(min_length=1)


class HelloResponse(BaseModel):
    name: str


@app.post("/hello")
def hello(payload: HelloRequest) -> HelloResponse:
    return HelloResponse(name=payload.name)
