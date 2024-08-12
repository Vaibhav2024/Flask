### Building URL Dynamically
### Variable Rule
### Jinja2 templete engine
"""
{{ }} expression to print output in html
{%...%} condition, for loop
{#...#} this is for comment
"""
from flask import render_template, request, Flask
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


@app.route("/submit", methods=['GET','POST'])   # redirects to /submit route
def submit():
    if request.method=='POST':
        name = request.form['name']
        return f"Hello {name}!"
    return render_template('form.html')


# Variable Rule
#Dynamic URL
@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score > 50:
        res = "PASSED"
    else:
        res = "FAILED"

    return render_template('result.html', results=res)


@app.route('/successres/<int:score>')
def successres(score):
    res = ""
    if score > 50:
        res = "PASSED"
    else:
        res = "FAILED"

    exp = {'score': score, "res": res}
    return render_template('result1.html', results=exp)

# if condition
@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result.html', results=score)


if __name__ == "__main__":
    app.run(debug=True)