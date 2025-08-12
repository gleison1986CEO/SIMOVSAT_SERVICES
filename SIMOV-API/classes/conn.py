import os
import sys
import pyodbc
import mysql.connector
from dotenv import load_dotenv


##################################
load_dotenv()

url_       = os.getenv('URL')
DRIVER     = os.getenv('DRIVER')
SERVER     = os.getenv('SERVER')
DATABASE   = os.getenv('DATABASE')
USERNAME   = os.getenv('USERNAME')
PASSWORD   = os.getenv('PASSWORD')
GOOGLE_    = os.getenv('GOOGLE')
IP_        = os.getenv('IP')
USUARIO_   = os.getenv('USUARIO')
PASS_      = os.getenv('PASS')
DB_        = os.getenv('DB')
DB_TRACCAR_= os.getenv('DB_TRACCAR')
USERLOCAL  = os.getenv('USERLOCAL')
PASSLOCAL  = os.getenv('PASSLOCAL')
IPLOCAL    = os.getenv('IPLOCAL')
##################################



class CONN:


    def teste(self):
        mydb = mysql.connector.connect(
          host=str(IP_),
          user=str(USUARIO_),
          passwd=str(PASS_),
          database=str(DB_)
        )
        return mydb
        
    def gpwrox(self):
        mydb = mysql.connector.connect(
          host=str(IP_),
          user=str(USUARIO_),
          passwd=str(PASS_),
          database=str(DB_)
        )
        return mydb

            
    def gpwrox_WEB(self):
        mydb = mysql.connector.connect(
          host=str(IP_),
          user=str(USUARIO_),
          passwd=str(PASS_),
          database=str(DB_)
        )
        return mydb    

    def traccar(self):
        mydb = mysql.connector.connect(
          host=str(IP_),
          user=str(USUARIO_),
          passwd=str(PASS_),
          database=str(DB_TRACCAR_)
        )
        return mydb

    def localhost(self):
        mydb = mysql.connector.connect(
          host=str(IPLOCAL),
          user=str(USERLOCAL),
          passwd=str(PASSLOCAL),
          database=str(DB_)
        )
        return mydb

    def sqlserver(self):
    
        server   = SERVER
        database = DATABASE
        username = USERNAME
        password = PASSWORD
        CONNECTION     = pyodbc.connect('DRIVER='+DRIVER+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password + ';Integrated Security=True;Connect Timeout=30;Trust Server Certificate=False;Application Intent=ReadWrite;ApplicationIntent=ReadWrite;TrustServerCertificate=yes;')
        cursor   = CONNECTION.cursor()
        cursor.execute("SELECT @@version;") ## GET VERSION FROM SQLSERVER

        return cursor