from database import db

class Visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    epitet = db.Column(db.String(120), unique=False)

    def __init__(self, username, epitet):
        self.username = username
        self.epitet = epitet

    def __repr__(self):
        return '<Visitor %r>' % self.username