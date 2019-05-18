import pyodbc
import MyJieba_hant

def cursorToList(SQLCmd):
    cursor.execute(SQLCmd)
    result = cursor.fetchall()
    listResult=[]
    for row in result:
        listRow = [row]
        string = ",".join(str(v) for v in listRow)
        string=string.replace(" ","").replace("'","").replace("(","").replace(")","")
        listCut = string.split(',')
        listResult.append(listCut)
    return listResult

iWearDB = pyodbc.connect(
    'DRIVER={SQL Server}; SERVER=140.131.114.241,1433; DATABASE=108-510; UID=108iwear; PWD=@108iwear',
    ENGINE = "sql_server.pyodbc",
    NAME= "108-510",
    HOST="140.131.114.241,1433",
    USER="108iwear",
    PASSWORD="@108iwear",
)

cursor = iWearDB.cursor()

for row in cursorToList("SELECT memInform.account, memInform.gender, memInform.birth, memInform.height, memInform.weight, post.word, post.photo, post.styleNo, post.accessoriesNo, post.clothesNo, post.coatNo, post.pantsNo, post.shoesNo FROM dbo.memInform AS memInform LEFT JOIN dbo.post AS post ON memInform.account=post.account"):
    MyJieba_hant.MyJieba_hant(context=row[5])

listPostStyleOption=['styleNo','accessoriesNo','clothesNo','coatNo','pantsNo','shoesNo']
listPercent=[30,10,15,15,15,15]

def getWeights(cusNo):

    arr=[]
    for i in range(len(listPostStyleOption)):
        SQLCmd="SELECT "+listPostStyleOption[i]+", COUNT(*) AS cnt FROM post WHERE account= '"+cusNo+"' GROUP BY "+listPostStyleOption[i]+";"

        styleSum=0
        rowMax=0
        for j in cursorToList(SQLCmd):
            # 加總
            styleSum+=int(j[1])
            rowMax+=1

        # 算比例
        print(styleSum/rowMax)
        arr.append(styleSum/rowMax)
    print(len(arr))

getWeights("44")
