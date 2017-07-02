import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:abcd,1234.@localhost:3306/flask"
SQLALCHEMY_TRACK_MODIFICATIONS = True
