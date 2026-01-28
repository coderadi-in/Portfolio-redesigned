'''coderadi &bull; Base router for the site'''

# ? IMPORTING LIBRARIES
from flask import Blueprint, render_template, redirect, url_for, flash, request, send_file
from plugins.models import Enquiry, ErrorReport, Project
from plugins import *

# ! INITIALIZING BASE ROUTER
router = Blueprint('router', __name__)

# * FUNCTION TO FLASH `UNDER-DEVELOPMENT` MESSAGE
def flash_dev():
    flash("This website is under development, some functions may not work.", "info")

# & BASE ROUTE
@router.route('/')
def home():
    flash_dev()
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
    projects_ = Project.query.all()
    return render_template('pages/projects.html', data={
        'projects': projects_
    })

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
        # GETTING FORM DATA
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # SAVING ENQUIRY
        new_enquiry = Enquiry(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        db.session.add(new_enquiry)
        db.session.commit()

        # NOTIFYING THE ADMIN
        notify(
            f"""Hey, you've received a new enquiry on coderadi.in!
Name: {name}
Email: {email}
Subject: {subject}
Message: {message}
"""
        )

        # GETTING THE PREVIOUS URL TO RETURN THE USER TO
        from_url = request.referrer
        if (not from_url):
            from_url = request.url

        # RETURNING RESPONSE TO USER
        flash("Your enquiry is submitted, we'll reply within 24 hours.", "check_circle")
        return redirect(from_url)
    
# & REPORT PAGE (ERROR REPORTING)
@router.route('/report/', methods=['POST'])
def report_error():
    # GETTING FORM DATA
    error_type = request.files.get('error-type')
    page_url = request.form.get('page-url')
    email = request.form.get('email')
    message = request.form.get('message')

    # CREATING NEW DB ROW
    new_error = ErrorReport(
        error_type=error_type,
        page_url=page_url,
        email=email,
        message=message
    )

    # SAVING ROW IN DB
    db.session.add(new_error)
    db.session.commit()

    # NOTIFYING THE ADMIN
    notify("Hey, you've received a new error report on coderadi.in!")

    # RETURNING RESPONSE TO USER
    flash("Your report has been submitted. We'll fix that as soon as possible.", "check_circle")
    return redirect(url_for('router.home'))

# & SITEMAP
@router.route('/sitemap.xml')
def send_sitemap():
    return send_file('sitemap.xml')