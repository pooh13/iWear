import pyodbc

def SQLServerDBLink241DB():
    # IP: 140.131.114.241
    return pyodbc.connect(
        'DRIVER={SQL Server}; SERVER=140.131.114.241,1433; DATABASE=108-510; UID=108iwear; PWD=@108iwear',
        ENGINE = "sql_server.pyodbc",
        NAME= "108-510",
        HOST="140.131.114.241,1433",
        USER="108iwear",
        PASSWORD="@108iwear",
    )

def SQLServerDBLinkMyDB():
    # IP: 122.116.41.151
    return pyodbc.connect(
        'DRIVER={SQL Server}; SERVER=122.116.41.151,1433; DATABASE=108-510; UID=sa; PWD=sqlserver',
        ENGINE = "sql_server.pyodbc",
        NAME= "108-510",
        HOST="220.135.161.251,1433",
        USER="sa",
        PASSWORD="sqlserver",
    )
