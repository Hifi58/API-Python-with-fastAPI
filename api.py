from fastapi import FastAPI

app = FastAPI()

#get
@app.get("/")
async def hello_world():
    return {"Welcome on HELP Your Meal API !"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)