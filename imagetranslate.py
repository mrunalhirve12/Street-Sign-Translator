import flask
import model
from flask import request
from werkzeug import secure_filename
import datetime
from google.cloud import storage
from google.cloud import vision
from google.cloud import translate

class imagetranslate(flask.views.MethodView):
	def get(self):
		"""
		Displays the form. 
		"""
		return flask.render_template('imagetranslate.html')


	def post(self):
		"""
		posts the data 
		when image is submitted OCR is performed and extracts the text on image
		the text is further passed to Google Cloud Translate API that translate
		the foreign text to english
		"""
		data=request.form.to_dict(flat=True)
		image = request.files['image']
		new_filename = safe_filename(image.filename)
		url = upload_file(image.read(), new_filename, image.content_type)
		new_filename = "gs://cs410c/" + new_filename
		text = detect_text_uri(new_filename)
		client =  translate.Client()
		translation = client.translate(text, target_language='en')
		model.insert(url, text, translation['translatedText'])
		return translation['translatedText']

def safe_filename(filename):
	"""
	creates filename in the format of YYYY-MM-DD-HHMMSS
	:param filename:string of the filename
	:return: filename-yyyy-mm-dd-hhmmss
	"""
	filename = secure_filename(filename)
	date = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H%M%S")
	basename, extension = filename.rsplit('.', 1)
	return "{0}-{1}.{2}".format(basename, date, extension)


def upload_file(file_stream, filename, content_type):
	"""
	Upload image from the form to the cloud storage
	:param form: contains filename of uploaded form
	:return: Returns the image url for accessing image
	"""
	client = storage.Client()
	bucket = client.get_bucket("cs410c")
	blob = bucket.blob(filename)

	blob.upload_from_string(
		file_stream,
		content_type=content_type)
	blob.make_public()
	url = blob.public_url

	return url

def detect_text_uri(uri):
	"""
	OCR is performed on image to extract text and translate it
	:param uri: uri of the image
	:return: text on image
	"""
	client = vision.ImageAnnotatorClient()
	image = vision.types.Image()
	image.source.image_uri = uri

	response = client.text_detection(image=image)
	texts = response.text_annotations
	
	return texts[0].description
