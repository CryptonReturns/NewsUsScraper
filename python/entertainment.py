from bs4 import BeautifulSoup 
import requests 

listSite = "https://www.nytimes.com/section/arts/television"
topEntertainmentNews = []
from nytimes import nytimes
node = requests.get(listSite).text
soup = BeautifulSoup(node, 'html.parser') 
listN = soup.find(id ="stream-panel").find('ol').find_all('li')
for site in listN :
    print("123")
    link = "https://www.nytimes.com/" + site.find('a')["href"]
    topEntertainmentNews.append(nytimes(link))

# listSite = "https://indianexpress.com/section/entertainment/"
# topEntertainmentNews2 = []

# node = requests.get(listSite).text
# soup = BeautifulSoup(node, 'html.parser') 
# listN = soup.find(class_ ="nation").find_all(class_ ="articles")

# for site in listN:
#     link = site.find(class_ = "title").a["href"]
#     heading = site.find(class_ = "title").a.text
#     news = {
#         "href": link,
#         "headline": heading
#     }
#     topEntertainmentNews2.append(news)