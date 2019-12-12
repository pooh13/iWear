import os, csv, iWearFunction, analysisSQL, testOnly.test01
from datetime import datetime

class MyException(Exception):
  def __init__(self, value):
    self.value = value

account = str(iWearFunction.socketLoginChecker())
account = account.strip("b").strip("'")
print(account)

listPercent=[0.3,0.1,0.15,0.15,0.15,0.15]

# 把所有種類抓出來
arrTable=['style','accessories','clothes','coat','pants','shoes']
arrTableCol=['styleNo','accessoriesNo','clothesNo','coatNo','pantsNo','shoesNo']
arrAllRow=[]
# e.x. ---[[ST01,ST02],[PA01,PA02]] [[ST01,ST02,ST03],[PA01,PA02,PA03]]

for table in arrTable:
    tableSQLCmd = ("SELECT * FROM "+table+";")
    arrTableCols=[]

    for cols in iWearFunction.cursorToList(tableSQLCmd):
        arrTableCols.append(cols[0])
    arrAllRow.append(arrTableCols)


def getPossible(cusNo):

    userLoginDatetimeSQLCmd = iWearFunction.cursorGFetch("SELECT CONVERT(varchar(100), last_login, 20) FROM auth_user where id = "+cusNo+";")

    userLoginDatetime = datetime.strptime(userLoginDatetimeSQLCmd[0][0], "%Y-%m-%d %H:%M:%S")

    print(userLoginDatetime)

    if userLoginDatetime < datetime.now():
        print("datetime is true")

    # ---開始此使用者貼文比例處裡統計---

    sum=0

    findCusNoSQLCmd = ("SELECT COUNT(*) as cnt FROM post WHERE account = "+cusNo+";")

    for cusNoPostCnt in iWearFunction.cursorToList(findCusNoSQLCmd):
        sum=int(cusNoPostCnt[0])

    # 尋找user每一種可能的比例
    cusNoPostCntSortA=""

    # e.x. { cusNoPostCntSortCmdA=["SELECT COUNT(*) as cnt,"] } { cusNoPostCntSortCmd01=[,] }
    # e.x. { cusNoPostCntSortCmdB=[" FROM post WHERE account ="+cusNo+" GROUP BY "," ORDER BY "] }
    cusNoPostCntSortSQLCmd = ["SELECT COUNT(*) as cnt,"," FROM post WHERE account = "+cusNo+" GROUP BY "," ORDER BY cnt desc, "]

    # 加入 cusNoPostCntSortCmdA
    for cusNoPostCntSortCmdA in cusNoPostCntSortSQLCmd:
        cusNoPostCntSortA+=cusNoPostCntSortCmdA
        cnt=0

        # 插入arrTableCol欄位於 cusNoPostCntSortCmdA & cusNoPostCntSortCmdB 之中
        for cusNoPostCntSortCmd01 in arrTableCol:
            cnt+=1
            cusNoPostCntSortA+=cusNoPostCntSortCmd01

            if cnt>=len(arrTableCol):
                break
            cusNoPostCntSortA+=","

    # 列印出(SELECT COUNT(*) as cnt,styleNo,accessoriesNo,clothesNo,coatNo,pantsNo,shoesNo FROM post WHERE account =64 GROUP BY styleNo,accessoriesNo,clothesNo,coatNo,pantsNo,shoesNo ORDER BY styleNo,accessoriesNo,clothesNo,coatNo,pantsNo,shoesNo)
    # print(cusNoPostCntSortA)

    print("\n"+"---getPossible/已完成此使用者貼文比例處理統計---"+"\n"+"-"*30+"\n")

    # ---判斷原始檔案是否存在---

    # DB.(2/3 A) 判斷 MyDB 是否有原有輸出檔案存在
    # filePathMyDB = "DataAnalysisResult/analysisResultMyDB.csv"
    # if os.path.isfile(filePathMyDB):
    #     os.remove(filePathMyDB)

    # DB.(2/3 B) 判斷 241DB 是否有原有輸出檔案存在
    filePath241DB = "DataAnalysisResult/analysisResult241DB.csv"
    if os.path.isfile(filePath241DB):
        os.remove(filePath241DB)

    print("\n"+"---getPossible/已完成存在檔案檢查並重建CSV---"+"\n"+"-"*30+"\n")

    # ---資料庫資料更新前先刪除此使用者先前貼文分析---

    deleteViewSQLCmd = ("DELETE FROM postAnalysisView WHERE id="+cusNo+"")
    iWearFunction.cursorGInsert(deleteViewSQLCmd)
    print(deleteViewSQLCmd)

    print("\n"+"---getPossible/已完成資料庫資料更新前先刪除此使用者先前貼文分析---"+"\n"+"-"*30+"\n")

    # ---產生使用者貼文比例分析結果---

    # 抓取且執行 cusNoPostCntSortA 查詢結果 = arrPersonalRow
    for arrPersonalRow in iWearFunction.cursorToList(cusNoPostCntSortA):
        cusNoPostCntSortB=""
        # print(arrPersonalRow)

        # 轉換成同一欄位
        for PersonalRow in range(len(arrPersonalRow)):
            cusNoPostCntSortB+=arrPersonalRow[PersonalRow]+","
            # print(cusNoPostCntSortB)

        # print(arrPersonalRow)
        cusNoPostCntSortB+=" 比例:"+str(int(arrPersonalRow[0])/sum)

        # 列印出每一種可能及比例
        print(cusNoPostCntSortB)

        # ---分析結果寫成CSV---

        # DB.(3/3 A) 將 DB-MyDB 分析結果寫成檔案
        # with open('DataAnalysisResult/analysisResultMyDB.csv',"a",encoding='UTF-8') as printFile:
        #     printFile.write(cusNoPostCntSortB+"\n")

        # DB.(3/3 B) 將 DB-241DB 分析結果寫成檔案
        with open('DataAnalysisResult/analysisResult241DB.csv',"a",encoding='BIG5') as printFile:
            printFile.write(cusNoPostCntSortB+"\n")


        print("\n"+"---getPossible/已完成此筆分析結果寫入檔案---"+"\n"+"-"*30+"\n")

    print("\n"+"---getPossible/已完成全部分析結果寫入檔案---"+"\n"+"-"*30+"\n")
    print("\n"+"===getPossibleCSV==="+"\n"+"-"*50+"\n")

    # ---將分析結果寫入資料庫---

    # ---資料庫資料更新前先刪除先前貼文分析---

    determineCusNoSQLCmd = "DELETE FROM postcount WHERE id = "+cusNo+""
    iWearFunction.cursorGInsert(determineCusNoSQLCmd)

    print("\n"+"---getPossible/已完成資料庫資料更新前先刪除先前貼文分析---"+"\n"+"-"*30+"\n")

    # ---以檔案將使用者貼文分析結果寫入資料庫---

    with open('DataAnalysisResult/analysisResult241DB.csv', "r", encoding='BIG5') as file:
        reader = csv.reader(file)
        print(type(reader))

        for column in reader:
            insertSQLCmd = ("INSERT INTO postCount VALUES(")
            column = list(column)
            column.insert(1, cusNo)

            for toString in column:
                insertSQLCmd+="'"+toString+"',"
            insertSQLCmd = (insertSQLCmd[:len(insertSQLCmd)-1]+');')

            print(insertSQLCmd)
            iWearFunction.cursorGInsert(insertSQLCmd)

    print("\n"+"---getPossible/已完成將使用者貼文分析結果寫入資料庫---"+"\n"+"-"*30+"\n")
    print("\n"+"===getPossibleInsertDB==="+"\n"+"-"*50+"\n")

    # ---開始此使用者貼文與其他使用者貼文分析和此使用者相同或相似貼文---

    delCusNoSQLCmd = "DELETE FROM postAnalysisView WHERE id != "+cusNo+""
    iWearFunction.cursorGInsert(delCusNoSQLCmd)

    insertAnalysisRequest = iWearFunction.cursorGFetch(analysisSQL.allSearchSQLCmd+"AND account!="+cusNo+";" + analysisSQL.orACSearchSQLCmd+"AND account!="+cusNo+";" + analysisSQL.orCOSearchSQLCmd+"AND account!="+cusNo+";" + analysisSQL.orSHSearchSQLCmd+"AND account!="+cusNo+";" + analysisSQL.orPASearchSQLCmd+"AND account!="+cusNo+";" + analysisSQL.orACCOSearchSQLCmd+"AND account!="+cusNo+";" + analysisSQL.orACCOSHSearchSQLCmd+"AND account!="+cusNo+";" + analysisSQL.orACCOSHPASearchSQLCmd + "AND account!="+cusNo+";")
    print(insertAnalysisRequest)

    print("\n"+"---getPossible/已完成此使用者貼文與其他使用者貼文分析和此使用者相同或相似貼文---"+"\n"+"-"*30+"\n")

    # ---將此使用者分析結果寫回資料庫---

    for row in insertAnalysisRequest:
        insertAnalysisRequestSQLCmd = ("INSERT INTO postAnalysisView VALUES(")

        # (73898, 62, '108510', 'photos/1511257878-3051391331.jpg', datetime.datetime(2019, 5, 27, 8, 24, 18, 483000), '照片測試2', 'ST01', 'AC01', 'CL01', 'CO01', 'PA01', 'SH01')
        row[4]=row[4].strftime('%Y-%m-%d %H:%M:%S')

        row=list(row)
        row.append(cusNo)

        for toString in row:
            toString=str(toString)
            insertAnalysisRequestSQLCmd+="'"+toString+"',"
        insertAnalysisRequestSQLCmd = insertAnalysisRequestSQLCmd[:len(insertAnalysisRequestSQLCmd)-1]+");"
        print("insertAnalysisRequestSQLCmd: "+insertAnalysisRequestSQLCmd)

        iWearFunction.cursorGInsert(insertAnalysisRequestSQLCmd)

    print("\n"+"---getPossible/已完成此使用者分析結果寫回資料庫---"+"\n"+"-"*30+"\n")
    print("\n"+"---getPossibleInsertAnalysisFinish---"+"\n"+"-"*50+"\n")
    print("\n"+"===getPossibleFinish==="+"\n"+"="*80+"\n")

