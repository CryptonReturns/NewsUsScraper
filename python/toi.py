import sys
from bs4 import BeautifulSoup 
import requests 
import pprint 
from summarize import getSummary

import datetime
def parseTime(time):
    return time
headers = {
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0",
}


def toi(url):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        text = soup.find(class_ = "_1_Akb clearfix").text
    except:
        return{}
    try:
        image = soup.find(class_ = "_2gIK-").find("img")["src"]
    except:
        image = None
    headline = soup.find(class_= "_2NFXP").h1.text
    time = None
    try:
        headline = soup.find(class_= "_2NFXP").h1.text
    except:
        return{}
    category = url.split('/')[3]
    content = text
    summary, keywords = getSummary(content)
    article = {
        "headline": headline,
        "time": time,
        "category": category,
        "url": url,
        "source": "Times Of India",
        "image_url": image,
        "body":summary,
        "keywords": keywords
    } 
    print(article["headline"])
    return article

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
    print(1)
