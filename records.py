import flask
import model


class records(flask.views.MethodView):
	"""
	Class displaying all list of records
	"""
	def get(self):
		"""
		call to list all data from listing table 
		:return: renders the template for listings 
		"""
		data = model.list()
		return flask.render_template('records.html', data=data)
