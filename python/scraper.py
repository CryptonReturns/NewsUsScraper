import sys 
# import requests 
# from bs4 import BeautifulSoup  
from csv import writer 


import firebase_admin
from firebase_admin import credentials
from firebase_admin import db   
cred = credentials.Certificate('../cred.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://newsusnetwork.firebaseio.com/'
})

import time
ref = db.reference('/')

ref.set({
		'articles': {}
		})

UPDATE_TIME = 5

'''
response = requests.get('https://leetcode.com/shubhamk314') 
soup = BeautifulSoup(response.text, 'html.parser') 
# It will create csv files named progress.csv in root folder once this is script is called. 
with open('progress.csv', 'w') as csv_file: 
	csv_writer = writer(csv_file) 
	headers = ['Name', 'Score'] 
	csv_writer.writerow(headers) 
	csv_writer.writerow(['rohan', '90'])

print("csv file created for leetcode") 
'''
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
