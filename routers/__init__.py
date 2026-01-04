'''coderadi &bull; ROUTERS initializer'''

# ? IMPORTING LIBRARIES
from routers.router import router
from routers.api import api

# * FUNCTION TO BIND ROUTERS TO SERVER
def bind_routers(server):
    server.register_blueprint(router)
    server.register_blueprint(api)