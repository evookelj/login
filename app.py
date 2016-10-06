#!/usr/bin/python
from flask import Flask, render_template, request, url_for, session, redirect
from hashlib import sha1
from utils import processForms
from os import urandom

app = Flask(__name__)
app.secret_key = urandom(32)

@app.route("/")
def home():
        processForms.loadDict()
        print "LEN: " + str(len(session.keys()))
        if (len(session.keys()) == 0):
                return redirect( url_for("login"))
        else: #if account exists, go to real home
                return render_template("home.html", user = session['User'])

@app.route("/login/")
def login():
        return render_template("dn.html")

#WITHOUT hash rn
@app.route("/authenticate/", methods=['POST'])
def auth():
        retAuth = processForms.authenticate(request.form['user'], request.form['pass'])
        if (retAuth[0]):
                session["User"] = request.form['user']
                return redirect( url_for("home"))
        else:
                theVerdict = "a failure"
        return render_template("dn.html", errorMsg=retAuth[1])

@app.route("/register/", methods=['POST'])
def reg():
        return render_template("dn.html", errorMsg=processForms.register(request.form['newUser'],request.form['newPass']))

if __name__ == ("__main__"):
	app.debug = True
	app.run()
