from imodel import IModel
from google.cloud import datastore

def list(limit= 100):
	"""
	uery to list all the records from table in the datastore in the
	form of dictionary.
	:return: a list of dict  
	"""
	client=datastore.Client()
	query = client.query(kind='imagetranslate')
	entities = query.fetch(limit)
	return entities 

def insert(image_url, untranslated, translated):
	"""
	Query that inserts the data related to image, text and translated 
	text to table in the datastore. Populate the model object with 
	form data.
	:return: String 
	"""
	client=datastore.Client()
	image_entity = datastore.Entity(key=client.key('imagetranslate'))
	image_entity['image_url'] = image_url
	image_entity['untranslated'] = untranslated
	image_entity['translated'] = translated
	client.put(image_entity)

