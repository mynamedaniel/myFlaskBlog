import os
from app import create_app, db
from app.models import Role, User
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)
app.config['MAIL_SERVER'] = 'smtp.googlemail.com' 
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

def make_shell_context():
	return dict(app=app, db=db, User=User, Role=Role)

if __name__ == '__main__':
	manager.add_command('shell', Shell(make_context=make_shell_context))
	manager.add_command('db', MigrateCommand)
	manager.run()