import toList
import SQLServerDBLink

# DB.(1/3 A) SQLServerDBLinkMyDB
# iWearDB = SQLServerDBLink.SQLServerDBLinkMyDB()

# DB.(1/3 B) SQLServerDBLink241DB
iWearDB = SQLServerDBLink.SQLServerDBLink241DB()
cursor = iWearDB.cursor()

def cursorToList(cursorToListResult):
    cursor.execute(cursorToListResult)
    cursorToListResult = cursor.fetchall()
    cursorToList = toList.toList(cursorToListResult)
    return cursorToList


