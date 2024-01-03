from flask import Flask, render_template

# Basic Flask Instance
app = Flask(__name__)

# Route Decorator - used to redirect to a webpage
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/user/<name>')

def user(name):
    return render_template('user.html', user_name=name)

# Custom Error Page - 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404