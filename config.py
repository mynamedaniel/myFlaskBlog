import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'fuckdaohaode12-'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'devData.sqlite')
	FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
	FLASK_MAIL_SENDER = 'Flasky Admin <mynamedaniel@126.com>'

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'testData.sqlite')

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'productionData.sqlite')

config = {
	'development' : DevelopmentConfig,
	'testing' : TestingConfig,
	'production' : ProductionConfig,
	'default' : DevelopmentConfig
}