import sys 
# import requests 
# from bs4 import BeautifulSoup  
from csv import writer 


import firebase_admin
from firebase_admin import credentials
from firebase_admin import db   
cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "newsusnetwork",
  "private_key_id": "f2639cfb48a2636f827e3ba6fd5c98ba1c79b19b",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCizWA0OngSeinA\nlHG9ARv2QXfIG5TfL/g4kTFnvvQbH+whdM3zKS/w83MAiAI0DfiQiwKK4SMvZbSN\nRyIfjkTol8lFKr4wTreYRL2YzV+vlUsWFxRekt4q52wZPy0Hyk1p8bbUKaFpZums\nFRBVnN5djRttbn9QQY8aJwwM59GjYcHb0pwKCptSkNwY9UeS3OzIvH0ZIebvoSii\ndbZbs3HTzyhH3j95IRlnzYVNL/m3hFiEVoOwqcNuUb8wKGUSQI3L+F8Spn+OUfpg\ng1MZfYQvlU0v/6HZYQimpS6KUEbRfbfhTpwZMyvJqv+KQp751ysUkcgs9NlPprDm\n+ngx0MuzAgMBAAECggEAAgN/TGfbn1g3z+CX8RvPA8l2vG4Py2OVcuU5S5q1/CCS\nHrx7894rt1raoD0cpd1nCkal5Fjc32HuRfG+IQd1EfXeN/Gg5kLXb/JTDOnYgNxq\nl0j3ryRyBLQrFUmGs1aT9uHkNzF5vSBmdru0L72RllFqb2BaOuPzz1cOaWDlxoW2\nPsX8a+k/SK1L2ggeIh6K8V1YjxcUy9jrNPyFaulO9GUnXjxYYZ2AP2iZtOW4J5jQ\n4mhRzBVOgot0ktNtpvauaOCb0sUlmD/5E/4tCqWzWD3eCAErAMV33Rk+49gauTxI\n3AYP5DmaMd9zlMaEwna/xWwjVymRlR4Wzh9R9XozMQKBgQDT1sMHYBjzr5Ro/RcK\nNZpQEu4S8/hAkU8Q4U4WGo73TAjWMdyJ6Mu+MIr7uNdrhrCLyL8cCh1GBHUHFmPf\n2a2GClCBNCeagde7EQbdUI9Xf8NeD4mMgEBrNN3RMwO+nH+2WWMPSXeyNSdADNzT\nLj2f2tO9PBl7XJPqQuVDdAjXwwKBgQDEvarK/5Au3OUEmB1HlqEtjm6FGNY9zgzF\ny9951aSHm3qH04f/TPZkoYsRQZL7SpNB4XocM9Lr45nMzX+ptrkpIE433GZSWhxQ\nDyxonJrxfY6Ci7izGPBpQwoOloP896Jxgu1QVKfZirseAOtEkEJ2skDCFis5lwfI\nNLPJqFftUQKBgQCjVYzMjADRK4jvpmz0Vz4jDWV5QZkhF6jx5/ZQPqwK6xpJJOrZ\nfqBRhZYz3mJiqthG/0KzOO03RkqBa3cYavtLRXqrFG6QyBpxRwCW9f1/xqf5R1uT\n9HM29e0t1vrFJl+mVqd1av0ab7dSwFgnkBi9v3jRCJzRLCF0V53z82y6BwKBgE6H\nYlfawINkGmnGCdHcVwNnGcg4jLNovoJpCQ+Jbj3Omo8CqQMHhkXOkULXCMMTFkoy\npNoC+Yq8c1RjJjTowWmgAnibmZ//ZdOy6sfq0pHXyv1ipdue9b8eSjJec9qSQZ3L\nY8wvrjvP+zZTqZTZfB4CsoSF8sTu+uU33Bd/AXGxAoGADMqzKkLbKCc3zx1Y9jpE\nnTwgEXOyHLXF30gs+131aifmiAyT/eR4jdUPAPaygiJql5TFI0etg5emS/pwgzCA\nV3vigxD+Lmar2hS4aAtBl18X2bWTsKmFMfouQfJDKVECsiwqHMStcej4m4ABZLcE\n09DeVQzAsEUeC0suYQhfoIE=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-kqjle@newsusnetwork.iam.gserviceaccount.com",
  "client_id": "105974694340799896519",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-kqjle%40newsusnetwork.iam.gserviceaccount.com"
})
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://newsusnetwork.firebaseio.com/'
})

import time
ref = db.reference('/')

ref.set({
		'articles': {}
		})

UPDATE_TIME = 120

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
