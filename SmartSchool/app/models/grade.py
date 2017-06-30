from app import db

class Grade(db.Model):
    __tablename__ = "grade"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True)
    def __repr__(self):
        return '<Class %r>' % (self.name)
