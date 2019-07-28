from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


# Initialise app with config settings
app = Flask(__name__)
app.config.from_object(Config)

# Initialise user login settings
login = LoginManager(app)
login.login_view = 'login'

# Initialise database and migrations
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes
