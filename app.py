import flask, flask.views 
from main import Main
from records import records
from imagetranslate import imagetranslate

app = flask.Flask(__name__)
#pp.secret_key = auth.secret_key

"""
Class based views. Each class containing a 'get' and 'post' method.
'get' method to render the page.  Pages having form input only have
'post' method implemented to perform action on form data
"""
app.add_url_rule('/', view_func=Main.as_view('index'), methods =["GET", "POST"])

app.add_url_rule('/records', view_func=records.as_view('records'), methods = ['GET', 'POST'])

app.add_url_rule('/imagetranslate', view_func=imagetranslate.as_view('imagetranslate'), methods = ['GET', 'POST'])

app.debug=True


"""
Initializing main method to run on given host and port no
"""
if __name__ == '__main__':
	
	app.run (host= '0.0.0.0', port=8888, debug=True)

