from flask import Flask, redirect

from keys import SERVER_SECRET

from routes.auth.auth import auth_bp
from routes.main.main import main_bp

from models.user import User
from models.food import Food

app = Flask(__name__)

app.secret_key = SERVER_SECRET

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(main_bp, url_prefix="/main")

@app.route("/")
def init_page():
  return redirect("/auth/login")

User.create_users_table()
Food.create_foods_table()

if __name__ == '__main__':
    app.run(host='0.0.0.0')