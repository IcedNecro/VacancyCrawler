from config import db

class Vacancy(db.Model):
	__tablename__ = 'vacancies'
	id = db.Column(db.Integer, primary_key=True)
	company_name = db.Column(db.String())
	image_path = db.Column(db.String())
	place = db.Column(db.String())
	title = db.Column(db.String())
	source = db.Column(db.String())

	def __init__():
		self.to_json = to_json