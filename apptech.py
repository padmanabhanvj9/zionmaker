'''

This is the master file for all the Web services
related to Doctor Appt application

'''

from flask import Flask,request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
   return "Hello World!"
@app.route("/user/<data>")
def helloName(data):
   return data

if __name__ == "__main__":
   app.run(debug=True)
  #app.run(host="192.168.1.35",port=5000)
