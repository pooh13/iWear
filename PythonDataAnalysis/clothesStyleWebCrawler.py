import requests, iWearFunction

from bs4 import BeautifulSoup

cleanSQLDB = ("DELETE webSentence Where webSentenceNo In (Select Max(webSentenceNo) From webSentence Group By web)")
iWearFunction.cursorGInsert(cleanSQLDB)

def clothesStyleWebCrawlerGoogleSearch():
    # Google 搜尋 URL
    google_url = 'https://www.google.com.tw/search'

    # 查詢參數
    my_params = {'q': '校園風格'}

    # 下載 Google 搜尋結果
    r = requests.get(google_url, params = my_params)

    # 確認是否下載成功
    if r.status_code == requests.codes.ok:
      # 以 BeautifulSoup 解析 HTML 原始碼
      soup = BeautifulSoup(r.text, 'lxml')
      # 以 CSS 的選擇器來抓取 Google 的搜尋結果
      items = soup.select('div.g > h3.r > a[href^="/url"]')

      for i in items:
        # 標題
        print("標題：" + i.text)
        # 網址
        print("網址：" + i.get('href'))

# clothesStyleWebCrawlerGoogleSearch()

def clothesStyleWebCrawlerDcard():

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
            completeUrl = dcard_url+urlString

            soup = BeautifulSoup(requests.get(completeUrl).text, 'lxml')
            title = soup.select('div.Post_wrapper_2rR09w > div.Post_meta_MVFsOq > h1')
            topic = soup.select('div.Post_wrapper_2rR09w > div.Post_content_NKEl9d > div.Post_topicList_2U8B7- > div.TopicList_root_17gqVK > ul > li')

            for clean in title:
                title = clean.text

            topicList = []

            for clean in topic:
                topics = clean.text
                topicList.append(topics)

            topicList = '/'.join(topicList)

            result = "'"+completeUrl+"'"+","+"'"+title+"'"+","+"'"+topicList+"'"
            # print("\n"+result)

            print("\n"+"-"*50)
            insertSQLCmd = ("INSERT INTO webSentence VALUES("+result+") SET ANSI_WARNINGS OFF ;")

            print(insertSQLCmd)
            iWearFunction.cursorGInsert(insertSQLCmd)

clothesStyleWebCrawlerDcard()


def clothesStyleWebCrawlerETtoday():

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
            soup = BeautifulSoup(requests.get(completeUrl).text, 'lxml')
            title = soup.select('h1')
            topic = soup.select('div.part_keyword > a')

            for clean in title:
                title = clean.text

            topicList = []

            for clean in topic:
                topics = clean.text
                topicList.append(topics)

            topicList = '/'.join(topicList)

            result = "'"+completeUrl+"'"+","+"'"+title+"'"+","+"'"+topicList+"'"

            # print("\n"+result)

            print("\n"+"-"*50)
            insertSQLCmd = ("INSERT INTO webSentence VALUES("+result+") SET ANSI_WARNINGS OFF ;")

            print(insertSQLCmd)
            iWearFunction.cursorGInsert(insertSQLCmd)

clothesStyleWebCrawlerETtoday()


def clothesStyleWebCrawlerGamme():
    gamme_url = 'https://news.gamme.com.tw'
    r = requests.get(gamme_url+"/tag/%E7%A9%BF%E6%90%AD")

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
            completeUrl = gamme_url+urlString
            print(completeUrl)
            soup = BeautifulSoup(requests.get(completeUrl).text, 'lxml')
            title = soup.select('div.Post_wrapper_2rR09w > div.Post_meta_MVFsOq > h1')
            topic = soup.select('div.Post_wrapper_2rR09w > div.Post_content_NKEl9d > div.Post_topicList_2U8B7- > div.TopicList_root_17gqVK > ul > li')

            for clean in title:
                print(clean.text+"\n"+"-"*50)

            for clean in topic:
                print(clean.text)

            # context = soup.find("div",attrs={"class":"Post_content_NKEl9d"}).text
            # print(iWearFunction.MyJieba_hant(context))
            print("\n"+"="*60)

# clothesStyleWebCrawlerGamme()


def clothesStyleWebCrawlerMeteor():
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
            print(iWearFunction.MyJieba_hant(context))

# clothesStyleWebCrawlerMeteor()


def clothesStyleWebCrawlerMobile01():
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

# clothesStyleWebCrawlerMobile01()


