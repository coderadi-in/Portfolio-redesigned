'''coderadi &bull; Plugins file'''

# ? IMPORTING PLUGINS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from twilio.rest import Client

# ? IMPORTING LIBRARIES
import os

# ! INITIALIZING PLUGINS
db = SQLAlchemy()
upgrade = Migrate()
client = Client(
    os.getenv('TWILIO_SID'),
    os.getenv('TWILIO_AUTH_TOKEN')
)

# * FUNCTION TO BIND PLUGINS TO SERVER
def bind_plugins(server):
    db.init_app(server)
    upgrade.init_app(server, db)

# * FUNCTION TO SEND WHATSAPP MESSAGE
def notify(body: str):
    client.messages.create(
        from_=os.getenv('TWILIO_WHATSAPP_FROM'),
        to=os.getenv('TWILIO_WHATSAPP_TO'),
        body=body,
    )