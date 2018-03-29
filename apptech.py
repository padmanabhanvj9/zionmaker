'''

This is the master file for all the Web services
related to Doctor Appt application

'''
import json
from flask import Flask,request, jsonify
from helloworld import pad

app = Flask(__name__)

@app.route("/")
def hello():
   return "Hello World!"
@app.route("/new")
def new():
   return pad(request)

if __name__ == "__main__":
   app.run(debug=True)
  #app.run(host="192.168.1.35",port=5000)
