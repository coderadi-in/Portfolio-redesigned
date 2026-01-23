'''coderadi &bull; Database models file for the project.'''

# ? IMPORTING LIBRARIES
from plugins import *

# | PROJECTS DATABASE MODEL
class Project(db.Model):
    '''Saves the case study of the projects I've built.
    
    ## Params
    - id: Integer, `primary`
    - title: String, `required`
    - desc: TEXT
    - cover: String, `required`
    - url: String, `required`'''

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(20), nullable=False)
    desc = db.Column(db.TEXT)
    cover = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(50), nullable=False)

# | ENQUIRY DATABASE MODEL
class Enquiry(db.Model):
    '''Saves the enquiry data made by visitors.
    
    ## Params
    - id: Integer, `primary`
    - name: String, `required`
    - email: String, `required`
    - subject: String, `required`
    - message: TEXT'''

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    message = db.Column(db.TEXT)