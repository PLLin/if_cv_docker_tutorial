import base64
import cv2
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    image: str


app = FastAPI()


@app.post("/get_shape")
def multiply(item: Item):
    image = base64.b64decode(item.image)
    image = np.frombuffer(image, np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    result = {
       "height": image.shape[0],
       "width": image.shape[1],
       "channel": image.shape[2]
    }
    return result
