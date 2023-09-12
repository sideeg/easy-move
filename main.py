from flask import Flask, redirect, url_for, request, render_template
# import flaskext_compat
# flaskext_compat.activate()
# from flask.ext import foo
import sqlite3
app = Flask(__name__)

db_file = "/home/ubuntu/easy_move/db/easy_move.db"
@app.route('/')
def landing_page():
        return render_template("index.html")

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      return render_template('home.html')
   else:
      return render_template('login.html')

@app.route('/register',methods = ['POST', 'GET'])
def register():
   if request.method == 'POST':
      return redirect(url_for('home'))
      
      try:
         first_name = request.form['first_name']
         last_name = request.form['last_name']
         email = request.form['email']
         
         con = sqlite3.connect(db_file)
         
         cur = con.cursor()
         cur.execute("INSERT INTO user  VALUES (?,?,?);",(first_name,last_name,email) )
         con.commit()
         msg =  "Record successfully added"
         return redirect(url_for('home'),msg=msg)
      except:
         con.rollback()
         
      finally:

            con.close()            
            return redirect(url_for('landing_page'))
           
   else:
      return render_template('register.html')

@app.route('/home')
def home():
     return render_template('home.html')
if __name__ == '__main__':
   app.run('0.0.0.0',5000,True)
