'''coderadi &bull; Run command file'''

# ? IMPORTING LIBRARIES
from main import server

# ! RUNNING THE SERVER
if (__name__ == "__main__"):
    server.run(debug=True, host='0.0.0.0', port=5000)