import os
import SQLServerDBLink

# SQLServerDBLinkMyDB
iWearDB = SQLServerDBLink.SQLServerDBLinkMyDB()

# SQLServerDBLink241DB
# iWearDB = SQLServerDBLink.SQLServerDBLink241DB()

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

    # 判斷 MyDB 是否有原有輸出檔案存在
    filePathMyDB = "DataAnalysisResult/analysisResultMyDB.txt"
    if os.path.isfile(filePathMyDB):
        os.remove(filePathMyDB)

    # 判斷 241DB 是否有原有輸出檔案存在
    # filePath241DB = "DataAnalysisResult/analysisResult241DB.txt"
    # if os.path.isfile(filePath241DB):
    #     os.remove(filePath241DB)

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

        # 將分析結果寫成檔案 MyDB
        with open('DataAnalysisResult/analysisResultMyDB.txt',"a",encoding='UTF-8') as printFile:
            printFile.write(cusNoPostCntSortB+"\n")

        # 將分析結果寫成檔案 241DB
        # with open('DataAnalysisResult/analysisResult241DB.txt',"a",encoding='UTF-8') as printFile:
        #     printFile.write(cusNoPostCntSortB+"\n")

getPossible("64")
