# Connect SQL
import pyodbc
import MyJieba_hant

def cursor2List(s):
    cursor.execute(s)
    result = cursor.fetchall()
    listC=[]
    for row in result:
        listA = [row]
        string = ",".join(str(v) for v in listA)
        string=string.replace(" ","").replace("'","").replace("(","").replace(")","")
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
# JiebaCutAnalyze

# for row in result:
#     listA = [row]
#     string = ",".join(str(v) for v in listA)
#     string=string.replace(" ","").replace("'","").replace("(","").replace(")","")
#
#     listCut = string.split(',')
#     print(listCut)
#     styleNo = listCut[7]
#     MyJieba_hant.MyJieba_hant(context=listCut[5])

for row in cursor2List("SELECT memInform.account, memInform.gender, memInform.birth, memInform.height, memInform.weight, post.word, post.photo, post.styleNo, post.accessoriesNo, post.clothesNo, post.coatNo, post.pantsNo, post.shoesNo FROM dbo.memInform as memInform left join dbo.post as post on memInform.account=post.account"):
    MyJieba_hant.MyJieba_hant(context=row[5])

listB=['styleNo','accessoriesNo','clothesNo','coatNo','pantsNo','shoesNo']
list_percent=[30,10,15,15,15,15]

def get_weights(cus_no):

    arr=[]
    for i in range(len(listB)):
        s="select "+listB[i]+", count(*) as cnt from post where account= '"+cus_no+"' Group by "+listB[i]+";"

        style_sum=0
        row_max=0
        for j in cursor2List(s):
            # 加總
            style_sum+=int(j[1])
            row_max+=1

        # 算比例
        print(style_sum/row_max)
        arr.append(style_sum/row_max)
    print(len(arr))

get_weights("44")





# ST02 = cursor.fetchall()
# print(ST02)
