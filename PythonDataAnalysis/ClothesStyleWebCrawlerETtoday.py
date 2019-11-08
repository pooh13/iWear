import requests
import iWearFunction

from bs4 import BeautifulSoup

etToday_url = 'https://www.ettoday.net/news'
r = requests.get(etToday_url+"/focus/%E6%99%82%E5%B0%9A/%E6%BD%AE%E6%B5%81%E7%A9%BF%E6%90%AD/")

arr=[]

# 確認是否下載成功
if r.status_code == requests.codes.ok:

    # 以 BeautifulSoup 解析 HTML 原始碼
    soup = BeautifulSoup(r.text, 'lxml')

    # 抓取穿搭板內文網頁
    for i in soup.find(attrs={"class":"block block_1 infinite_scroll"}).findAll(attrs={"class":"piece clearfix"}):
        urltag = i.find(attrs={"a":""})
        url = urltag.get('href')
        urlString=str(url)
        arr.append(urlString)

    for urlString in arr:
        completeUrl = etToday_url+urlString
        print(completeUrl)
        soup = BeautifulSoup(requests.get(completeUrl).text, 'lxml')
        title = soup.select('h1')
        topic = soup.select('div.part_keyword > a')

        for clean in title:
            print(clean.text+"\n"+"-"*50)

        for clean in topic:
            print(clean.text)

        # context = soup.find("div",attrs={class":"/news/20190917/1536808.htm"}).text
        # print(iWearFunction.MyJieba_hant(context))
        print("\n"+"="*60)
