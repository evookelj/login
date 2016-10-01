#!/usr/bin/python
from flask import Flask, render_template, request

app = Flask(__name__)

userInfo = {}

@app.route("/")
@app.route("/login/")
def login():
        if (len(userInfo)==0):
                csv = open('data/userPass.csv').read().strip("\n")
                if "\n" in csv:
                        csv = csv.split("\n")
                        for row in csv:
                                row = row.split(",")
                                userInfo[row[0]] = row[1]
                else:
                        csv = csv.split(",")
                        userInfo[csv[0]] = csv[1]
	return render_template("dn.html", errorMsg = "")

@app.route("/authenticate/", methods=['POST'])
def auth():
        theVerdict = "a failure."
        theUser = ""
        theReason=""
        if (request.form['user'] in userInfo.keys()):
                if (request.form['pass'] == userInfo[request.form['user']]):
                        theVerdict = "a success!"
                else:
                        theReason = "Incorrect password entered."
        else:
                theReason = "Username does not exist."
        return render_template("auth.html", verdict=theVerdict, reason=theReason)

@app.route("/register/", methods=['POST'])
def reg():
        return render_template("dn.html", errorMsg="(Registration failed. Try again)")

if __name__ == ("__main__"):
	app.debug = True
	app.run()
