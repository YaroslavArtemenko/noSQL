from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from flask import Flask

app = Flask(__name__)
# подключение
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Trouble228@localhost/LABA2'
# связь
db = SQLAlchemy(app)


app.secret_key = 'development key'

class Contest(db.Model):
    tablename = 'contest'
    contest_name = db.Column(db.String(20), primary_key=True)
    event_name = db.Column(db.String(20), db.ForeignKey('event.event_name'))


class People(db.Model):
    tablename = 'People'
    people_email = db.Column(db.String(20), primary_key=True)
    people_name = db.Column(db.String(20))
    people_phone = db.Column(db.String(20))
    people_birthday = db.Column(db.Date)

    people_event = db.relationship('Event')


class association(db.Model):
    __tablename__ = 'associate_table'
    left_name = db.Column(db.String(20), db.ForeignKey('event.event_name'), primary_key=True)
    right_name = db.Column(db.String(20), db.ForeignKey('place.place_name'), primary_key=True)


class Event(db.Model):
    __tablename__ = 'event'
    event_name = db.Column(db.String(20), primary_key=True)
    people_email = db.Column(db.String(20), db.ForeignKey('people.people_email'))
    event_date = db.Column(db.Date)

    place_name_fk = db.relationship("Place", secondary='associate_table')
    event_contest = db.relationship('Contest')


class Place(db.Model):
    __tablename__ = 'place'
    place_name = db.Column(db.String(20), primary_key=True)
    place_adress = db.Column(db.String(100))

    event_name_fk = db.relationship("Event", secondary='associate_table')


# создание всех таблиц
db.create_all()