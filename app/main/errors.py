from . import main

@main.app_errorhandler(404)
def page_not_found(e):
	return '<h1>Page Not Found!</h1>' 