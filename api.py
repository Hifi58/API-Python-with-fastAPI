from fastapi import FastAPI
from routes.index import user

app = FastAPI()
app.include_router(user)

@app.get("/")
async def welcome():
    return {"welcome " : "creator"}