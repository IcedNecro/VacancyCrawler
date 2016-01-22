import json
import requests

from config import es
def to_json(model):
    json = {}
    json['fields'] = {}
    json['pk'] = getattr(model, 'id')

    for col in model._sa_class_manager.mapper.mapped_table.columns:
        json['fields'][col.name] = getattr(model, col.name)

    return json

def elasticsearch_like(like_string):
	request_data = {
		'query': {
			"more_like_this": {
				"fields":['title', 'company_name'],
				'like_text': like_string,
				"min_doc_freq":1,
				"min_term_freq":1
			}
		}
	}
	response = es.search(index='vacancies', body=request_data)
	ids = map(lambda x: int(x['_id']) ,response['hits']['hits'])
	print ids
	return ids