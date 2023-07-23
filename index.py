import os
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from sqlalchemy import select
from data.connection import sqdb
from data.models.user import User

dotenv_path = '/path/to/.env'
load_dotenv(dotenv_path)

from routes import user
import data.modelList

app = FastAPI()

@app.get("/")
async def server_on():
    return {"success": True, "message": "Hello welcome to Python Server..."}

@app.get("/server/health")
async def check_server_health():
    return {"success": True, "message": "TSC Survey Server is running.."}

app.include_router(user.router, prefix="/api/users")

def controller():
    search_query = select(User)
    result = sqdb.execute(search_query)
    print(result)

controller()

if __name__ == "__main__":
    uvicorn.run("index:app", host="localhost", port=9009, reload=True)
