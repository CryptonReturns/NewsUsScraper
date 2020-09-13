from bs4 import BeautifulSoup 
import requests 
import datetime
from summarize import getSummary

headers = {
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0",
}

def parseTime(time):
    # timestamp = datetime.datetime.fromtimestamp(time)
    # return timestamp.strftime("%d/%m/%Y %H:%M:%S")
    return time

def financialExpress(url):
    flag = False
    try:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        flag = False
    except Exception as e: 
        return {}
    try:
        headlineSoup = soup.find(class_ = "post-title")
        headline = headlineSoup.text
    except:
        flag = True
    try:
        timeSoup = soup.find(class_ = "place-line")
        time = parseTime(timeSoup.span['content'])    
    except:
        print("Cannot find datetime")
        time = datetime.datetime.now()
        time = time.strftime("%d/%m/%Y %H:%M:%S")
    try:
        imageSoup = soup.find(class_="article-image")
        image = imageSoup.figure.img["src"]
    except:
        image = "https://image.freepik.com/free-vector/money-bag_16734-108.jpg" # bOiler plate image link
    try:
        content = ""    
        soup = soup.find(class_="post-summary")
        contentSoupList = soup.find_all('p', recursive=False)
        for contentSoup in contentSoupList:
            content = content + contentSoup.text
        summary, keywords = getSummary(content)
        if len(summary.split(" ")) == 0:
            flag = True
    except: 
        flag = True    
    if not flag:
        article = {
            "headline": headline,
            "time": time,
            "category": "Finance",
            "url": url,
            "source": "Financial Express",
            "image_url": image,
            "body": summary,
            "keywords": keywords
        }
        return article
    else:
        return {}
        
if __name__ == "__main__":
    print(financialExpress("https://www.financialexpress.com/economy/retail-inflation-to-come-down-with-easing-of-lockdowns-chief-economic-adviser/2082058/"))
