import requests
import MyJieba_hant

from bs4 import BeautifulSoup

dcard_url = 'https://www.dcard.tw'
r = requests.get(dcard_url+"/f/dressup")

arr=[]

# 確認是否下載成功
if r.status_code == requests.codes.ok:

    # 以 BeautifulSoup 解析 HTML 原始碼
    soup = BeautifulSoup(r.text, 'lxml')

    # 抓取穿搭板內文網頁
    for i in soup.findAll(attrs={"class":"PostEntry_root_V6g0rd"}):
        url = i.get('href')
        urlString=str(url)
        index=urlString.index("-")
        urlString=urlString[:index]
        arr.append(urlString)

    for urlString in arr:
        print(dcard_url+urlString)
        soup = BeautifulSoup(requests.get(dcard_url+urlString).text, 'lxml')
        title = soup.select('div.Post_wrapper_2rR09w > div > h2')

        for clean in title:
            print(clean.text)

        context = soup.find("div",attrs={"class":"Post_content_NKEl9d"}).text
        print(MyJieba_hant.MyJieba_hant(context))



