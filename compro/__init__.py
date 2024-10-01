import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Define APP
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

# Define DB
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

Migrate(app, db)

# Define login manager
login_manager = LoginManager()
login_manager.init_app(app)


from compro.core.views import core_bp
from compro.users.views import users_bp

app.register_blueprint(core_bp)
app.register_blueprint(users_bp)
