from . import db
#Classes here are for Object Relational Mapping

class User(db.Model):
    __tablename__ = 'users'
    username = db.Column(db.String(30), primary_key =True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    email = db.Column(db.String(50))
    password_ = db.Column(db.String(80))

    def __repr__(self):
        return '<User %r>' % self.username
