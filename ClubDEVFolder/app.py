from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Event(db.Model):
    #WIP
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    date = db.Column(db.DateTime)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    num_vol_required = db.Column(db.Integer)
    max_vol = db.Column(db.Integer)
    num_vol_registered = db.Column(db.Integer)
    status = db.Column(db.String(20))
    club_id = db.Column(db.Integer, db.ForeignKey('club.id'))

class Club(db.Model):
    #WIP 
    club_id = db.Column(db.Integer, primary_key=True)
    club_name = db.Column(db.String(80))
    volunteers = db.relationship('Volunteer', backref='club', lazy='dynamic')
    events = db.relationship('Event', backref='club', lazy='dynamic')
    # ... add other columns as needed

@app.route('/manage_events')
def events():
    events = Event.query.all()
    return render_template('events.html', events=events)

@app.route('/new_event', methods=['GET', 'POST'])
def new_event():
    form = NewEventForm() #NewEventForm should be a Flask Form class
    if form.validate_on_submit()::
    event = Event(
        name=form.name.data,
        date = form.date.data,
        start_time = form.start_time.data,
        end_time = form.end_time.data,
        num_vol_required = form.num_vol_required.data,
        max_vol = form.max_vol.data,
        num_vol_registered = 0,
        status = 'Pending Volunteers',
        # club_id = session['club_id']
        #event_id = get_new_event_id()

    )
    db.session.add(event)
    db.session.commit()
    flash('Event successfully created')
    return redirect(url_for('events'))
return render_template('new_event.html', form=form)
