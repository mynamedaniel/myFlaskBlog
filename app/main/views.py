from . import main
from flask import render_template, session, redirect, url_for, flash
from datetime import datetime
from forms import NameForm
from app.models import User
from app import db

@main.route('/', methods = ['GET','POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.name.data).first()
		if user is None:
			user = User(username=form.name.data)
			db.session.add(user)
			#db.session.commit()
			session['known'] = False
		else:
			session['known'] = True
		session['name'] = form.name.data
		form.name.data = ''
		return redirect('/')
	return render_template('index.html', current_time = datetime.utcnow(), form = form, name = session.get('name'), known = session.get('known', False))

@main.route('/user/<name>')
def user(name):
	return render_template('user.html', name = name)

@main.route('/life')
def life():
	return render_template('life.html')

@main.route('/programming')
def programming():
	return render_template('programming.html')