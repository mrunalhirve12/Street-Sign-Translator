import flask
from flask.views import MethodView

class Main(MethodView):
	"""
	Class for index page
	"""
	
	def get(self):
		"""
		for rendering the index page
		"""
		return flask.render_template('index.html')
	
	
