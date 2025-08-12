
from flask import Flask, json, request, Response, jsonify, redirect, url_for, Response;
from dotenv import load_dotenv
import time;
import requests
import redis
from flask_caching import Cache 
from threading import Thread
import traceback
import uuid
import urllib.request
import urllib
from flask_swagger_ui import get_swaggerui_blueprint
import os, sys
import os.path
import random
import re
import sys
import mysql.connector
import os, sys
import os.path
import random
import re
import sys
from threading import Thread
import threading
import datetime


## classes

from classes.redis import redis_server
from classes_jobs.data import DATA
r = redis_server
redis = r.URI()
DATA_ = DATA()


###############LOAD ENV
load_dotenv()

URL      = os.getenv('URL')
GOOGLE   = os.getenv('GOOGLE')
IP       = os.getenv('IP')
USUARIO  = os.getenv('USUARIO')
PASS     = os.getenv('PASS')
DB       = os.getenv('DB')
DB_TRACCAR = os.getenv('DB_TRACCAR')
###############LOAD ENV




class MOVIDA():
    def gerar_link(self, placa):


        database_gpwrox = mysql.connector.connect(
          host=IP,
          user=USUARIO,
          passwd=PASS,
          database=DB
        )

        database_traccar = mysql.connector.connect(
          host=IP,
          user=USUARIO,
          passwd=PASS,
          database=DB_TRACCAR
        )

        ## search by PLATE

        connectionTraccar = database_traccar.cursor()
        connectionGP = database_gpwrox.cursor()
        ###


        device_id = "SELECT * FROM devices WHERE plate_number LIKE  %s"

        adr = (placa, )

        connectionGP.execute(device_id, adr)

        resultById = connectionGP.fetchall()
        placa_ = placa
      
        id_device =  resultById[0][0]
        imei =  resultById[0][10]
        nome =  resultById[0][9]
        telefone =  resultById[0][15]
        cpf =  resultById[0][19]
        registro =  resultById[0][20]
        proprietario =  resultById[0][21]
        tabela_fipe =  resultById[0][22]
        dados_veiculo =  resultById[0][23]
        rastreador =  resultById[0][17]
        placa =  resultById[0][18]
        veiculo =  resultById[0][23]

        hash = str(placa)

        #####################
        #####################


        user_id = 1
        now = datetime.datetime.now()
        active = 1
        delete_after_expiration = 0


        sharing = """INSERT INTO sharing (user_id,name,hash,expiration_date,active,delete_after_expiration) VALUES  (%s, %s, %s, %s, %s, %s)"""
        dataSharing = [(user_id, nome,hash,None,active,0)]
        connectionGP.executemany(sharing , dataSharing)
        database_gpwrox.commit()
        id_sharing = connectionGP.lastrowid



        sharing_pivot = """INSERT INTO sharing_device_pivot (sharing_id,device_id,user_id,expiration_date,active) VALUES  (%s, %s, %s, %s, %s)"""
        dataSharing_pivot = [(id_sharing, id_device, user_id,None,active)]
        connectionGP.executemany(sharing_pivot , dataSharing_pivot)
        database_gpwrox.commit()
        id_sharings = connectionGP.lastrowid
        database_gpwrox.close()

        ###
        data = {
            "link":"https://simovsat.com.br/sharing/" + hash + "",
            "placa":placa,
            "imei":imei,
            "nome": nome,

        }

        json_callback = json.dumps(data)
        redis.set("imei", json.dumps(json_callback))

        DATA_.GENERATEFORMOVIDA(placa)
        return data


    def cercas():


        database_gpwrox = mysql.connector.connect(
          host=IP,
          user=USUARIO,
          passwd=PASS,
          database=DB
        )

        database_traccar = mysql.connector.connect(
          host=IP,
          user=USUARIO,
          passwd=PASS,
          database=DB_TRACCAR
        )

        connectionTraccar = database_traccar.cursor()
        connectionGP = database_gpwrox.cursor()

        ## Cadastro de cercas de entrada e saída + notificação de cerca rompida

        return "OK"  


