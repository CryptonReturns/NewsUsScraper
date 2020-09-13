from bs4 import BeautifulSoup 
import requests 
topSportsNews = []

listSite = "https://timesofindia.indiatimes.com/sports"
node = requests.get(listSite).text
soup = BeautifulSoup(node, 'html.parser') 
listN = (soup.find(class_ ="top-newslist small").ul.find_all('li'))

from indianexpress import indianExpress
# for site in listN :
#     link ="https://timesofindia.indiatimes.com" + site.find(class_ ="w_tle").a["href"]
#     heading = site.find(class_ ="w_tle").text
#     body,imageHref = getImageAndText(link) 
    
#     if body == None:
#         continue
#     news = {
#         "category":"Sports",
#         "source":"Times of India",

#         "href": link,
#         "headline": heading,
#         "imageHref": imageHref,
#         "body": body 
#     }

#     topSportsNews.append(news)
# print(topSportsNews)
topSportsNews2 = []

listSite = "https://indianexpress.com/section/sports/"
node = requests.get(listSite).text
soup = BeautifulSoup(node, 'html.parser') 
listN = soup.find(class_ = "nation").find_all(class_ = "articles")

for site in listN:
    link = site.h2.a["href"]
    topSportsNews2.append(indianExpress(link))

print(topSportsNews2[0])
