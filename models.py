from database import db

class Visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    epithet = db.Column(db.String(120), unique=False)

    def __init__(self, username, epithet):
        self.username = username
        self.epithet = epithet

    def __repr__(self):
        return '<Visitor %r>' % self.username