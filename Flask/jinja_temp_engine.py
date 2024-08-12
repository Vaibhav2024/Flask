### Building URL Dynamically
### Variable Rule
### Jinja2 templete engine
"""
{{ }} expression to print output in html
{%...%} condition, for loop
{#...#} this is for comment
"""
from flask import render_template, request, Flask, redirect, url_for
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


@app.route("/submit", methods=['GET', 'POST'])
def submit():
    total_score = 0
    if request.method == "POST":
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['data_science'])
    else:
        return render_template('getresult.html')
    
    total_score = (science + maths + c + datascience)/4
    return redirect(url_for('successres', score=total_score))

if __name__ == "__main__":
    app.run(debug=True)