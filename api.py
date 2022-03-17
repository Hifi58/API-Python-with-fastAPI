from fastapi import FastAPI

app = FastAPI()

###################
# Welcome message #
###################

@app.get("/")
async def hello_world():
    return {"Welcome on HELP Your Meal API !"}

###################
## Get for Users ##
###################

@app.get("/user/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)