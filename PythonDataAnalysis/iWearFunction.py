import SQLServerDBLink
import jieba_hant
import urllib.request
import socket

# DB.(1/3 A) SQLServerDBLinkMyDB
# iWearDB = SQLServerDBLink.SQLServerDBLinkMyDB()

# DB.(1/3 B) SQLServerDBLink241DB
iWearDB = SQLServerDBLink.SQLServerDBLink241DB()
cursor = iWearDB.cursor()

def cursorGFetch(cursorGResult):
    cursor.execute(cursorGResult)
    cursorGResult = cursor.fetchall()

    return cursorGResult

def cursorGInsert(cursorGResult):
    cursor.execute(cursorGResult)
    iWearDB.commit()

def toList(result):
    listResult=[]

    for row in result:
        listRow = [row]
        string = ",".join(str(v) for v in listRow)
        string=string.replace(" ","").replace("'","").replace("(","").replace(")","")
        listCut = string.split(',')
        listResult.append(listCut)

    return listResult

def cursorToList(cursorToListResult):
    cursor.execute(cursorToListResult)
    cursorToListResult = cursor.fetchall()
    cursorToList = toList(cursorToListResult)

    return cursorToList

from collections import Counter
def MyJieba_hant(context):
    # print("原文內容："+context)
    sentence=([t for t in jieba_hant.cut(context, cut_all=False)])
    # print("斷詞結果：",sentence)
    # -------------------------------------------------------------------------
    cnt = Counter()

    for x in sentence:
        if len(x)>1 and x != '\r\n':
            cnt[x] += 1

    # print("字詞出現頻率統計結果\n")
    for (k,v) in cnt.most_common(5):
        # print("%s%s %s  %d" % ("  "*(5-len(k)), k, "*"*int(v/3), v))
        result = k+","+str(v)
        print(result)

    print("\n"+"-"*80+"\n")

def get_Content403(url,host):

    # @獲取403禁止訪問的網頁

    req= urllib.request.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36")
    req.add_header("Host",host)
    req.add_header("Referer","https://"+host+"/")
    req.add_header("GET",url)

    content=urllib.request.urlopen(req).read()

    return content

    # https://blog.csdn.net/jsqfengbao/article/details/44594985
    # https://blog.csdn.net/sinat_37802274/article/details/79536300

# def restartProgram():
#     os.execl(sys.executable, sys.executable, * sys.argv)
#     if __name__ == "__main__":
#         restartProgram()

def socketLoginChecker():
    bind_ip = socket.gethostname()
    bind_port = 9999

    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    server.bind((bind_ip,bind_port))
    server.listen(5)

    print("[*] Listening on "+bind_ip,bind_port)

    while True:
        client,addr = server.accept()
        print('Connected by '+str(addr))

        while True:
            data = client.recv(1024)
            print("Client recv data:"+str(data))
            client.send("ACK！".encode())
