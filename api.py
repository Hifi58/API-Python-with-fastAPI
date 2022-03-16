from fastapi import FastAPI

app = FastAPI()

###################
# Welcome message #
###################

@app.get("/")
async def hello_world():
    return {"Welcome on HELP Your Meal API !"}

###################
## Get for Stock ##
###################

@app.get("/stock/{stock_id}")
async def get_stock(stock_id: int):
    return {"stock_id": stock_id}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)