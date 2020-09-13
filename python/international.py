from bs4 import BeautifulSoup 
import requests 
from summarize import getSummary
import datetime
def parseTime(time):
    return time

from bbc import bbc

headers = {
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0",
}
listSite = "https://www.bbc.com/news"
baseURL = "https://www.bbc.com"
page = requests.get(listSite, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
listN = soup.find_all(class_ = "nw-c-top-stories__secondary-item") 

topNews = []
for site in listN :
    link = baseURL + site.find('a')["href"]
    topNews.append(bbc(link))
# print(topNews)

listN = soup.find_all(class_ = "nw-c-top-stories__tertiary-top")
listN.extend(soup.find_all(class_ = "nw-c-top-stories__tertiary-items"))

for site in listN:
    link = baseURL + site.find('a')["href"]
    topNews.append(bbc(link))
