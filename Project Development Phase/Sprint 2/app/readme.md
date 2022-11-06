# Nutrition assistant Application

### Project structure

- **/pages** view
- **/controllers** logic
- **/models** DB model (data)
- **/utils** third party api methods

### How to execute?

- add keys in [keys_frame.py](keys_frame.py)
- rename the keys_frame.py to keys.py
- add DigiCertGlobalRootCA.crt from ibm_db2 in this dir (./app)
- ```python -m flask run```  
- (or)  
- ```flask run```

# Routes

- http://127.0.0.1:5000/auth/login
- http://127.0.0.1:5000/auth/register
- http://127.0.0.1:5000/main