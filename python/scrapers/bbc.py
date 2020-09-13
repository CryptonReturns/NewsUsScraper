import sys
from bs4 import BeautifulSoup 
import requests 
import datetime
sys.path.append("../")
from summarize import getSummary

headers = {
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0",
}

def parseTime(time):
    timestamp = datetime.datetime.fromtimestamp(time)
    return timestamp.strftime("%d/%m/%Y %H:%M:%S")

def bbc(url):
    flag = False
    try:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        flag = False
    except Exception as e: 
        return {}
    try:
        headlineSoup = soup.find(class_ = "story-body__h1")
        headline = headlineSoup.text
    except:
        flag = True
    try:
        timeSoup = soup.find(class_ = "date")
        time = parseTime(timeSoup['data-seconds'])    
    except:
        print("Cannot find datetime")
        time = datetime.datetime.now()
        time = time.strftime("%d/%m/%Y %H:%M:%S")
    try:
        imageSoup = soup.find(class_="image-and-copyright-container")
        image = imageSoup.img["src"]
    except:
        image = "https://image.flaticon.com/icons/png/512/21/21601.png" # bOiler plate image link
    try:
        content = ""    
        soup = soup.find(class_="story-body__inner")
        contentSoupList = soup.find_all('p', recursive=False)
        for contentSoup in contentSoupList:
            content = content + contentSoup.text
        summary, keywords = getSummary(content)
    except: 
        flag = True    
    if not flag:
        article = {
            "headline": headline,
            "time": time,
            "category": "International",
            "url": url,
            "source": "BBC",
            "image_url": image,
            "body": summary,
            "keywords": keywords
        }
        return article
    else:
        return {}
        
if __name__ == "__main__":
    print(bbc("https://www.bbc.com/news/world-us-canada-54130785"))
