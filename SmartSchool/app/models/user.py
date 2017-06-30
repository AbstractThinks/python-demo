from app import db


school_user = db.Table('school_user', db.Model.metadata,
    db.Column('school_id', db.Integer, db.ForeignKey('school.id')),
    db.Column('user_id',db.Integer, db.ForeignKey('user.id'))
)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index = True)
    email = db.Column(db.String(120), index = True, unique = True)
    school_id = db.relationship('School',
                              secondary = school_user, #关联表,只需要在一个表建立关系,sqlalchemy会负责处理好另一个表
                              backref = db.backref('users',lazy='dynamic'),
                              lazy = 'dynamic')
    subject = db.relationship('Subject',
                                backref = 'user',
                                lazy = 'dynamic')
    def __repr__(self):
        return '<User %r>' % (self.name)
