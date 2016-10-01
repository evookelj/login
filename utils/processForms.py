#!/usr/bin/python
from hashlib import sha1

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

def authenticate(user,password):
    theVerdict = "a failure."
    theReason=""
    passHash = sha1(password).hexdigest()
    if (user in userInfo.keys()):
        if (passHash == userInfo[user]):
            theVerdict = "a success!"
        else:
            theReason = "Incorrect password entered."
    else:
        theReason = "Username does not exist."
    return [theVerdict,theReason]

def register(user,password):
    theError = ""
    passHash = sha1(password).hexdigest()
    if (user in userInfo.keys()):
        print "route1"
        theError = "This username is already registered."
    else:
        print "route2"
        if ("," in user):
            theError = "Username has invalid character (a comma)."
        else:
            with open('data/userPass.csv','a') as csv:
                csv.write(user + "," + passHash + "\n")
                theError = "Your account was successfully created!"
                userInfo[user] = passHash
    return theError
