"""Working With HTTP Verb Get and Post"""
## get means we are directly heating the url and we are getting it
## post means searching something and getting info from related search
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Hello I am Vaibhav</H1></html>"

@app.route("/index", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/form", methods=['GET','POST'])
def form():
    if request.method=='POST':
        name = request.form['name']
        return f"Hello {name}!"
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)