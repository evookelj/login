#!/usr/bin/python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/login/")
def login():
	#print request.headers
	return render_template("dn.html");

@app.route("/authenticate/", methods=['POST'])
def auth():
        theVerdict = "a failure"
        theUser = ""
        if (request.form['user'] == "emma" and request.form['pass'] == "helloWorld"):
                theVerdict = "successful"
                theUser = request.form['user']
        return render_template("auth.html", verdict=theVerdict, user=theUser)

if __name__ == ("__main__"):
	app.debug = True
	app.run()
