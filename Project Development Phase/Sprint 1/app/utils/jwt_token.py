from telnetlib import SE
import jwt
from keys import SERVER_SECRET
from flask import make_response, Request, request

def generate_token(payload):    
  return jwt.encode(payload, SERVER_SECRET, algorithm="HS256")

def decode_token(token):    
    token = jwt.decode(token, SERVER_SECRET, algorithms=["HS256"])
    print("=====================================", token)
    return token

def validate_token(func):
    def wrapper(*args, **kwargs):
        try:
            token = request.cookies.get('access-token')   
            if token == None:
              raise Exception()              
        except:
            return make_response({"message": "Token not provided"}, 403)
        
        try:
            jwt.decode(token, SERVER_SECRET, algorithms=["HS256"])
            return func(*args, **kwargs)
        except Exception as e:
            return make_response({"message": "Invalid token provided"}, 403)   
    return wrapper