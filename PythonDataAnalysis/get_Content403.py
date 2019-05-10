import urllib.request
def get_Content403(url,host):
    '''
    @獲取403禁止訪問的網頁
    '''

    req= urllib.request.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36")
    req.add_header("Host",host)
    req.add_header("Referer","https://"+host+"/")
    req.add_header("GET",url)

    content=urllib.request.urlopen(req).read()
    return content

# https://blog.csdn.net/jsqfengbao/article/details/44594985
# https://blog.csdn.net/sinat_37802274/article/details/79536300
