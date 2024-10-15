from fastapi import FastAPI

app = FastAPI()

# 1. first step
@app.get("/")
async def root():
    # return ["Hello", "World"]
    # return "Hello World"
    # return 23
    return {"message": "Hello World"}

# 2. Path Parameters
"""Order Matters"""
@app.get("/items/me")
async def read_item(): 
    return {"item_id": "me"}

"""
Path Parameters
Path Parameters with types
"""
@app.get("/items/{item_id}")
# async def read_item(item_id):
async def read_item(item_id: int): # Data conversion and Data validation 数据转换并校验
    return {"item_id": item_id}

"""Predefined values"""
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    
@app.get("/models/{model_name}") # Input should be 'alexnet', 'resnet' or 'lenet'
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


# 3. Query Parameters
""""""
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/books/")
async def get_books(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]