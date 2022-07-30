from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    num1: int
    num2: int


app = FastAPI()


@app.post("/multiply")
def multiply(item: Item):
    result = {
       "result": item.num1 * item.num2
    }
    return result
