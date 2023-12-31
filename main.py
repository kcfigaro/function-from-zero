"""
This is the Wikibot webapp using FastAPI with json payload
"""
from fastapi import FastAPI
from pydantic import BaseModel
from mylib.bot import scrape
import uvicorn

app = FastAPI()


class Item(BaseModel):
    name: str
    length: int


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/scrape/")
def scrape_wiki(item: Item):
    result = scrape(item.name, item.length)
    payload = {"wikipage": result}
    # retrun payload with json
    return payload


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Run this app with uvicorn main:app --reload
