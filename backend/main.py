from fastapi import FastAPI
from pymongo import MongoClient

client = MongoClient()
db = client["tweets"]

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/answer")
async def answer():
    items = []
    for item in db["elonmusk"].aggregate([{"$sample": {"size": 1}}]):
        item.pop("_id")
        items.append(item)
    answer = items[0]
    return answer


client.close()