print("\\"*100+"\ngetPossibleEND\n"+"/"*100+"\n"*3)


def getCusNoOwnPostJieba(cusNo):

    cusNoPostContextSQLCmd = ("SELECT word FROM post WHERE account = "+cusNo+"")
    # print(cusNoPostContextSQLCmd)

    # ---判斷原始檔案是否存在---

    # DB.(2-1/3 A) 判斷 MyDB 是否有原有輸出檔案存在
    # filePathMyDB = "DataAnalysisResult/userSentenceResult241DB.csv"
    # if os.path.isfile(filePathMyDB):
    #     os.remove(filePathMyDB)

    # DB.(2-1/3 B) 判斷 241DB 是否有原有輸出檔案存在
    filePath241DB = "DataAnalysisResult/userSentenceResult241DB.csv"
    if os.path.isfile(filePath241DB):
        os.remove(filePath241DB)

    print("\n"+"---已完成存在檔案檢查並重建CSV---"+"\n"+"-"*30+"\n")

    # ---開始此使用者貼文文字內容處裡統計---

    for cusNoPostContext in iWearFunction.cursorToList(cusNoPostContextSQLCmd):
        # print(str(cusNoPostContext))
        JiebaResult = str(iWearFunction.MyJieba_hant(str(cusNoPostContext)))
        print(type(JiebaResult))
        print(JiebaResult)

        # JiebaResult = cusNo+","+JiebaResult
        # print(type(JiebaResult))
        # print(JiebaResult)

        print("\n"+"---getCusNoOwnPostJieba/已完成此使用者貼文文字內容處裡統計---"+"\n"+"-"*30+"\n")

        # ---分析結果寫成CSV---

        # DB.(3-1/3 A) 將 DB-MyDB 分析結果寫成檔案
        # with open('DataAnalysisResult/userSentenceResultMyDB.csv',"a",encoding='UTF-8') as printFile:
        #     printFile.write(cusNoPostCntSortB+"\n")

        # DB.(3-1/3 B) 將 DB-241DB 分析結果寫成檔案
        with open('DataAnalysisResult/userSentenceResult241DB.csv',"a",encoding='BIG5') as printFile:
            printFile.write(JiebaResult+"\n")

        print("\n"+"---getCusNoOwnPostJieba/已完成此筆分析結果寫入檔案---"+"\n"+"-"*30+"\n")

    print("\n"+"---getCusNoOwnPostJieba/已完成全部分析結果寫入檔案---"+"\n"+"-"*30+"\n")
    print("\n"+"===getCusNoOwnPostJiebaCSV==="+"\n"+"-"*50+"\n")

    # ---將分析結果寫入資料庫---

    # ---資料庫資料更新前先刪除先前貼文分析---

    determineCusNoSQLCmd = ("DELETE FROM userSentenceCount WHERE account = "+cusNo+"")
    iWearFunction.cursorGInsert(determineCusNoSQLCmd)

    print("\n"+"---getCusNoOwnPostJieba/已完成資料庫資料更新前先刪除先前貼文分析---"+"\n"+"-"*30+"\n")

    # ---以檔案將使用者貼文分析結果寫入資料庫---

    with open('DataAnalysisResult/userSentenceResult241DB.csv', "r", encoding='BIG5') as file:
        reader = csv.reader(file)

        for column in reader:
            insertSQLCmd = ("INSERT INTO userSentenceCount VALUES(")
            column=list(column)
            column.insert(0,cusNo)

            for addCusNo in column:
                insertSQLCmd+="'"+addCusNo+"',"
            insertSQLCmd = insertSQLCmd[:len(insertSQLCmd)-1]+');'

            print(insertSQLCmd)
            iWearFunction.cursorGInsert(insertSQLCmd)

    print("\n"+"---getCusNoOwnPostJieba/已完成將使用者貼文分析結果寫入資料庫---"+"\n"+"-"*30+"\n")
    print("\n"+"===getCusNoOwnPostJiebaInsertDB==="+"\n"+"-"*50+"\n")

    # ---開始此使用者貼文與其他使用者貼文分析和此使用者有關聯文章---

    delCusNoSQLCmd = "DELETE FROM webAndUserSentenceAnalysis WHERE ownAccount != "+cusNo+""
    iWearFunction.cursorGInsert(delCusNoSQLCmd)

    insertAnalysisRequest = iWearFunction.cursorGFetch(analysisSQL.sentenceAnalysisSQLCmd)
    print(insertAnalysisRequest)

    print("\n"+"---getCusNoOwnPostJieba/已完成此使用者貼文與其他使用者貼文分析和此使用者有關聯文章---"+"\n"+"-"*30+"\n")

    # # ---將此使用者分析結果寫回資料庫---
    #
    for row in insertAnalysisRequest:
        insertAnalysisRequestSQLCmd = ("INSERT INTO webAndUserSentenceAnalysis VALUES(")

        row=list(row)
        row.append(cusNo)

        for toString in row:
            toString=str(toString)
            insertAnalysisRequestSQLCmd+="'"+toString+"',"
        insertAnalysisRequestSQLCmd = insertAnalysisRequestSQLCmd[:len(insertAnalysisRequestSQLCmd)-1]+");"
        print("insertAnalysisRequestSQLCmd: "+insertAnalysisRequestSQLCmd)

        iWearFunction.cursorGInsert(insertAnalysisRequestSQLCmd)

    print("\n"+"---getCusNoOwnPostJieba/已完成此使用者分析結果寫回資料庫---"+"\n"+"-"*30+"\n")
    print("\n"+"---getCusNoOwnPostJieba---"+"\n"+"-"*50+"\n")
    print("\n"+"===getCusNoOwnPostJiebaFinish==="+"\n"+"="*80+"\n")

# while True:
#     try:
#         getPossible(account)
#         # getPossible("109")
#         getCusNoOwnPostJieba(account)
#         # getCusNoOwnPostJieba("109")
#
#         break
#
#     except MyException as e:
#         if e.value == "restart":
#             continue

getPossible(account)
# getPossible("109")
getCusNoOwnPostJieba(account)
# getCusNoOwnPostJieba("109")
