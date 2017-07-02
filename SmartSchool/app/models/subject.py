from app import db

class Subject(db.Model):
    __tablename__ = "subject"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True)

    def __repr__(self):
        return '<Subject %r>' % (self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }
