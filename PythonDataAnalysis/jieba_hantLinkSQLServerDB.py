# Connect SQL
import pyodbc
import MyJieba_hant
from collections import Counter

def func(s):
    cursor.execute(s)
    result = cursor.fetchall()
    listC=[[]]
    for row in result:
        listA = [row]
        string = ",".join(str(v) for v in listA)
        listCut = string.split(',')
        listC.append(listCut)
    return listC

iWear = pyodbc.connect(
    'DRIVER={SQL Server}; SERVER=140.131.114.241,1433; DATABASE=108-510; UID=108iwear; PWD=@108iwear',
    ENGINE = "sql_server.pyodbc",
    NAME= "108-510",
    HOST="140.131.114.241",
    USER="108iwear",
    PASSWORD="@108iwear",
)
cursor = iWear.cursor()

# Read
cursor.execute("SELECT memInform.account, memInform.gender, memInform.birth, memInform.height, memInform.weight, post.word, post.photo, post.styleNo, post.accessoriesNo, post.clothesNo, post.coatNo, post.pantsNo, post.shoesNo FROM dbo.memInform as memInform left join dbo.post as post on memInform.account=post.account")
result = cursor.fetchall()
cnt = Counter()
styleNo=[]
# JiebaCutAnalyze
for row in result:
    listA = [row]
    string = ",".join(str(v) for v in listA)
    listCut = string.split(',')
    styleNo = listCut[7]
    MyJieba_hant.MyJieba_hant(context=listCut[5])

listB=['styleNo','accessoriesNo','clothesNo','coatNo','pantsNo','shoesNo']
userId="44"
for i in range(6):
    s="select styleNo,count(*) as cnt from  post where account= '"+userId+"' Group by "+listB[i]+";"
    # for j in func(s):



# ST02 = cursor.fetchall()
# print(ST02)




















