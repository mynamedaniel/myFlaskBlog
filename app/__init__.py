from flask import Flask
from config import config
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail, Message
import os

#create extensions instance
bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
mail = Mail()
basedir = os.path.abspath(os.path.dirname(__file__))

def create_app(config_name):
	#create Flask app
	app = Flask(__name__)

	#initiate configuration
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	bootstrap.init_app(app)
	moment.init_app(app)
	db.init_app(app)
	mail.init_app(app)

	#register blueprint
	from main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	return app

def send_mail(to, subject, template, **kwargs):
	msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject, sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
	msg.body = 'test body'
	msg.html = '<h1>Test</h1> body'
	mail.send(msg)