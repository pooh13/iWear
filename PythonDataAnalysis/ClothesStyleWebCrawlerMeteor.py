import requests
import urllib
import MyJieba_hant
from bs4 import BeautifulSoup

meteor_url = 'https://meteor.today/b/styling/new'

r = requests.get(meteor_url)
arr=[]
# 確認是否下載成功
if r.status_code == requests.codes.ok:
    # 以 BeautifulSoup 解析 HTML 原始碼
    soup = BeautifulSoup(r.text, 'lxml')
    #抓取穿搭板內文網頁
    for i in soup.findAll(attrs={"class":"ng-binding"}):
        url = i.get('href')
        urlString=str(url)
        arr.append(urlString)
        print(urlString)
    for urlString in arr:
        print(meteor_url+urlString)
        soup = BeautifulSoup(requests.get(meteor_url+urlString).text, 'lxml')
        title = soup.select('div.header ng-binding > div > p')
        for clean in title:
            print(clean.text)
        context = soup.find("div",attrs={"class":"article_content"}).text
        print(MyJieba_hant.MyJieba_hant(context))



