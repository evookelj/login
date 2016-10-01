#!/usr/bin/python
from flask import Flask, render_template, request
from hashlib import sha1

app = Flask(__name__)

userInfo = {}

def loadDict():
        csv = open('data/userPass.csv').read().strip("\n")
        if (len(csv)==0):
                return
        if "\n" in csv: # more than one entry
                csv = csv.split("\n")
                for row in csv: 
                        row = row.split(",")
                        userInfo[row[0]] = row[1]
        else:
                csv = csv.split(",")
                userInfo[csv[0]] = csv[1]

@app.route("/")
@app.route("/login/")
def login():
        loadDict()
        return render_template("dn.html")

#WITHOUT hash rn
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
        theError = ""
        if (request.form['newUser'] in userInfo.keys()):
                print "route1"
                theError = "This username is already registered."
        else:
                print "route2"
                if ("," in request.form['newUser']):
                        theError = "Password has invalid character (a comma)."
                else:
                        with open('data/userPass.csv','a') as csv:
                                csv.write(request.form['newUser'] + "," + request.form['newPass'] + "\n")
                                theError = "Your account was successfully created!"
        return render_template("dn.html", errorMsg=theError)

if __name__ == ("__main__"):
	app.debug = True
	app.run()
