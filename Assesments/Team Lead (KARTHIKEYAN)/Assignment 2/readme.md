# Assignment 2 - Flask Application
- [x] Create a Flask App
- [x] Add the Home page, About Page
- [x] Add the Bootstrap
- [x] Add the Sign in page and add the Signup Page with database connectivity
- [x] Use IBM Db2 as Database

## How to execute? 

> This code will also execute locally so it is not mandatory for you to provide ibm db2 credentials so step 1 and 2 is not mandatory
 
**step 1**  _(optional but needed for IBM DB2)_

👇 replace with your IBM DB2 Credentials before executing

``` python
conn = ibm_db.connect("DATABASE=<databasename>;HOSTNAME=<your-hostname>;PORT=<portnumber>;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=<username>;PWD=<password>",'','')

```

**step 2** _(optional but needed for IBM DB2)_

Download 'DigiCertGlobalRootCA.crt' file from IBM DB2 console and paste it along with 'app.py' file

**step 3** _Must_

- ```python -m flask run```  
- (or)  
- ```flask run```
- visit localhost:5000