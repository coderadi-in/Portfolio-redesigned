'''coderadi &bull; Base router for the site'''

# ? IMPORTING LIBRARIES
from flask import Blueprint, render_template, redirect, url_for, flash, request
from plugins.models import Enquiry
from plugins import *

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

# | ARTICLES ROUTE
@router.route('/coding-greatness/articles/<article>')
def show_article(article):
    return render_template(f'articles/{article}.html')

# & PROJECTS ROUTE
@router.route('/projects/')
def projects():
    return render_template('pages/projects.html')

# | PROJECT-DOC ROUTE
@router.route('/projects/<project>')
def show_project(project):
    return render_template(f'docs/{project}.html')

# & WORK-WITH-US ROUTE
@router.route('/work/')
def work():
    return render_template('pages/work.html')

# & ABOUT ROUTE
@router.route('/about/')
def about():
    return render_template('pages/about.html')

# & CONTACT ROUTE
@router.route('/contact/', methods=['GET', 'POST'])
def contact():
    if (request.method == 'GET'):
        return render_template('pages/contact.html')
    
    else:
        # | GETTING FORM DATA
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # | SAVING ENQUIRY
        new_enquiry = Enquiry(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        db.session.add(new_enquiry)
        db.session.commit()

        # | NOTIFYING THE ADMIN
        notify(
            f"""Hey, you've received a new enquiry on coderadi.in!
Name: {name}
Email: {email}
Subject: {subject}
Message: {message}
"""
        )