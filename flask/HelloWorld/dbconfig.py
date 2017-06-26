# sql
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:abcd,1234.@localhost:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app) #实例化
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

class User(db.Model):
    """定义数据模型"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    migrate = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

if __name__ == '__main__':
    # db.drop_all()
    db.create_all()
    manager.run()


# 1. python dbconfig.py db init  创建迁移仓库  这个命令会创建 migrations 文件夹，所有迁移脚本都存放其中
# 2. python dbconfig.py db migrate -m "initial migration"  自动创建迁移脚本
# 3. python dbconfig.py db upgrade  更新数据库
