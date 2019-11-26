from django.db import connections, connection,transaction

def ExecuteSql(sql,db='default'):
    """
    执行SQL
    """
    if sql is None or sql == "":
        return

    cursor = connections[db].cursor()
    cursor.execute(sql)
    transaction.commit_unless_managed(using=db)
    cursor.close()
    return True


def SelectAllSql(sql,db='default'):
    """
    查询SQL多条数据
    """
    if sql is None or sql == "":
        return

    cursor = connections[db].cursor()
    cursor.execute(sql)
    fetchall = cursor.fetchall()
    cursor.close()
    return fetchall


def SelectAllSqlByColumns(sql,columns,db='default'):
    """
    查询SQL多条数据并返回字典结果集
    """
    if sql is None or sql == "":
        return

    cursor = connections[db].cursor()
    cursor.execute(sql)
    fetchall = cursor.fetchall()
    object_list = []
    if fetchall:
        for obj in fetchall:
            dict = {}
            for index,c in enumerate(columns):
                dict[c] = obj[index]
            object_list.append(dict)
    cursor.close()
    return object_list


def SelectOneSql(sql,db='default'):
    """
   查询SQL单条数据
    """
    if sql is None or sql == "":
        return


    cursor = connections[db].cursor()
    cursor.execute(sql)
    fetchone = cursor.fetchone()
    cursor.close()
    return fetchone


def SelectOneSqlByColumns(sql,columns,db='default'):
    """
    查询SQL单条数据并返回字典结果集
    """
    if sql is None or sql == "":
        return
    cursor = connections[db].cursor()
    cursor.execute(sql)
    fetchone = cursor.fetchone()
    object = {}
    if fetchone:
        for index, c in enumerate(columns):
            object[c] = fetchone[index]
    cursor.close()
    return object