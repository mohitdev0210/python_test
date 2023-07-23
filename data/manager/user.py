from pymongo import MongoClient
from pydantic import ValidationError
from lib.errorLib import generate_error_msg
from data.models.user import User
import json
import pdb  # Import the pdb module
from datetime import datetime

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)



class userManager:

    def __init__(self, client):
        self.db = client
        self.collection = self.db['user']

    def create_user_profile(self, payload):
        try:
            new_user = User(**payload)
            self.collection.insert_one(new_user.model_dump())
            return new_user.__dict__
        except ValidationError as e:
            # Invalid payload
            error_msg = generate_error_msg('createUserProfile', e.errors())
            raise ValueError(error_msg)
        except Exception as e:
            # Other errors
            error_msg = generate_error_msg('createUserProfile', e)
            raise ValueError(error_msg)
        
    def get_user_profile(self, search_query):
        try:
            result = self.collection.find_one(search_query)
            if result:
                print('result', result)
                result['_id'] = str(result['_id'])
                result = json.loads(json.dumps(result, cls=CustomJSONEncoder))
                return result
            else:
                return None
        except Exception as e:
            error_msg = generate_error_msg('get_user_profile', e)
            raise ValueError(error_msg)
        
    def update_user_profile(self, search_query, update_query):
        try:
            result = self.collection.update_one(search_query, update_query)
            return result
        except Exception as e:
            error_msg = generate_error_msg('update_user_profile', e)
            raise ValueError(error_msg)
    

