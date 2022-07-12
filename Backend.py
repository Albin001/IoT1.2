from flask import *
app=Flask(__name__)
@app.route('/')
def n2():
    return render_template('login.html')
@app.route('/menu')
def sw1():
    return render_template('user.html')
@app.route('/check')
def check():
    return "CHECK Your user name and Password"
@app.route('/log',methods=['POST','GET'])
def n3():
    a1="albin"
    a2="123"
    if(request.method=='POST'):
        user=request.form['yt']
        pass1=request.form['yt1']
        return render_template('user.html')
    else:
        pass
@app.route('/dash')
def d2():
    return render_template('dash.html')
@app.route('/set')
def s1():
    return render_template('settings.html')
@app.route('/login')
def log():
    return render_template('login.html')
@app.route('/rt/<n1>/<n2>/<n3>')
def f1(n1,n2,n3):
    return render_template('show.html',t1=n1,t2=n2,t3=n3)
@app.route('/process',methods=['POST','GET'])
def p1():
    if(request.method=='POST'):
        w1=request.form['number1']
        w2=request.form['number2']
        w3=request.form['number3']
        return redirect(url_for('rt',n1=w1,n2=w2,n3=w3))
    else:
        pass
if(__name__=='__main__'):
    app.run(debug=True)