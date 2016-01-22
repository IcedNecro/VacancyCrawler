# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from db_config import Vacancy, Session,es
import requests

class CrawlerPipeline(object):
	def process_item(self, item, spider):
		
		session = Session()
		if spider.name == 'stepstone_crawler':
			source = 'stepstone'
		else:
			source = 'monster'
		previous = session.query(Vacancy).filter_by(source=source, **item).first()
		if not previous:
			new_vacancy = Vacancy(source=source, **item)
			session.add(new_vacancy)
			session.commit()
			# adding to elastic search
			es.index(index="vacancies", doc_type="vacancy", id=new_vacancy.id, body={"id": new_vacancy.id, "title": item['title'], 'company_name':item['company_name']})
		session.close()

		return item
