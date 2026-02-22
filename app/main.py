from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

@app.get("/add")
def add(a: int = Query(...), b: int = Query(...)):
    result = a + b
    return {"result": result}
