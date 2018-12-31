import requests
from bs4 import BeautifulSoup

class Html_GetUrl:

    def getUrl(self, movieName):
        try:
            url = "https://www.douban.com/search"
            r = requests.get(url,{"q":"{}".format(movieName)})
            print(r.status_code)
        except:
            print("爬取失败")
    
        html = BeautifulSoup(r.text, "html.parser")
        list = html.find("div", class_="result-list")
        endUrl = list.find("div", class_="result").find("div", class_="title").find("a")['href']
        return endUrl




