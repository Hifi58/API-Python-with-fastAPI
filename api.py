from fastapi import FastAPI

app = FastAPI()

###################
# Welcome message #
###################

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

@app.get("/")
async def hello_world():
    return {"Welcome on HELP Your Meal API !"}


################################################
## Menu                                       ##
## .1 Users                                   ##
################################################



################################################
##                                            ##
##              .1 USERS                      ##
##                                            ##
################################################



###################
##   Get Users   ##
###################

@app.get("/user/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}

####################
##   Post Users   ##
####################


# @app.post("/add_user")
# async def add_user(user: User):
#     # db here
#     return {"new_user": User.dict}