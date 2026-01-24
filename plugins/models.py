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

# | ERROR-REPORT DATABASE MODEL
class ErrorReport(db.Model):
    '''Saves the report of error in the site.
    
    ## Params
    - id: Integer, `primary`
    - error_type: String
    - page_url: String
    - email: String
    - message: TEXT'''

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    error_type = db.Column(db.String(70))
    page_url = db.Column(db.String(70))
    email = db.Column(db.String(50))
    message = db.Column(db.TEXT)