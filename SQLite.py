import sqlite3 as sql

def SQL_init():
    global cursor, dataBase
    dataBase = sql.connect("./DataBase.db")
    cursor = dataBase.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS site_pass(ID integer PRIMARY KEY,
                       SiteName nvarchar(20) NOT NULL UNIQUE,
                       Password nvarchar(64) NOT NULL,
                       MethodCreate nvarchar(15))""")

def SQL_close():
    cursor.close()
    dataBase.close()
    return 0



def SQL_insert(site_name, password, method):
    _data = [site_name, password, method]
    cursor.execute("""INSERT INTO site_pass (SiteName, Password, MethodCreate) 
                      VALUES(?, ?, ?)""", _data)
    dataBase.commit()
    return 0


def SQL_select_one(site_name):
    cursor.execute("""SELECT Password
                   FROM site_pass
                   WHERE SiteName = '{}'""".format(site_name))
    data = cursor.fetchall()
    password = data[0][0] if data != [] else None
    return password

def SQL_update_one(site_old, site_new, password, method):
    cursor.execute("""UPDATE site_pass
                   SET SiteName = '{}', Password = '{}', MethodCreate = '{}'
                   WHERE SiteName = '{}'""".format(site_new, password, method, site_old))
    return 0

def SQL_select_all():
    cursor.execute("""SELECT SiteName, Password
                   FROM site_pass
                   ORDER BY SiteName
                   """)
    data = dict(cursor.fetchall())
    return data
