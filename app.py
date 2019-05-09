from flask import Flask, render_template, redirect, url_for, request, session, flash, g

import sqlite3

from functools import wraps


#falask object
app = Flask(__name__)
app.secret_key="vishal"
app.database="sample.db"


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
#url
@app.route('/')
@login_required

#function
def home():
	# return "hello, world"
    g.db = connect_db()
    cur = g.db.execute('select * from posts')
    posts = [dict(title = rows[0], desc = rows[1]) for rows in cur.fetchall()]
    g.db.close()
    return render_template('index.html', posts=posts)


@app.route('/welcome')
#function
def welcome():
	return render_template("welcome.html")

@app.route('/login', methods=['GET','POST'])
def login():
	error =None;
	if request.method =='POST':
		if request.form['username']!='admin' or request.form['password']!='admin':
			error = 'Invalid username or password'
		else:
			session['logged_in'] = True
			flash('you logged in')
			return redirect(url_for('home'))
	return render_template("login.html",error=error)

@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in',None)
	flash('you were just logged out')
	return redirect(url_for('welcome'))


def connect_db():
    return sqlite3.connect(app.database)

if __name__== '__main__':
	app.run(debug=True)
