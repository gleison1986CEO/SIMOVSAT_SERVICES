import pyodbc
import time

from classes.conn   import CONN
SQLSERVER  = CONN()
cursor     = SQLSERVER.sqlserver()
cpf = "70823204260"

query   = cursor.execute("select * from dbo.ClubeUser where cpf ='" + cpf + "'")
results = query.fetchall()

if results:
    print(results)
else:
    print("NONE")