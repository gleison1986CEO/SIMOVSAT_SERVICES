import pyodbc
import time

from classes.conn   import CONN
SQLSERVER  = CONN()
cursor     = SQLSERVER.sqlserver()

class QUERY:


    def CONEXABYCPF(self, cpf):

        query   = cursor.execute("select * from dbo.ConexaUser where cpf ='" + cpf + "'")
        results = query.fetchall()
        
        if results:
           return  results 
        else:
           return "None" 



    def CLUBEBYCPF(self, cpf):

        query   = cursor.execute("select * from dbo.ClubeUser where cpf ='" + cpf + "'")
        results = query.fetchall()

        if results:
            return results 
        else:
           return "None"  



    def CONEXA(self):
        query   = cursor.execute("select * from dbo.ConexaUser")
        results = query.fetchall()

        if results:
            return  results 
        else:
           return "None" 
       


    def CLUBE(self):

        query   = cursor.execute("select * from dbo.ClubeUser")
        results = query.fetchall()
        
        if results:
            return  results 
        else:
           return "None"     