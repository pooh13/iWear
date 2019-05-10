import pyodbc
def SQLServerDBLink(iWear):
    iWear = pyodbc.connect(
        'DRIVER={SQL Server}; SERVER=140.131.114.241,1433; DATABASE=108-510; UID=108iwear; PWD=@108iwear',
        ENGINE = "sql_server.pyodbc",
        NAME= "108-510",
        HOST="140.131.114.241",
        USER="108iwear",
        PASSWORD="@108iwear",
    )
