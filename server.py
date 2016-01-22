from flask import *
from config import configure

app = Flask(__name__)
configure(app)

@app.route('/')
def render_index():
	return render_template('index.html')
	
if __name__ == '__main__':
	from config import db
	app.run(debug=True)