import SQLServerDBLink

# DB.(1/3 A) SQLServerDBLinkMyDB
# iWearDB = SQLServerDBLink.SQLServerDBLinkMyDB()

# DB.(1/3 B) SQLServerDBLink241DB
iWearDB = SQLServerDBLink.SQLServerDBLink241DB()
cursor = iWearDB.cursor()

def cursorG(cursorGResult):
    cursor.execute(cursorGResult)
    cursorGResult = cursor.fetchall()
    return cursorGResult
