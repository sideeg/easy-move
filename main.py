
from flask import Flask, redirect, url_for, request, render_template
import flaskext_compat
flaskext_compat.activate()
from flask.ext import foo

app = Flask(__name__)

@app.route('/')
def landing_page():
   return render_template('hello.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return render_template('login.html')
   else:
      user = request.args.get('nm')
      return render_template('login.html')

@app.route('/register',methods = ['POST', 'GET'])
def register():
   if request.method == 'POST':
      #user = request.form['nm']
      return render_template('register.html')
   else:
      #user = request.args.get('nm')
      return render_template('register.html')


if __name__ == '__main__':
   app.run('0.0.0.0',5000,True)
