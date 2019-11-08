import requests, iWearFunction
import urllib
from bs4 import BeautifulSoup

mobile01_url = 'https://www.mobile01.com'

r=iWearFunction.get_Content403(mobile01_url+"/topiclist.php?f=302","www.mobile01.com")
arr=[]
# if r.status_code == requests.codes.ok:
# 以 BeautifulSoup 解析 HTML 原始碼
soup = BeautifulSoup(r, 'lxml')
#抓取穿搭板內文網頁
for i in soup.findAll(attrs={"class":"topic_gen"}):
    url = i.get('href')
    urlString=str(url)
    urlString=urlString[urlString.index("topicdetail.php?f=302&t="):]
    arr.append(urlString)
for urlString in arr:
    print(mobile01_url+"/"+urlString)
    soup = BeautifulSoup(requests.get(mobile01_url+"/"+urlString).text, 'lxml')
    title = soup.select('div.forum-content > main > h1')
    for clean in title:
        print(clean.text)
    # context = soup.find("div",attrs={"id":"ct72381770"})
    # print(iWearFunction.MyJieba_hant(context))
