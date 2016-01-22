from flask import Blueprint

from flask import *
from models import Vacancy
from helpers import to_json, elasticsearch_like

blueprint = Blueprint('dashboard', __name__)

@blueprint.route('/list')
def get_list():
	args = request.args
	page = 1 if 'page' not in args else int(args['page'])
	limit = 10 if 'limit' not in args else int(args['limit'])
	filters = {}
	if 'source' in args:
		filters['source'] = args['source']

	if 'like' in args:

		ids = elasticsearch_like(args['like'])
		query = Vacancy.query.filter_by(**filters).filter(Vacancy.id.in_(ids)).slice((page-1)*limit, page*limit)
		amount = len(Vacancy.query.filter_by(**filters).filter(Vacancy.id.in_(ids)).all())
	else:
		query = Vacancy.query.filter_by(**filters).slice((page-1)*limit, page*limit)
		amount = len(Vacancy.query.filter_by(**filters).all())

	pages_total = round(amount/limit)
	
	if page <=5:
		last_page=10 if pages_total>10 else pages_total
		first_page=1
	elif pages_total - page <=5:
		first_page = pages_total-10 if pages_total>10 else 1
		last_page = pages_total
	else :
		last_page = page+5
		first_page = page-4

	return jsonify(**{"data":[to_json(q)['fields'] for q in query.all()], 'current_page':page,'first_page': first_page, 'last_page':last_page})

