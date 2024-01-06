from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# Basic Flask Instance
app = Flask(__name__)

# DB
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

app.config['SECRET_KEY'] = 'key'

# Initializing the DB
db = SQLAlchemy(app)

# DB Model

# Event Post Model
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    details = db.Column(db.Text)
    location = db.Column(db.String(255))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    slug = db.Column(db.String(255))
    


# Route Decorator - used to redirect to a webpage
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/user/<name>')

def user(name):
    return render_template('user.html', user_name=name)

class eventForm(FlaskForm):
    eventName = StringField("Name of the Event  ", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/event', methods=['GET', 'POST'])
def event():
    eventName = None
    form = eventForm()
    if form.validate_on_submit():
        
        flash("Event Added Successfully") # we are validating the form gets submitted here
        eventName = form.eventName.data
        form.eventName.data = ''
    
    return render_template('event.html',
                           eventName = eventName,
                           form = form)

# Form Class

# Custom Error Page - 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404