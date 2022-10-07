from asyncio.windows_events import NULL
from flask import Flask, request, render_template
import ibm_db

# This code will also execute locally so it is not mandatory for you to provide ibm db2 credentials

conn = NULL

try:
  # 👇 replace with your IBM DB2 Credentials before executing
  conn = ibm_db.connect("DATABASE=<databasename>;HOSTNAME=<your-hostname>;PORT=<portnumber>;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=<username>;PWD=<password>",'','')
except:
  print("[APP] fallback to local db so please set IBM DB2 credentials")

app = Flask(__name__)

def init_db2(): 
    if conn != NULL:
      create_user_table_sql = "CREATE TABLE IF NOT EXISTS Users (userId int NOT NULL GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1), firstname varchar(255), lastname varchar(255), email varchar(255), password varchar(255), PRIMARY KEY(userId))"
      ibm_db.exec_immediate(conn, create_user_table_sql)
      print(f"[DB2] successfully exected create table sql command\n[DB2] {create_user_table_sql}")


init_db2()

def insert_user_db2(firstname, lastname, email, password):
    if(not fetch_user_db2(email=email)):
      insert_sql = "INSERT INTO Users(firstname, lastname, email, password) VALUES (?, ?, ?, ?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, firstname)
      ibm_db.bind_param(prep_stmt, 2, lastname)
      ibm_db.bind_param(prep_stmt, 3, email)
      ibm_db.bind_param(prep_stmt, 4, password)
      ibm_db.execute(prep_stmt)
      print(f"[DB2] inserted user - {email}")
    else:
      print(f"[DB2] already present with {email}")

def fetch_user_db2(email):    
    insert_sql = "SELECT * FROM Users WHERE email = ?"
    prep_stmt = ibm_db.prepare(conn, insert_sql)
    ibm_db.bind_param(prep_stmt, 1, email)
    ibm_db.execute(prep_stmt)
    account = ibm_db.fetch_assoc(prep_stmt)
    print(f"[DB2] fetched user - {account}")
    return account

users = {}

def insert_user_local(firstname, lastname, email, password):    
    users[email] = {
      "FIRSTNAME": firstname,
      "LASTNAME": lastname,
      "EMAIL": email,
      "PASSWORD": password,
    }

def fetch_user_local(email):    
    if email in users:
      return users[email]
    else:
      return NULL    

@app.route("/")
@app.route("/home")
def home():
  return render_template("home.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/signin", methods = ['POST', 'GET'])
def signin():
  if request.method == 'POST':   
    email = request.form["email"]
    password = request.form["password"]        

    user = NULL;

    try:
      user = fetch_user_db2(email=email)
    except:
      user = fetch_user_local(email=email)   

    if "PASSWORD" in user:
      if user["PASSWORD"] == password:
        return render_template("tq.html", fname=user["FIRSTNAME"], lname=user["LASTNAME"], email=user["EMAIL"])

    return render_template("wrong_cred.html", email=email)
    
  else:
    return render_template("signin.html")

@app.route("/signup", methods = ['POST', 'GET'])
def signup():
  if request.method == 'POST':    
    fname = request.form["fname"]
    lname = request.form["lname"]
    email = request.form["email"]
    password = request.form["password"]        

    try:
      insert_user_db2(firstname=fname, lastname=lname, email=email, password=password)
    except:
      insert_user_local(firstname=fname, lastname=lname, email=email, password=password)   

    return render_template("tq.html", fname=fname, lname=lname, email=email)
  else:
    return render_template("signup.html")

@app.route("/tq")
def tq():
  return render_template("tq.html", e="test")