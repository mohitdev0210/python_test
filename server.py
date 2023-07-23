import base64
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from urllib.parse import unquote

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/api/example")
async def get_example(request: Request):
    try:
        query_param = request.query_params.get("query", "")
        if not query_param or query_param == "":
            return JSONResponse(status_code=409, content={"success": True, "message": "Required Data is missing"})
        decodedQuery = unquote(query_param)
        decoded_data = base64.b64decode(decodedQuery.encode("utf-8"))
        decoded_query = decoded_data.decode("utf-8")
        return JSONResponse(status_code=200, content={"success": True, "data": decoded_query})
    except ValueError as e: 
        return JSONResponse(status_code=409, content={"success": False, "message": str(e)})

@app.post("/items")
def read_item(item_id: Request):
    print("console")
    return {"item_id": item_id}
print(__name__)
if __name__ == "__main__":
    
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=9009, reload=True)
