from app import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True)
    email = db.Column(db.String(120), index = True, unique = True)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'))
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'))
    def __repr__(self):
        return '<User %r>' % (self.name)
