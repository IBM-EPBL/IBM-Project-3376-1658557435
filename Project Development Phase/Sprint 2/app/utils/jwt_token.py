import jwt
from keys import SERVER_SECRET
from flask import request, redirect, session
import requests

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
            
            res = requests.get(f'{request.root_url}auth/isvalid?token={token}&ss={SERVER_SECRET}').json()
            
            if res['status'] == True:
                session['user'] = res['user']
                return func(*args, **kwargs)
            else:
                raise res['error']

        except Exception as e:
            print(e)
            return redirect("/")
            
    wrapper.__name__ = func.__name__
    return wrapper