from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# Basic Flask Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'

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