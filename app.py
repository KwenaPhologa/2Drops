from flask import Flask, render_template,request, redirect, session

app = Flask(__name__)
app.secret_key = "PhologaTestMe"

@app.route("/")
def index():
    return render_template("2Drops.html")

@app.route('/submit',methods=["GET","POST"])
def submit():
    username=request.form.get("username")
    return render_template('greet.html',person=username)

@app.route('/login',methods=["POST","GET"])
def login():
    correct_username = "kwenaphologa"
    correct_password ="password123"
    givenuser = request.form.get("username")
    givenpass = request.form.get("password")

    print(givenuser)
    print(givenpass)
    if (givenuser == correct_username and givenpass == correct_password):
        session["logged"] = True
        return redirect("/dashboard")
    else:
        return redirect('/login')

@app.route('/index')
def home():
    if session.get("logged"):
        return render_template("index.html")
    else:
        return redirect('/login')
@app.route('/logout', methods=["GET","POST"])
def logout():
    session["logged"] = False
    return redirect('/login')

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")