from flask import Flask, render_template

# Basic Flask Instance
app = Flask(__name__)

# Route Decorator - used to redirect to a webpage
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/user/<name>')

def user(name):
    return "<h1>Hello {}</h1>".format(name)