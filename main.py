'''coderadi &bull; Main file of the project'''

# ? IMPORTING LIBRARIES
from flask import Flask, render_template
from plugins import *
from routers import *
import os

# ! LOADING VIRTUAL ENVIRONMENT
from dotenv import load_dotenv
load_dotenv('.venv/vars.env')

# ! BUILDING SERVER
server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
server.config['SECRET_KEY'] = os.getenv('KEY')

# ! BINDING PLUGINS & ROUTERS
bind_plugins(server)
bind_routers(server)

# ! INITIALIZING DATABASE
with server.app_context():
    db.create_all()

# ! ERROR HANDLERS
# & 404
@server.errorhandler(404)
def handle_404(error):
    return render_template('err/404.html')

# & 500
@server.errorhandler(500)
def handle_404(error):
    return render_template('err/500.html')