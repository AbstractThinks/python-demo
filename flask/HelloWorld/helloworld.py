from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask_script import Manager
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand


app = Flask(__name__)
manager = Manager(app)
# app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:abcd,1234.@localhost:3306/flask'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:abcd,1234.@localhost:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app) #实例化
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

class User(db.Model):
    """定义数据模型"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello %s</h1>' % name

@app.route('/requestHeader')
def requestHeader():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

@app.route('/returnSatus')
def returnSatus():
    return '<h1>Bad Request<h1>', 400

@app.route('/set_cookie')
def response():
    resp = make_response('<h1>this document carries a cookie!</h1>')
    resp.set_cookie('answer', '42')
    return resp

@app.route('/redirect')
def returnRedirect():
    return redirect("http://www.baidu.com")

@app.route('/userabort/<name>')
def userabort(name):
    if name != 'jesse':
        abort(404)
    return '<h1>Hello, %s</h1>'%name


# template
@app.route('/render/html')
def renderHtml():
    return render_template('index.html')

@app.route('/render/user/<name>')
def renderUser(name):
    return render_template('user.html', name=name)


# sql

@app.route('/adduser')
def add_user():
    user1 = User('jesse', 'jesse@qq.com')
    user2 = User('alvin', 'alvin@qq.com')
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
    db.session.close()
    return "<p>add succssfully!</p>"

@app.route('/getuser')
def get_user():
    users = User.query.all()
    return "%s" %str(users)

@app.route('/updateuser')
def update_user():
    jesse = User.query.filter_by(username='jesse').first()
    jesse.email = "admin@hotmail.com"
    db.session.add(jesse)
    db.session.commit()
    db.session.close()
    # admin = User.query.filter_by(username='jesse').first()
    return "更新成功"

@app.route('/deleteuser')
def delete_user():
    alvin = User.query.filter_by(username='alvin').first()
    db.session.delete(alvin)
    db.session.commit()
    db.session.close()
    return '删除成功'

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    manager.run()

    # app.run(debug = True)
