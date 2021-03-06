# -*- coding: utf-8 -*-
import random

from flask import Flask,render_template, request, jsonify

from database import db
from models import Visitor


app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)

with app.app_context():
    db.create_all()

epithets = [u'великий', u"ужасный", u"всемогущий", u"владыка", u"великодушный", u"диктатор", u"тиран"]

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/form', methods=['POST'])
def execute():
    # There could be wtforms
    name = request.form['name']
    visitor = Visitor.query.filter_by(username=name).first()
    come_back = False
    if not visitor:
        epithet = random.choice(epithets)
        visitor = Visitor(name, epithet)
        db.session.add(visitor)
        db.session.commit()
    else:
        epithet = visitor.epithet
        come_back = True
    return jsonify(name=name, epitet=epithet, come_back=come_back)

if __name__ == '__main__':
    app.run()
