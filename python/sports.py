from bs4 import BeautifulSoup 
import requests 
topSportsNews = []

listSite = "https://timesofindia.indiatimes.com/sports"
node = requests.get(listSite).text
soup = BeautifulSoup(node, 'html.parser') 
listN = (soup.find(class_ ="top-newslist small").ul.find_all('li'))

from indianexpress import indianExpress
from toi import toi
for site in listN :
    link ="https://timesofindia.indiatimes.com" + site.find(class_ ="w_tle").a["href"]
    heading = site.find(class_ ="w_tle").text
    news = toi(link) 
    topSportsNews.append(news)
topSportsNews2 = []

listSite = "https://indianexpress.com/section/sports/"
node = requests.get(listSite).text
soup = BeautifulSoup(node, 'html.parser') 
listN = soup.find(class_ = "nation").find_all(class_ = "articles")

for site in listN:
    link = site.h2.a["href"]
    topSportsNews2.append(indianExpress(link))
