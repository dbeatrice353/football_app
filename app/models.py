from . import db
#Classes here are for Object Relational Mapping

class User(db.Model):
    __tablename__ = 'users'
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    email = db.Column(db.String(50), primary_key = True)
    password_ = db.Column(db.String(80))

    def __repr__(self):
        return '<User %r>' % self.email
