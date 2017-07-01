from app import db

class School(db.Model):
    __tablename__ = "school"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True)
    email = db.Column(db.String(120), index = True, unique = True)
    phone = db.Column(db.String(120), index = True, unique = True)
    parent_id = db.Column(db.Integer, db.ForeignKey('school.id'))
    parent = db.relationship('school',
                            backref = 'school',
                            lazy = 'dynamic')
    user = db.relationship('User',
                            backref = 'subject',
                            lazy = 'dynamic')
    def __repr__(self):
        return '<School %r>' % (self.name)
