'''coderadi &bull; Base router for the site'''

# ? IMPORTING LIBRARIES
from flask import Blueprint, render_template, redirect, url_for, flash, request

# ! INITIALIZING BASE ROUTER
router = Blueprint('router', __name__)

# & BASE ROUTE
@router.route('/')
def home():
    return render_template('pages/home.html')

# & CODING-THE-GREATNESS ROUTE
@router.route('/coding-greatness/')
def coding_greatness():
    return render_template('pages/coding-greatness.html')

# & PROJECTS ROUTE
@router.route('/projects/')
def projects():
    return render_template('pages/projects.html')

# & ABOUT ROUTE
@router.route('/about/')
def about():
    return render_template('pages/about.html')

# & CONTACT ROUTE
@router.route('/contact/')
def contact():
    return render_template('pages/contact.html')