from flask import Flask, json, request, Response, jsonify, redirect, url_for, Response;
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
from retry import retry
import logging

#########################---------->> CLASSES
from classes.locationMovida import STA
sta = STA()

from classes.redis import redis_server
r = redis_server
redis = r.URI()

from classes.key import key_acess
generate_key = key_acess

from classes.conn import CONN
connection_mysql = CONN()
#########################---------->> CLASSES


#######################---------->>>>>
from classes.logs        import log_api
#######################---------->>>>>


###################################

url        = os.environ.get('URL')
GOOGLE     = os.environ.get('GOOGLE')
IP         =  os.environ.get('IP')
USUARIO    = os.environ.get('USUARIO')
PASS       = os.environ.get('PASS')
DB         = os.environ.get('DB')
DB_TRACCAR = os.environ.get('DB_TRACCAR')

###################################


####################/////////////////////////-------->>>
LOGS_BY_SYSTEM  =  log_api()
####################/////////////////////////-------->>>




class DATA:
   @retry(ValueError, tries=120, delay=120)
   def dataEXECUTEGET(self):

      print("INICIANDO PROCESSO DO MAPA")
      ###################################
      ###################################
      database_gpwrox  = connection_mysql.gpwrox() 
      database_traccar = connection_mysql.traccar() 
      ###################################

      connection_gp      = database_gpwrox.cursor() ## cursor mysql
      connection_traccar = database_traccar.cursor() ##cursor mysql


      query ="SELECT COUNT(*) FROM devices"
      connection_gp.execute(query)

      id_count = connection_gp.fetchall()

      result_count = str(id_count)

      replace_count = result_count.replace("[(", "")
      count_result = replace_count.replace(",)]", "")

      count = int(count_result)


      connection_gp.execute("SELECT plate_number FROM devices LIMIT " + count_result)

      result_plate = connection_gp.fetchall()

      for plate in result_plate:

         result = str(plate)  
         replace = result.replace("('", "")
         replace_ = replace.replace("',)", "")

         sql = "SELECT * FROM devices WHERE plate_number = %s ORDER BY id LIMIT " + count_result
         placa_vehicle = (str(replace_), )


         connection_gp.execute(sql, placa_vehicle)

         result = connection_gp.fetchall()
               
         id = result[0][0]
         imei = result[0][10]
         nome = result[0][9]
         telefone = result[0][15]
         cpf = result[0][19]
         registro = result[0][20]
         proprietario = result[0][21]
         tabela_fipe = result[0][22]
         dados_veiculo = result[0][23]
         rastreador = result[0][17]
         placa = result[0][18]
         veiculo = result[0][23]
         
         try: 
               sql_traccar = "SELECT * FROM devices WHERE uniqueId = %s LIMIT " + count_result
               imei_vehicle = (str(imei), )

               connection_traccar.execute(sql_traccar, imei_vehicle)

               result_traccar = connection_traccar.fetchall()


               latitude = result_traccar[0][4]
               longitude = result_traccar[0][5]
               velocidade = result_traccar[0][7] 
               date = result_traccar[0][8] 
               dateGps = result_traccar[0][9] 
               altitude = result_traccar[0][12] 
               course = result_traccar[0][13] 
               bateria = result_traccar[0][14] 
               address = result_traccar[0][15] 
               protocol = result_traccar[0][16]
               lastPosition = result_traccar[0][17] 
               vehicle_status = result_traccar[0][6]


               status = str(vehicle_status)
         
               init = status.replace("<", ",")
               init2 = init.replace(">", '":')
               init3 = init2.replace("/>", "")
               init4 = init3.replace("/", "")
               init5 = init4.replace(",", '"')


               batery        = sta.batery(init5)
               totaldistance = sta.totaldistance(init5)
               motion        = sta.motion(init5)
               ignition      = sta.ignition(init5)
               charge        = sta.charge(init5)
               blocked       = sta.blocked(init5)

               

               data = {

               "tracker":{
                  "imei": imei,
                  "rastreador": rastreador,
                  "latitude":latitude,
                  "longitude":longitude,
                  "dataGPS":dateGps, 
                  "altitude":altitude, 
                  "bateria":bateria, 
                  "protocolo":protocol,
                  "ultimaPosicao": lastPosition,
               },


               "user":{
                  "nome": nome,
                  "telefone": telefone,
                  "cpf":cpf,
                  "registro":registro,
                  "proprietario":proprietario,
                  "tabela_fipe":tabela_fipe,
                  "dados_veiculo":dados_veiculo,
         

               },
               "vehicle":{
                  "placa":placa,
                  "dados_veiculo":dados_veiculo,
                  "parametros":{
                     "batery":batery,
                     "totaldistance":totaldistance,
                     "motion":motion,
                     "ignition":ignition,
                     "charge":charge,
                     "blocked":blocked
                  },
               }

               }


               result_ = json.dumps(data)
               redis.set(str(placa), json.dumps(data))

               #######LOGS//////////////////
               formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
               LOGS_BY_SYSTEM.LOGSYS("logs/maps.log", formatLOG , str(data), logging.INFO)
               #######LOGS//////////////////
         

         except:
               raise ValueError
         



  



