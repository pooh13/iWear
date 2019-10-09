import MySplit
import SQLServerDBLink

# DB.(1/3 A) SQLServerDBLinkMyDB
# iWearDB = SQLServerDBLink.SQLServerDBLinkMyDB()

# DB.(1/3 B) SQLServerDBLink241DB
iWearDB = SQLServerDBLink.SQLServerDBLink241DB()

def cursorToMySplit(cursorToMySplitResult):
    cursor.execute(cursorToMySplitResult)
    cursorToMySplitResult = cursor.fetchall()
    cursorToMySplit = MySplit.MySplit(cursorToMySplitResult)
    return cursorToMySplit

cursor = iWearDB.cursor()
