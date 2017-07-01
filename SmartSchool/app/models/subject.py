from app import db

class Subject(db.Model):
    __tablename__ = "subject"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True)
    subject = db.relationship('Subject',
                                backref = 'user',
                                lazy = 'dynamic')
    def __repr__(self):
        return '<Class %r>' % (self.name)
