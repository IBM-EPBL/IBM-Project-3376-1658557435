from flask import Flask

from routes.auth.auth import auth_bp
from routes.main.main import main_bp

from models.user import User

app = Flask(__name__)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(main_bp, url_prefix="/main")

User.create_users_table()