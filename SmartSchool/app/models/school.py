from app import db

class School(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True)
    email = db.Column(db.String(120), index = True, unique = True)
    phone = db.Column(db.String(120), index = True, unique = True)
    def __repr__(self):
        return '<School %r>' % (self.name)