"""
	Python Database
"""
from mysql.connector import connect

def db_connect()->object:
    return connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="pydb"
    )
def getall(table:str)->list:
    sql:str = f"SELECT * FROM `(table)`"
    db:object = db_connect()
    cursor:object = db.cursor(dictionary=True)
    cursor.execute(sql)
    data:list = cursor.fetchall()
    return data
    
def getrecord(table:str,**kwargs)->dict:pass
def addrecord(table:str,**kwargs)->bool:pass
def updaterecord(table:str,**kwargs)->bool:pass
def deleterecord(table:str,**kwargs)->bool:pass

print(getall('student'))
