import os, cursorToList, cursorG, MyJieba_hant, csv
import loginChecker
from datetime import datetime
import cursorToMySplit
import toList
import socketLoginChecker



userLoginDatetimeSQLCmd = cursorG.cursorG("SELECT CONVERT(varchar(100), last_login, 20) FROM auth_user where id = 62;")

userLoginDatetime = datetime.strptime(userLoginDatetimeSQLCmd[0][0], "%Y-%m-%d %H:%M:%S")

# print(type(userLoginDatetime))
print(userLoginDatetime)
# print(type(userLoginDatetimeSQLCmd[0][0]))

if userLoginDatetime < datetime.now():
    print("datetime is true")
    # loginChecker.loginChecker()
# views.login()
# loginChecker.loginChecker("62")

listPercent=[0.3,0.1,0.15,0.15,0.15,0.15]

# 把所有種類抓出來
arrTable=['style','accessories','clothes','coat','pants','shoes']
arrTableCol=['styleNo','accessoriesNo','clothesNo','coatNo','pantsNo','shoesNo']
arrAllRow=[] # [[ST01,ST02],[PA01,PA02]] [[ST01,ST02,ST03],[PA01,PA02,PA03]]

for table in arrTable:
    tableSQLCmd="SELECT * FROM "+table+";"
    arrTableCols=[]
    for cols in cursorToList.cursorToList(tableSQLCmd):
        arrTableCols.append(cols[0])
    arrAllRow.append(arrTableCols)

def getPossible(cusNo):

    sum=0

    for cusNoPostCnt in cursorToList.cursorToList("SELECT COUNT(*) as cnt FROM post WHERE account = "+cusNo+";"):
        sum=int(cusNoPostCnt[0])
        # print(sum)

    # 尋找user每一種可能的比例
    cusNoPostCntSortA=""

    # { cusNoPostCntSortCmdA=["SELECT COUNT(*) as cnt,"] } { cusNoPostCntSortCmd01=[,] }
    # { cusNoPostCntSortCmdB=[" FROM post WHERE account ="+cusNo+" GROUP BY "," ORDER BY "] }
    cusNoPostCntSortSQLCmd = ["SELECT COUNT(*) as cnt,"," FROM post WHERE account = "+cusNo+" GROUP BY "," ORDER BY cnt desc, "]

    # 加入 cusNoPostCntSortCmdA
    for cusNoPostCntSortCmdA in cusNoPostCntSortSQLCmd:
        cusNoPostCntSortA+=cusNoPostCntSortCmdA
        cnt=0
        # print(cusNoPostCntSortA)

        # 插入arrTableCol欄位於 cusNoPostCntSortCmdA & cusNoPostCntSortCmdB 之中
        for cusNoPostCntSortCmd01 in arrTableCol:
            cnt+=1
            cusNoPostCntSortA+=cusNoPostCntSortCmd01
            if cnt>=len(arrTableCol):
                break
            cusNoPostCntSortA+=","

    # 列印出(SELECT COUNT(*) as cnt,styleNo,accessoriesNo,clothesNo,coatNo,pantsNo,shoesNo FROM post WHERE account =64 GROUP BY styleNo,accessoriesNo,clothesNo,coatNo,pantsNo,shoesNo ORDER BY styleNo,accessoriesNo,clothesNo,coatNo,pantsNo,shoesNo)
    # print(cusNoPostCntSortA)

    # DB.(2/3 A) 判斷 MyDB 是否有原有輸出檔案存在
    # filePathMyDB = "DataAnalysisResult/analysisResultMyDB.csv"
    # if os.path.isfile(filePathMyDB):
    #     os.remove(filePathMyDB)

    # DB.(2/3 B) 判斷 241DB 是否有原有輸出檔案存在
    filePath241DB = "DataAnalysisResult/analysisResult241DB.csv"
    if os.path.isfile(filePath241DB):
        os.remove(filePath241DB)

    # 抓取且執行 cusNoPostCntSortA 查詢結果 = arrPersonalRow
    for arrPersonalRow in cursorToList.cursorToList(cusNoPostCntSortA):
        cusNoPostCntSortB=""
        # print(arrPersonalRow)

        # 轉換成同一欄位
        for PersonalRow in range(len(arrPersonalRow)):
            cusNoPostCntSortB+=arrPersonalRow[PersonalRow]+","
            # print(cusNoPostCntSortB)

        print(arrPersonalRow)
        cusNoPostCntSortB+=" 比例:"+str(int(arrPersonalRow[0])/sum)

        # print(type(str(arrPersonalRow)))
        # cursorToList.cursor.execute("INSERT INTO dbo.postcount(id, count, styleNo, accessoriesNo, clothesNo, coatNo, pantsNo, shoesNo) VALUES("+cusNo+","+str(arrPersonalRow).split(',')+")")

        # 列印出每一種可能及比例
        print(cusNoPostCntSortB)

        # DB.(3/3 A) 將 DB-MyDB 分析結果寫成檔案
        # with open('DataAnalysisResult/analysisResultMyDB.csv',"a",encoding='UTF-8') as printFile:
        #     printFile.write(cusNoPostCntSortB+"\n")

        # DB.(3/3 B) 將 DB-241DB 分析結果寫成檔案
        with open('DataAnalysisResult/analysisResult241DB.csv',"a",encoding='BIG5') as printFile:
            printFile.write(cusNoPostCntSortB+"\n")

    print("\n"+"-"*80+"\n")

    with open('DataAnalysisResult/analysisResult241DB.csv', "r", encoding='BIG5') as file:
        reader = csv.reader(file)
        # postDataAnalysisCmd = 'INSERT INTO postcount({0}) VALUES ({1})'
        # postDataAnalysisCmd = postDataAnalysisCmd.format(','.join(reader), ','.join('?' * len(reader)))
        # cursorToList.iWearDB.cursor()
        for postDataAnalysisDataRow in reader:
            postDataAnalysisDataString=cusNo
            for postDataAnalysisDataSQLCmd in postDataAnalysisDataRow:
                postDataAnalysisDataString = postDataAnalysisDataString+" ,'" +postDataAnalysisDataSQLCmd+ "'"
            postDataAnalysisDataSQLCmd = "INSERT INTO postcount(id, [count], styleNo, accessoriesNo, clothesNo, coatNo, pantsNo, shoesNo, note) VALUES("+postDataAnalysisDataString+");"
            print("postDataAnalysisDataSQLCmd: ",postDataAnalysisDataSQLCmd)

    print("\n"+"="*80+"\n")

getPossible(socketLoginChecker.socketLoginChecker())

def getCusNoOwnPostJieba(cusNo):

    cusNoPostContextSQLCmd = ("SELECT word FROM post WHERE account = "+cusNo+"")
    # print(cusNoPostContextSQLCmd)

    for cusNoPostContext in cursorToList.cursorToList(cusNoPostContextSQLCmd):
        # print(str(cusNoPostContext))
        MyJieba_hant.MyJieba_hant(str(cusNoPostContext))

getCusNoOwnPostJieba("62")

# # 檢查是否已登入 iWear 平台 (需連結Django測試)
# loginResult = loginChecker.loginChecker()
# if loginResult[0]=="verified":
#     getPossible(loginResult[1])
#
# def getCusNoOthersPostJieba(cusNo):
#
#     # 將資料庫其他使用者既有貼文抓出
#     cursorToList.cursor.execute("SELECT * 0FROM post WHERE account!="+cusNo+"")
#     allPost = cursorToList.cursor.fetchall()
#
#     # 依優先順序顯示貼文
#     print(allPost)

# getCusNoOthersPostJieba("64")


