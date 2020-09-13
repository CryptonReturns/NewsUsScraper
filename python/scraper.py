import sys 
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred_json = {
  "type": "service_account",
  "project_id": "newsusnetwork",
  "private_key_id": os.environ["PRIVATE_KEY_ID"],
  "private_key": os.environ["PRIVATE_KEY"],
  "client_email": os.environ["CLIENT_EMAIL"],
  "client_id": os.environ["CLIENT_ID"],
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": os.environ["CLIENT_CERT_URL"]
}

cred = credentials.Certificate(cred_json)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://newsusnetwork.firebaseio.com/'
})

import time
ref = db.reference('/')

ref.set({
		'articles': {}
		})

UPDATE_TIME = 5

def scrapeSports() :
	from sports import topSportsNews as a ,topSportsNews2 as b
	articles = []
	for i in a:
		articles.append(i)
	for i in b:
		articles.append(i)
	return articles

articles = {}
articles["sports"] = []

#server:
while (True):
	articles["sports"] += (scrapeSports())
	ref.set({
			'articles': articles
		})
	time.sleep(UPDATE_TIME)
