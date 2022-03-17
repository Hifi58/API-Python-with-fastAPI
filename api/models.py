import fastapi from FastAPI

import uvicorn

from typing import Optional

from pydantic import BaseModel

#####################################################
##                   MENU                          ##
##                                                 ##
##               1.User                            ##
#####################################################

class User(BaseModel):
    pk_id    : int
    mail     : str
    password : str 
    premium  : Optional[bool]