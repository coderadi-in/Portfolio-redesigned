'''coderadi &bull; API router for the site'''

# ? IMPORTING LIBRARIES
from flask import Blueprint, render_template, redirect, url_for, flash, request
from plugins.models import *
from plugins import db
import os

# ! INITIALIZING API ROUTER
api = Blueprint('api', __name__, url_prefix='/api')

# * FUNCTION TO CHECK ADMIN PASS
def check_admin_pass():
    admin_pass = request.headers.get('admin_pass')
    protocol_pass = os.getenv('ADMIN_PASS')

    return (admin_pass == protocol_pass)

# >>> I DB OPERATIONS [START]
# >>> II PROJECTS OPERATIONS [START]
# & API ROUTE TO SAVE NEW PROJECT
@api.route('/db/projects/new', methods=['POST'])
def new_project_logic():
    # | CHECKING ADMIN PASS
    check_admin_pass()

    # | GETTING DATA FROM REQUEST
    data = request.json
    title = data.get('title')
    desc = data.get('desc')
    cover = data.get('cover')
    url = data.get('url')

    # | VALIDATING DATA
    if (not title) or (not cover) or (not url):
        return {'status': 'error', 'message': 'Missing required fields.'}, 400
    
    # | SAVING DATA TO DATABASE
    new_project = Project(
        title=title,
        desc=desc,
        cover=cover,
        url=url
    )

    db.session.add(new_project)
    db.session.commit()

    return {'status': 'success', 'message': 'New project added successfully.'}, 201

# & API ROUTE TO GET ALL PROJECTS
@api.route('/db/projects/all', methods=['GET'])
def get_all_projects():
    projects = Project.query.all()
    projects_list = []

    for project in projects:
        projects_list.append({
            'id': project.id,
            'title': project.title,
            'desc': project.desc,
            'cover': project.cover,
            'url': project.url
        })

    return {'status': 'success', 'projects': projects_list}, 200

# & API ROUTE TO DELETE A PROJECT
@api.route('/db/projects/delete/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    # | CHECKING ADMIN PASS
    check_admin_pass()

    # | FETCHING PROJECT
    project = Project.query.get(project_id)

    if (not project):
        return {'status': 'error', 'message': 'Project not found.'}, 404

    # | DELETING PROJECT
    db.session.delete(project)
    db.session.commit()

    return {'status': 'success', 'message': 'Project deleted successfully.'}, 200

# & API ROUTE TO UPDATE A PROJECT
@api.route('/db/projects/update/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    # | CHECKING ADMIN PASS
    check_admin_pass()

    # | FETCHING PROJECT
    project = Project.query.get(project_id)

    if (not project):
        return {'status': 'error', 'message': 'Project not found.'}, 404

    # | GETTING DATA FROM REQUEST
    data = request.json
    title = data.get('title')
    desc = data.get('desc')
    cover = data.get('cover')
    url = data.get('url')

    # | UPDATING FIELDS IF PROVIDED
    if (title): project.title = title
    if (desc): project.desc = desc
    if (cover): project.cover = cover
    if (url): project.url = url
    db.session.commit()

    return {'status': 'success', 'message': 'Project updated successfully.'}, 200
# >>> II PROJECTS OPERATIONS [END]

# >>> II ENQUIRIES OPERATIONS [START]
# & API ROUTE TO GET ALL ENQUIRIES
@api.route('/db/enquiries/all', methods=['GET'])
def get_all_enquiries():
    # | CHECKING ADMIN PASS
    check_admin_pass()

    # | FETCHING ENQUIRIES
    enquiries = Enquiry.query.all()
    enquiries_list = []

    # | FORMATTING ENQUIRIES
    for enquiry in enquiries:
        enquiries_list.append({
            'id': enquiry.id,
            'name': enquiry.name,
            'email': enquiry.email,
            'message': enquiry.message,
        })

    return {'status': 'success', 'enquiries': enquiries_list}, 200

# & API ROUTE TO DELETE AN ENQUIRY
@api.route('/db/enquiries/delete/<int:enquiry_id>', methods=['DELETE'])
def delete_enquiry(enquiry_id):
    # | CHECKING ADMIN PASS
    check_admin_pass()

    # | FETCHING ENQUIRY
    enquiry = Enquiry.query.get(enquiry_id)

    if (not enquiry):
        return {'status': 'error', 'message': 'Enquiry not found.'}, 404

    # | DELETING ENQUIRY
    db.session.delete(enquiry)
    db.session.commit()

    return {'status': 'success', 'message': 'Enquiry deleted successfully.'}, 200
# >>> II ENQUIRIES OPERATIONS [END]

# >>> II ERROR OPERATIONS [START]
# & API ROUTE TO GET ALL ERROR REPORTS
@api.route('/db/errors-report/all', methods=['GET'])
def get_all_reports():
    # | CHECKING ADMIN PASS
    check_admin_pass()

    # | FETCHING ERRORS
    errors = ErrorReport.query.all()
    errors_list = []

    # | FORMATTING ERRORS
    for error in errors:
        errors_list.append({
            'id': error.id,
            'type': error.error_type,
            'page-url': error.page_url,
            'email': error.email,
            'message': error.message,
        })

    return {'status': 'success', 'errors': errors_list}, 200

# & API ROUTE TO DELETE AN ERROR REPORT
@api.route('/db/errors-report/delete/<int:report_id>', methods=['DELETE'])
def delete_report(report_id):
    # | CHECKING ADMIN PASS
    check_admin_pass()

    # | FETCHING ERROR REPORT
    report = ErrorReport.query.get(report_id)

    if (not report_id):
        return {'status': 'error', 'message': 'Report not found.'}, 404

    # | DELETING REPORT
    db.session.delete(report)
    db.session.commit()

    return {'status': 'success', 'message': 'Report deleted successfully.'}, 200
# >>> II ERROR OPERATIONS [END]
# >>> I DB OPERATIONS [END]