class DATA:
   @retry(ValueError, tries=120, delay=120)
   def GENERATEFORMOVIDA(self, plate):

      print("PROCESSO GOOGLE MAPS MOVIDA")
      ###################################
      ###################################
      database_gpwrox  = connection_mysql.gpwrox() 
      database_traccar = connection_mysql.traccar() 
      ###################################

      connection_gp      = database_gpwrox.cursor() ## cursor mysql
      connection_traccar = database_traccar.cursor() ##cursor mysql




      result = str(plate)  
      replace = result.replace("('", "")
      replace_ = replace.replace("',)", "")

      sql = "SELECT * FROM devices WHERE plate_number = %s ORDER BY id LIMIT " + count_result
      placa_vehicle = (str(replace_), )


      connection_gp.execute(sql, placa_vehicle)
      result = connection_gp.fetchall()
            
      id = result[0][0]
      imei = result[0][10]
      nome = result[0][9]
      telefone = result[0][15]
      cpf = result[0][19]
      registro = result[0][20]
      proprietario = result[0][21]
      tabela_fipe = result[0][22]
      dados_veiculo = result[0][23]
      rastreador = result[0][17]
      placa = result[0][18]
      veiculo = result[0][23]
      
      try: 

         sql_traccar = "SELECT * FROM devices WHERE uniqueId = %s LIMIT " + count_result
         imei_vehicle = (str(imei), )

         connection_traccar.execute(sql_traccar, imei_vehicle)

         result_traccar = connection_traccar.fetchall()


         latitude = result_traccar[0][4]
         longitude = result_traccar[0][5]
         velocidade = result_traccar[0][7] 
         date = result_traccar[0][8] 
         dateGps = result_traccar[0][9] 
         altitude = result_traccar[0][12] 
         course = result_traccar[0][13] 
         bateria = result_traccar[0][14] 
         address = result_traccar[0][15] 
         protocol = result_traccar[0][16]
         lastPosition = result_traccar[0][17] 
         vehicle_status = result_traccar[0][6]


         status = str(vehicle_status)
   
         init = status.replace("<", ",")
         init2 = init.replace(">", '":')
         init3 = init2.replace("/>", "")
         init4 = init3.replace("/", "")
         init5 = init4.replace(",", '"')


         batery        = sta.batery(init5)
         totaldistance = sta.totaldistance(init5)
         motion        = sta.motion(init5)
         ignition      = sta.ignition(init5)
         charge        = sta.charge(init5)
         blocked       = sta.blocked(init5)

         

         data = {

         "tracker":{
            "imei": imei,
            "rastreador": rastreador,
            "latitude":latitude,
            "longitude":longitude,
            "dataGPS":dateGps, 
            "altitude":altitude, 
            "bateria":bateria, 
            "protocolo":protocol,
            "ultimaPosicao": lastPosition,
         },


         "user":{
            "nome": nome,
            "telefone": telefone,
            "cpf":cpf,
            "registro":registro,
            "proprietario":proprietario,
            "tabela_fipe":tabela_fipe,
            "dados_veiculo":dados_veiculo,
   

         },
         "vehicle":{
            "placa":placa,
            "dados_veiculo":dados_veiculo,
            "parametros":{
               "batery":batery,
               "totaldistance":totaldistance,
               "motion":motion,
               "ignition":ignition,
               "charge":charge,
               "blocked":blocked
            },
         }

         }


         result_ = json.dumps(data)
         redis.set(str(placa), json.dumps(data))

         #######LOGS//////////////////
         formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
         LOGS_BY_SYSTEM.LOGSYS("logs/maps.log", formatLOG , str(data), logging.INFO)
         #######LOGS//////////////////
         print("FINALIZANDO PROCESSO")
      

      except:
            raise ValueError
         



  