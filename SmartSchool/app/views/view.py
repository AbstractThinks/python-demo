from app import app
from datetime import datetime
from app.models import user, subject
from app import db
from flask_json import JsonError, json_response, as_json
from flask import request


@app.route("/")
def getIndex():
    return "<h1>Hello World</h1>"

@app.route('/api/school/query')
def getSchools():
    userlist = user.User.query.all()
    return json_response(userlist)

@app.route('/api/subject/list')
def getSubjects():
    subjectlist = []
    result = subject.Subject.query.all()
    for o in result:
        subjectlist.append(o.to_json())
    return json_response(data = subjectlist)

@app.route('/api/subject/query')
def getSubject():
    param_id = request.args.get('id')
    result = subject.Subject.query.get(param_id)
    return json_response(data = result.to_json())
