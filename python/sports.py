from bs4 import BeautifulSoup 
import requests 
from summarize import getSummaryPerNews
topSportsNews = []

listSite = "https://timesofindia.indiatimes.com/sports"
node = requests.get(listSite).text
soup = BeautifulSoup(node, 'html.parser') 
listN = (soup.find(class_ ="top-newslist small").ul.find_all('li'))

def getImageAndText(link):
    node = requests.get(link).text
    soup = BeautifulSoup(node, 'html.parser') 
    text = soup.find(class_ = "_1_Akb clearfix")
    if text:
        text = text.text  
    imageHref = soup.find(class_ = "_2gIK-")
    if imageHref:
        imageHref = imageHref.find("img")     
        if imageHref:
            imageHref = imageHref["src"]
    return (text,imageHref)

for site in listN :
    link ="https://timesofindia.indiatimes.com" + site.find(class_ ="w_tle").a["href"]
    heading = site.find(class_ ="w_tle").text
    body,imageHref = getImageAndText(link) 
    
    if body == None:
        continue
    news = {
        "category":"Sports",
        "source":"Times of India",

        "href": link,
        "headline": heading,
        "imageHref": imageHref,
        "body": body 
    }
    if len(body)<50:
        continue
    news = getSummaryPerNews(news)
    topSportsNews.append(news)

topSportsNews2 = []
listSite = "https://indianexpress.com/section/sports/"
node = requests.get(listSite).text
soup = BeautifulSoup(node, 'html.parser') 
listN = soup.find(class_ ="nation").find_all(class_ ="articles")
for site in listN:
    link = site.h2.a["href"]
    heading = site.h2.text
    news = {
        "href": link,
        "headline": heading
    }
    topSportsNews2.append(news)