## Create a simple flask applicatio

from flask import Flask,redirect,url_for


## create the flask app
app=Flask(__name__)

@app.route('/')
def home():
    return "<h2>Hello, World!<h2>"

@app.route('/welcome')
def welcome():
    return "Welcome to the Flask Tutorial"
    
@app.route('/index')
def index():
    return "Welcome to the index page"


    

if __name__=="__main__":
    app.run(debug=True)

