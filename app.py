#!/usr/bin/python

from flask import Flask, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    return "NO POST, THx"
  else :
    return "U GOT IT!!!"

if __name__ == "__main__":
  app.run(port=1025, debug=True)
  #app.run(port=1025)

