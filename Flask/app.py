"""Basic Skeleton of Flask"""
from flask import Flask
# it creates instance of flask class, and it will be your WSGI application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to This Best Flask"

@app.route("/index")
def welccome_index():
    return "Welcome to index page"


if __name__ == "__main__":
    app.run(debug=True)