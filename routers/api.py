'''coderadi &bull; API router for the site'''

# ? IMPORTING LIBRARIES
from flask import Blueprint, render_template, redirect, url_for, flash, request

# ! INITIALIZING API ROUTER
api = Blueprint('api', __name__)