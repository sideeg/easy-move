from flask import Flask, redirect, url_for, request, render_template
# import flaskext_compat
# flaskext_compat.activate()
# from flask.ext import foo
import sqlite3
app = Flask(__name__)

db_file = "/home/ubuntu/easy_move/db/easy_move.db"
@app.route('/')
def landing_page():
        #con = sql.connect("/home/ubuntu/easy_move/db/easy_move.db")
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute("select * from user")
        
        rows = cur.fetchall();
        
        conn.close()
        return render_template("index.html",rows = rows)

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      return request.form
      user = request.form['first_name']
       
      return render_template('login.html')
   else:
      
      return render_template('login.html')

@app.route('/register',methods = ['POST', 'GET'])
def register():
   if request.method == 'POST':
      try:
         first_name = 'dd' #request.form['first_name']
         last_name = 'qq' #request.form['last_name']
         email = 'aa' #request.form['email']
         
         c = sqlite3.connect(db_file)
         print(c)
         with sqlite3.connect(db_file) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO user  VALUES (?,?,?,?)",(first_name,last_name,email) )
            #return cur.lastrowid
            con.commit()
            return "Record successfully added"
      except:
         return cur.lastrowid
         con.rollback()
         return "error in insert operation"
      
      finally:
            #return render_template("home.html",msg = msg)
            con.close()
            return str(cur.lastrowid) 
            return redirect(url_for('landing_page'))
            #return "fine"
   else:
      #user = request.args.get('nm')
      return render_template('register.html')


if __name__ == '__main__':
   app.run('0.0.0.0',5000,True)
