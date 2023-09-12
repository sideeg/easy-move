from flask import Flask, redirect, url_for, request, render_template
from simple_geoip import GeoIP
from flask import jsonify
import sqlite3
app = Flask(__name__)

#route to the db file
db_file = "/home/ubuntu/easy_move/db/easy_move.db"
#prepare the geoip key
geoip = GeoIP("at_1XijkKLvn8aL4z8c7SKM2EdL0UR6E");
#the main route 
@app.route('/')
def landing_page():
        return render_template("index.html")

#the login routes for get and post
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      return render_template('home.html')
   else:
      return render_template('login.html')

#the register route for the post and get
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

#the main page which have all the feature

@app.route('/home')
def home():
     return render_template('home.html')

#get the user cruunt location
@app.route('/get_location')
def get_location():
      
    try:
       data = geoip.lookup(str(request.remote_addr)) # Replace this with your public IP
    except ConnectionError:
       # If you get here, it means you were unable to reach the geoipify
       # service, most likely because of a network error on your end.
       return 'ConnectionError'
       #except ServiceError:
       # If you get here, it means geoipify is having issues, so the request
       # couldn't be completed 
       #return 'ServiceError'
    except:
       # Something else happened (non-geoipify) related. Maybe you hit CTRL-C
       # while the program was running, the kernel is killing your process, or
       # something else all together.
       return 'sonting went wrong'
    return data
if __name__ == '__main__':
   app.run('0.0.0.0',5000,True)
