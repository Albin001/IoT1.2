from flask import *
import pyrebase
import time
app=Flask(__name__)
time.sleep(2)
con1 = { "apiKey": "AIzaSyAGEs6gpTj68o8ZRkzIIi6EvpPjwRq3utw",
  "authDomain": "agri1-platform.firebaseapp.com",
  "databaseURL": "https://agri1-platform-default-rtdb.firebaseio.com",
  "projectId": "agri1-platform",
  "storageBucket": "agri1-platform.appspot.com",
  "messagingSenderId": "984064207409",
  "appId": "1:984064207409:web:1b37f3d82673bd07cdc310",
  "measurementId": "G-EF5CLPM1P7" }
firebase=pyrebase.initialize_app(con1)
db=firebase.database()
def fg2():
    a7 = db.child('data').get()
    a8 = a7.val()
    return  int(a8)
def fg():
    a2 = db.child('data2').get()
    a1=a2.val()
    return  float(a1)
def fg1():
    a3 = db.child('data3').get()
    a4=a3.val()
    return  float(a4)
@app.route('/')
def n2():
    return render_template('login.html')
@app.route('/menu')
def sw1():
    return render_template('user.html')
@app.route('/check')
def check():
    return  render_template('message.html')
@app.route('/message1/<a>/<b>')
def m2(a,b):
    return "Your username {} and Password {}".format(a,b)
@app.route('/log',methods=['POST','GET'])
def n3():
    a1="albin"
    a2="123"
    if request.method=='POST':
        user = request.form['yt']
        pass1 = request.form['yt1']
        if(a1==user and a2==pass1):

             return render_template('user.html')
        else:
            return redirect(url_for('check'))
    else:
        user = request.args.get('yt')
        pass1 = request.args.get('yt1')
        return redirect(url_for('message1',a=user,b=pass1 ))

@app.route('/dash')
def d2():
    per1 = fg()
    per2 = fg1()
    per3 = fg2()
    return render_template('dash.html',n3=per3,n4=per1,n5=per2)
@app.route('/set')
def s1():
    return render_template('settings.html')
@app.route('/login')
def log():
    return render_template('login.html')
@app.route('/rt/<name>/<name1>/<name2>')
def success(name,name1,name2):
   return " Temperature {} , Moisture {} and Water {} ".format(name,name1,name2)
@app.route('/process',methods=['POST','GET'])
def p2():
   if request.method == 'POST':
      user = request.form['nm']
      user1 = request.form['nm1']
      user2 = request.form['nm2']
      db.child('data1').set(user)
      return redirect(url_for('success',name = user,name1=user1,name2=user2))
   else:
      user = request.args.get('nm')
      user1 = request.form['nm1']
      user2 = request.form['nm2']
      return redirect(url_for('rt',name = user,name1=user1,name2=user2))
if(__name__=='__main__'):
    app.run(debug=True)