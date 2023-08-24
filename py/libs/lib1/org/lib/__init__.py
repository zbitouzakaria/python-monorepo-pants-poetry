from pydantic import BaseModel


class Foo(BaseModel):
    name: str


class Bar(BaseModel):
    name: str
