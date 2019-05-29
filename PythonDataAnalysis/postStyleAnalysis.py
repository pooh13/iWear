import  pyodbc

def cursorToList(cusNoPostCntSortSQLCmd):
    cursor.execute(cusNoPostCntSortSQLCmd)
    result = cursor.fetchall()
    listResult=[]
    for row in result:
        listRow = [row]
        string = ",".join(str(v) for v in listRow)
        string=string.replace(" ","").replace("'","").replace("(","").replace(")","")
        listCut = string.split(',')
        listResult.append(listCut)
    return listResult

# IP: 220.135.161.251
iWearDB = pyodbc.connect(
    'DRIVER={SQL Server}; SERVER=220.135.161.251,1433; DATABASE=108-510; UID=sa; PWD=sqlserver',
    ENGINE = "sql_server.pyodbc",
    NAME= "108-510",
    HOST="220.135.161.251,1433",
    USER="sa",
    PASSWORD="sqlserver",
)

# IP: 140.131.114.241
# iWearDB = pyodbc.connect(
#     'DRIVER={SQL Server}; SERVER=140.131.114.241,1433; DATABASE=108-510; UID=sa; PWD=sqlserver',
#     ENGINE = "sql_server.pyodbc",
#     NAME= "108-510",
#     HOST="140.131.114.241,1433",
#     USER="108iwear",
#     PASSWORD="@108iwear",
# )

cursor = iWearDB.cursor()

listPercent=[0.3,0.1,0.15,0.15,0.15,0.15]

def getPossible(cusNo):
    # 把所有種類抓出來
    arrTable=['style','accessories','clothes','coat','pants','shoes']
    arrTableCol=['styleNo','accessoriesNo','clothesNo','coatNo','pantsNo','shoesNo']
    arrAllRow=[] # [[ST01,ST02],[PA01,PA02]] [[ST01,ST02,ST03],[PA01,PA02,PA03]]
    for table in arrTable:
        tableSQLCmd="SELECT * FROM "+table+";"
        arrTableCols=[]
        for cols in cursorToList(tableSQLCmd):
            arrTableCols.append(cols[0])
        arrAllRow.append(arrTableCols)

    sum=0
    for cusNoPostCnt in cursorToList("SELECT COUNT(*) as cnt FROM post WHERE account="+cusNo+";"):
        sum=int(cusNoPostCnt[0])

    # 尋找user每一種可能的比例
    cusNoPostCntSortA=""

    # { cusNoPostCntSortCmdA=["SELECT COUNT(*) as cnt,"] } { cusNoPostCntSortCmd01=[,] }
    # { cusNoPostCntSortCmdB=[" FROM post WHERE account ="+cusNo+" GROUP BY "," ORDER BY "] }
    cusNoPostCntSortSQLCmd=["SELECT COUNT(*) as cnt,"," FROM post WHERE account ="+cusNo+" GROUP BY "," ORDER BY "]

    # 加入 cusNoPostCntSortCmdA
    for cusNoPostCntSortCmdA in cusNoPostCntSortSQLCmd:
        cusNoPostCntSortA+=cusNoPostCntSortCmdA
        cnt=0
        # print(cusNoPostCntSortA)

        # 插入arrTableCol欄位於 cusNoPostCntSortCmdA & cusNoPostCntSortCmdB 之中
        for cusNoPostCntSortCmd01 in arrTableCol:
            cnt+=1
            cusNoPostCntSortA+=cusNoPostCntSortCmd01
            if cnt>=len(arrTableCol):break
            cusNoPostCntSortA+=","

    # 列印出(SELECT COUNT(*) as cnt,styleNo,accessoriesNo,clothesNo,coatNo,pantsNo,shoesNo FROM post WHERE account =64 GROUP BY styleNo,accessoriesNo,clothesNo,coatNo,pantsNo,shoesNo ORDER BY styleNo,accessoriesNo,clothesNo,coatNo,pantsNo,shoesNo)
    print(cusNoPostCntSortA)

    # 抓取且執行 cusNoPostCntSortA 查詢結果 = arrPersonalRow
    for arrPersonalRow in cursorToList(cusNoPostCntSortA):
        cusNoPostCntSortB=""
        # print(arrPersonalRow)

        # 轉換成同一欄位
        for PersonalRow in range(len(arrPersonalRow)):
            cusNoPostCntSortB+=arrPersonalRow[PersonalRow]
            # print(cusNoPostCntSortB)
        cusNoPostCntSortB+=" 比例:"+str(int(arrPersonalRow[0])/sum)

        # 列印出每一種可能及比例
        print(cusNoPostCntSortB)

        # 將分析結果寫成檔案 localhost DB
        with open('analysisResultlocalDB.txt',"a",encoding='UTF-8') as printFile:
            printFile.write(cusNoPostCntSortB+"\n")

        # 將分析結果寫成檔案 140.131.114.241 DB
        # with open('analysisResult241sDB.txt',"a",encoding='UTF-8') as printFile:
        #     printFile.write(cusNoPostCntSortB+"\n")

getPossible("64")
