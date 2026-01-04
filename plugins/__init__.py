'''coderadi &bull; Plugins file'''

# ? IMPORTING LIBRARIES
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

# ! INITIALIZING PLUGINS
db = SQLAlchemy()
upgrade = Migrate()

# * FUNCTION TO BIND PLUGINS TO SERVER
def bind_plugins(server):
    db.init_app(server)
    upgrade.init_app(server, db)

