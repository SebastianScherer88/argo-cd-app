import os

import uvicorn
from fastapi import FastAPI

from utils import ValidUser, create_message

API_PORT = int(os.environ.get('API_PORT',8080))

demo_app = FastAPI()


@demo_app.get("/")
async def default_message():
    return {"message": create_message()}

@demo_app.get("/{user_name}/")
async def named_message(user_name: ValidUser = ''):
    return {"message": create_message(user_name)}

if __name__ == "__main__":
    uvicorn.run(demo_app, host="0.0.0.0", port=API_PORT)