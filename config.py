from flask.ext.bower import Bower
from flask_sqlalchemy import SQLAlchemy
from elasticsearch import Elasticsearch

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://roman:12345@localhost/globe_soft'

es=Elasticsearch()

def configure(app):
	# config sqlalchemy
	global db

	app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
	db = SQLAlchemy(app)
	
	# importing and registering blueprints
	from dashboard.views import blueprint as dashboard_blueprint
	app.register_blueprint(dashboard_blueprint, url_prefix='/api')

	# config bower
	app.config['BOWER_COMPONENTS_ROOT'] = 'bower_components'
	Bower(app)
