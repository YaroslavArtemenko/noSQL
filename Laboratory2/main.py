from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from dao.orm.populate import *

from Forms.UserForm import UserForm
from Forms.ContestForm import ContestForm
from Forms.EventForm import EventForm
from Forms.PlaceForm import PlaceForm
from Forms.PeopleFormEdit import PeopleFormEdit
from Forms.EventFormEdit import EventFormEdit
from Forms.ContestFormEdit import ContestFormEdit
from Forms.PlaceFormEdit import PlaceFormEdit

from sqlalchemy.sql import func
import plotly
import plotly.graph_objs as go

import json

from Forms.UserForm import UserForm

app = Flask(__name__)
# подключение
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Trouble228@localhost/LABA2'
# связь
db = SQLAlchemy(app)


app.secret_key = 'development key'


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    query1 = (
        db.session.query(
            People.people_name,
            func.count(Event.event_name).label('event_name')
        ).join(Event, People.people_email == Event.people_email).
            group_by(People.people_name)
    ).all()

    print(query1)

    query2 = (
        db.session.query(
            Event.event_name,
            func.count(Contest.contest_name).label('contest_name')
        ).join(Contest, Event.event_name == Contest.event_name).
            group_by(Event.event_name)
    ).all()

    print(query2)

    people_name, event_name = zip(*query1)
    bar = go.Bar(
        x=people_name,
        y=event_name
    )

    event_name, contest_name = zip(*query2)
    pie = go.Pie(
        labels=event_name,
        values=contest_name
    )

    data = {
        "bar": [bar],
        "pie": [pie]
    }
    graphs_json = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', graphsJSON=graphs_json)

@app.route('/edit_people/<string:email>', methods=['GET', 'POST'])
def edit_people(email):
    form = PeopleFormEdit()
    result = db.session.query(People).filter(People.people_email == email).one()

    if request.method == 'GET':

        form.people_name.data = result.people_name
        form.people_email.data = result.people_email
        form.people_birthday.data = result.people_birthday
        form.people_phone.data = result.people_phone


        return render_template('edit_people.html', form=form, form_name=email)
    elif request.method == 'POST':

        result.people_name = form.people_name.data
        result.user_email = form.people_email.data
        result.people_birthday = form.people_birthday.data.strftime("%Y-%m-%d"),
        result.people_phone = form.people_phone.data

        db.session.commit()
        return redirect('/people')


@app.route('/edit_event/<string:name>', methods=['GET', 'POST'])
def edit_event(name):
    form = EventFormEdit()
    result = db.session.query(Event).filter(Event.event_name == name).one()

    if request.method == 'GET':

        form.event_name.data = result.event_name
        form.event_date.data = result.event_date


        return render_template('edit_event.html', form=form, form_name=name)
    elif request.method == 'POST':

        result.event_name = form.event_name.data
        result.event_date = form.event_date.data.strftime("%Y-%m-%d"),

        db.session.commit()
        return redirect('/event')



@app.route('/edit_contest/<string:name>', methods=['GET', 'POST'])
def edit_contest(name):
    form = ContestFormEdit()
    result = db.session.query(Contest).filter(Contest.contest_name == name).one()

    if request.method == 'GET':

        form.contest_name.data = result.contest_name


        return render_template('edit_contest.html', form=form, form_name='Edit Contest')
    elif request.method == 'POST':

        result.contest_name = form.contest_name.data

        db.session.commit()
        return redirect('/contest')


@app.route('/edit_place/<string:name>', methods=['GET', 'POST'])
def edit_place(name):
    form = PlaceFormEdit()
    result = db.session.query(Place).filter(Place.place_name == name).one()

    if request.method == 'GET':

        form.place_name.data = result.place_name
        form.place_adress.data = result.place_adress


        return render_template('edit_place.html', form=form, form_name='Edit Place')
    elif request.method == 'POST':

        result.place_name = form.place_name.data
        result.place_adress = form.place_adress.data

        db.session.commit()
        return redirect('/place')


@app.route('/create_people', methods=['POST', 'GET'])
def create_people():
    form = UserForm()

    if request.method == 'POST':
        new_people = People(
            people_name=form.people_name.data,
            people_birthday=form.people_birthday.data.strftime("%Y-%m-%d"),
            people_email=form.people_email.data,
            people_phone=form.people_phone.data,
        )
        db.session.add(new_people)
        db.session.commit()
        return redirect('/people')
    elif request.method == 'GET':
        return render_template('create_people.html', form=form)


@app.route('/delete_people/<string:email>', methods=['GET', 'POST'])
def delete_people(email):
    result = db.session.query(People).filter(People.people_email == email).one()

    db.session.delete(result)
    db.session.commit()

    return redirect('/people')



@app.route('/create_contest', methods=['POST', 'GET'])
def create_contest():
    form = ContestForm()

    if request.method == 'POST':
        new_contest = Contest(
            contest_name=form.contest_name.data,
        )
        db.session.add(new_contest)
        db.session.commit()
        return redirect('/contest')
    elif request.method == 'GET':
        return render_template('create_contest.html', form=form)


@app.route('/delete_contest/<string:name>', methods=['GET', 'POST'])
def delete_contest(name):
    result = db.session.query(Contest).filter(Contest.contest_name == name).one()

    db.session.delete(result)
    db.session.commit()

    return redirect('/contest')


@app.route('/create_event', methods=['POST', 'GET'])
def create_event():
    form = EventForm()

    if request.method == 'POST':
        new_event = Event(
            event_name=form.event_name.data,
            event_date=form.event_date.data.strftime("%Y-%m-%d")
        )
        db.session.add(new_event)
        db.session.commit()
        return redirect('/event')
    elif request.method == 'GET':
        return render_template('create_event.html', form=form)


@app.route('/delete_event/<string:name>', methods=['GET', 'POST'])
def delete_event(name):
    result = db.session.query(Event).filter(Event.event_name == name).one()

    db.session.delete(result)
    db.session.commit()

    return redirect('/event')


@app.route('/create_place', methods=['POST', 'GET'])
def create_place():
    form = PlaceForm()

    if request.method == 'POST':
        new_place = Place(
            place_name=form.place_name.data,
            place_adress=form.place_adress.data
        )
        db.session.add(new_place)
        db.session.commit()
        return redirect('/place')
    elif request.method == 'GET':
        return render_template('create_place.html', form=form)


@app.route('/delete_place/<string:name>', methods=['GET', 'POST'])
def delete_place(name):
    result = db.session.query(Place).filter(Place.place_name == name).one()

    db.session.delete(result)
    db.session.commit()

    return redirect('/place')




@app.route('/', methods=['GET', 'POST'])
def root():

    return render_template('index.html')

@app.route('/people', methods=['GET'])
def all_peolpe():
    result = db.session.query(People).all()

    return render_template('all_people.html', result=result)


@app.route('/contest', methods=['GET'])
def all_contest():
    result = db.session.query(Contest).all()

    return render_template('all_contest.html', result=result)


@app.route('/event', methods=['GET'])
def all_event():
    result = db.session.query(Event).all()

    return render_template('all_event.html', result=result)


@app.route('/place', methods=['GET'])
def all_place():
    result = db.session.query(Place).all()

    return render_template('all_place.html', result=result)


if __name__ == "__main__":
    app.run()


