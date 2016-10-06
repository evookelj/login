#!/usr/bin/python
from flask import Flask, render_template, request, url_for, session
from hashlib import sha1
from utils import processForms

app = Flask(__name__)
app.secret_key = 'heyllo'

@app.route("/")
def home():
        processForms.loadDict()
        if (len(session.keys()) == 0):
                return redirect( url_for("login"))
        else:
                return render_template("home.html", user = session['User'])

@app.route("/login/")
def login():
        #redirect( url_for(auth) ) will redirect to correct URL for fxn auth()
        if (len(session.keys()) == 0):
                return render_template("dn.html")
        else:
                return render_template("home.html", user=session["User"])

#WITHOUT hash rn
@app.route("/authenticate/", methods=['POST'])
def auth():
        retAuth = processForms.authenticate(request.form['user'], request.form['pass'])
        if (retAuth[0]):
                session["User"] = request.form['user']
                theVerdict = "a success!"
        else:
                theVerdict = "a failure"
        return render_template("auth.html", verdict=theVerdict, reason=retAuth[1])

@app.route("/register/", methods=['POST'])
def reg():
        return render_template("dn.html", errorMsg=processForms.register(request.form['newUser'],request.form['newPass']))

if __name__ == ("__main__"):
	app.debug = True
	app.run()
