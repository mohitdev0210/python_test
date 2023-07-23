import base64
import json
import pdb
from fastapi import Request
from urllib.parse import unquote
from fastapi.responses import JSONResponse
from  data.connection import db
from data.manager.user import userManager 
from datetime import datetime
userManager = userManager(db)

class User:
    
    async def create_user_profile(request: Request):
        try:
            query_param = await request.body()
            if not query_param or query_param == "":
                return JSONResponse(status_code=409, content={"success": True, "message": "Required Data is missing"})
            decodedQuery = unquote(query_param)
            user_data = json.loads(decodedQuery)
            userManager.create_user_profile(user_data)
            return JSONResponse(status_code=200, content={"success": True, "data": user_data})
        except ValueError as e:
            return JSONResponse(status_code=409, content={"success": False, "message": str(e)})

    async def get_user_profile(request: Request):
        try:
            query_param = request.query_params.get("query", "")
            if not query_param or query_param == "":
                return JSONResponse(status_code=409, content={"success": True, "message": "Required Data is missing"})
            search_query = {
                "email": unquote(query_param)
            }
            userProfile = userManager.get_user_profile(search_query)
            if userProfile:
                return JSONResponse(status_code=200, content={"success": True, "data": userProfile})
            else:
                return JSONResponse(status_code=404, content={"success": False, "message": "User not found"})
        except ValueError as e:
            return JSONResponse(status_code=409, content={"success": False, "message": str(e)})
        
    async def update_user_profile(request: Request):
        try:
            query_param = await request.body()
            if not query_param or query_param == "":
                return JSONResponse(status_code=409, content={"success": True, "message": "Required Data is missing"})
            user_data = unquote(query_param)
            search_query = {'email': user_data['email']}
            userManager.update_user_profile(search_query,{ "$set": user_data})
            return JSONResponse(status_code=200, content={"success": True, "message": 'Data updated successfully'})
        except ValueError as e:
            return JSONResponse(status_code=409, content={"success": False, "message": str(e)})

