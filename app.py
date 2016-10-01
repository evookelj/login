#!/usr/bin/python
from flask import Flask, render_template, request
from hashlib import sha1
from utils import processForms

app = Flask(__name__)

@app.route("/")
@app.route("/login/")
def home():
        processForms.loadDict()
        return render_template("dn.html")

#WITHOUT hash rn
@app.route("/authenticate/", methods=['POST'])
def auth():
        retAuth = processForms.authenticate(request.form['user'], request.form['pass'])
        return render_template("auth.html", verdict=retAuth[0], reason=retAuth[1])

@app.route("/register/", methods=['POST'])
def reg():
        return render_template("dn.html", errorMsg=processForms.register(request.form['newUser'],request.form['newPass']))

if __name__ == ("__main__"):
	app.debug = True
	app.run()
