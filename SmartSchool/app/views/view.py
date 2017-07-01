from app import app

@app.route('/api/school/query')
def getSchools():
    return '<h1>Hello World</h1>'
