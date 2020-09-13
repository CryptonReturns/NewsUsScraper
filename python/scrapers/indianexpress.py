import sys
from bs4 import BeautifulSoup 
import requests 
import pprint 
sys.path.append("../")
from summarize import getSummary

import datetime
def parseTime(time):
    return time
headers = {
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0",
}

def indianExpress(url):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    headlineSoup = soup.find(class_ = "heading-part")
    headline = headlineSoup.h1.text
    soup = soup.find(class_ = "full-details")
    timeSoup = soup.find(id = "storycenterbyline")
    time = timeSoup.span['content']
    imageSoup = soup.find(class_="custom-caption")
    image = imageSoup.img["src"]
    category = url.split('/')[4]
    # get content
    content = ""
    contentSoupList = soup.find_all('p', recursive=False)
    for contentSoup in contentSoupList:
        content = content + contentSoup.text
    print(content)
    summary, keywords = getSummary(content)
    article = {
        "headline": headline,
        "time": time,
        "category": category,
        "url": url,
        "source": "The Indian Express",
        "image_url": image,
        "body":summary,
        "keywords": keywords
    }    
    pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(article)
    # print(article)
    print(summary)
    return []

    # Object Model:
    # headline --
    # time(in datetime format) --
    # keywords(returned from summarizer.py)
    # category(from scraping e.g. finance, tech etc.) --
    # body(summary returned from summarizer)
    # url(url to the full article) --
    # source(name of media channel e.g times of india, indianExpress etc.) --
    # image_url(url for article image, if cannot find one then give some boilerplate image from net corresponding to category) -- 
    # randomly generated id for object(mongo creates one on its own, idk about firebase, please see that..)
    # any other field you can think of
    # 9 including id

if __name__ == "__main__":
    indianExpress("https://indianexpress.com/article/sports/tennis/dominic-thiem-clay-bred-us-open-hard-court-contender-6593839/")
    # print(1)