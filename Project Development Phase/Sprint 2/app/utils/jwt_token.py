from telnetlib import SE
import jwt
from keys import SERVER_SECRET
from flask import make_response, redirect, request, session

def generate_token(payload):    
  return jwt.encode(payload, SERVER_SECRET, algorithm="HS256")

def decode_token(token):    
    return jwt.decode(token, SERVER_SECRET, algorithms=["HS256"])

def validate_token(func):
    def wrapper(*args, **kwargs): 
        try:
            token = request.cookies.get('access-token')   
            if token == None:
              raise Exception()              
        except:
            return redirect("/")
        
        try:
            session['user'] = jwt.decode(token, SERVER_SECRET, algorithms=["HS256"])            
            return func(*args, **kwargs)
        except Exception as e:     
            return redirect("/")
            
    wrapper.__name__ = func.__name__
    return wrapper