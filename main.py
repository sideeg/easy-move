
from flask import Flask, redirect, url_for, request, render_template
#import flaskext_compat
#flaskext_compat.activate()
#from flask.ext import foo
import sqlite3
app = Flask(__name__)

db_file = "/home/ubuntu/easy_move/db/easy_move.db"
@app.route('/')
def landing_page():
        #con = sql.connect("/home/ubuntu/easy_move/db/easy_move.db")
        conn = sqlite3.connect(db_file)
        #con.row_factory = sql.Row
        cur = conn.cursor()
        cur.execute("select * from user")

        rows = cur.fetchall();
        return rows 
        return render_template("hello.html",rows = rows)
	

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
      try:
         first_name = request.form['first_name']
         last_name = request.form['last_name']
         email = request.form['email']
         
         c = sqlite3.connect(db_file)
         print(c)
         with sqlite3.connect(db_file) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO user (first_name,last_name,email) VALUES (?,?,?,?)",(first_name,last_name,email) )
            
            con.commit()
            return "Record successfully added"
      except:
         con.rollback()
         return "error in insert operation"
      
            #finally:
            #return render_template("home.html",msg = msg)
            #con.close()
            #return redirect(url_for('landing_page'))
            #return "fine"
   else:
      #user = request.args.get('nm')
      return render_template('register.html')


if __name__ == '__main__':
   app.run('0.0.0.0',5000,True)
