from flask import Flask, json, request, Response, jsonify, redirect, url_for, Response;
import time
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
from threading import Thread
import threading
import logging
from datetime import date


####################/////////////////////////-------->>>
from classes.redis      import redis_server
from classes.movida     import MOVIDA
from error.error_data   import ERROR_DATA
from classes.hinova     import HINOVA
from classes.pagamentos     import PAGAMENTOS
from classes.conexa     import CONEXA
from classes.infornet   import INFORNET
from classes.logs       import log_api
####################/////////////////////////-------->>>




####################/////////////////////////-------->>>

ERROR      = ERROR_DATA()
hinova_    = HINOVA()
pagamentos_= PAGAMENTOS()
conexa_    = CONEXA()
infornet_  = INFORNET()
movidaData = MOVIDA()
r          = redis_server
redis      = r.URI()

####################/////////////////////////-------->>>





####################/////////////////////////-------->>>
LOGS_BY_SYSTEM  =  log_api()
####################/////////////////////////-------->>>


####################/////////////////////////-------->>>
url = os.environ.get('URL')
GOOGLE = os.environ.get('GOOGLE')
IP = os.environ.get('IP')
USUARIO = os.environ.get('USUARIO')
PASS = os.environ.get('PASS')
DB = os.environ.get('DB')
DB_TRACCAR = os.environ.get('DB_TRACCAR')
####################/////////////////////////-------->>>


####################/////////////////////////-------->>>REDIS CONFIG

api = Flask(__name__)
#api.config.from_object('config.ConfigRedis')

####################/////////////////////////-------->>>REDIS CONFIG



SWAGGER_URL = '/swagger'
API_URL = '/spec'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "api_simovsat"
    }
)


####################/////////////////////////-------->>>
####################/////////////////////////-------->>>
@api.route('/spec')
def swagger():
    with open('swagger.json', 'r') as f:
        return jsonify(json.load(f))

api.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
####################/////////////////////////-------->>>
####################/////////////////////////-------->>>



@api.route('/')

def index():
   try:
      return jsonify({

         "status": True,
         "/spec"                         : "swagger version api",
         "/movida_generate_link/<placa>" : "GENERATE LINK WITH MAP",
         "/movida_cerca"                 : "CERCA",
         "/movida_result/<placa>"        : "GET LOCATION USER BY PLATE",
         "/usuarios_importadas"          : "GET USERS IMPORTED",
         "/veiculos_importados"          : "GET VEHICLES IMPORTED",
         "/veiculos_cooperativa/ativos/<codigo_cooperativa>"         : "GET VEHICLES /ATIVOS BY COOPERATIVA ID",
         "/veiculos_regional/ativos/<codigo_regional>"               : "GET VEHICLES /ATIVOS BY REGIONAL ID",
         "/veiculos_situacao/ativos/<codigo_situaca>"                : "GET VEHICLES /ATIVOS BY SITUACAO ID",

         "/veiculos_cooperativa/inadimplentes/<codigo_cooperativa>"  : "GET VEHICLES /INADIMPLENTES BY COOPERATIVA ID",
         "/veiculos_regional/inadimplentes/<codigo_regional>"        : "GET VEHICLES /INADIMPLENTES BY REGIONAL ID",
         "/veiculos_situacao/inadimplentes/<codigo_situaca>"         : "GET VEHICLES /INADIMPLENTES BY SITUACAO ID",

         "/veiculos_cooperativa/inativos/<codigo_cooperativa>"       : "GET VEHICLES /INATIVOS BY COOPERATIVA ID",
         "/veiculos_regional/inativos/<codigo_regional>"             : "GET VEHICLES /INATIVOS BY REGIONAL ID",
         "/veiculos_situacao/inativos/<codigo_situaca>"              : "GET VEHICLES /INATIVOS BY SITUACAO ID",

         "/regionais_todas"              : "GET REGIONAIS",
         "/cooperativas_todas"           : "GET COOPERATIVAS",
         "/voluntarios_todas"            : "GET VOLUNTARIOS",
         "/produtos_todas"               : "GET PRODUTOS",
         "/situacao_todas"               : "GET SITUAÇÕES",
         "/placas_inativos/<placa>"      : "GET PLATES INATIVOS SIMOVSAT",
         "/placas_inativos_hinova/<placa>" :  "GET PLATES INATIVOS HINOVA",
         "/placas_inadimplentes/<placa>" :    "GET PLATES INA. SIMOVSAT",
         "/placas_inadimplentes_hinova/<placa>" : "GET PLATES INA. HINOVA",
         "/placas_ativas/<placa>"        : "GET ACTIVE PLATES SIMOVSAT",
         "/placas_ativas_hinova/<placa>" : "GET ACTIVE PLATES HINOVA",
         "/hinova_result/<uid>"          : "GET RESULTS HINOVA",
         "/usuarios"                     : "POST USERS TO IMPORT",
         "/veiculos_filter"              : "POST VEHICLES WITH FILTER",
         "/veiculos_filter_import"       : "POST VEHICLES TO IMPORT WITH FILTER",
         "/situacao"                     : "POST TO GENERATE SITUATIONS",
         "/produto"                      : "POST TO GENERATE PRODUTOS",
         "/voluntarios"                  : "POST TO GENERATE VOLUNTARIOS",
         "/cooperativa"                  : "POST TO GENERATE COOPERATIVAS",
         "/regionais"                    : "POST TO GENERATE REGIONAIS",
         "/pacientes"                    : "POST TO CONEXAAPP",
         "/boletos"                      : "POST TO BOLETOS",
         "profile":"JESUS É FIEL",
         "developer":"GLEISON SILVEIRA DE FREITAS"
      })
   except Exception:
      error = {
       "status":"Failed"
      }


################### MOVIDA GERANOD LINK DE ASSISTENCIA
################### MOVIDA GERANOD LINK DE ASSISTENCIA


@api.route('/movida_generate_link/<placa>', methods=['GET'])
def generate_link(placa):

   try:

     ##  TREADINGS

     t = threading.Thread(target=movidaData.gerar_link, args=(placa,))
     t.start()

     data = {
      "placa": placa,
      "status": True,
      "link":"https://simovsat.com.br/sharing/" + placa + "",
      "result": "processado"
     }

     #######LOGS//////////////////
     formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
     LOGS_BY_SYSTEM.LOGSYS("logs/data.log", formatLOG , str(data), logging.INFO)
     #######LOGS//////////////////

     return jsonify(data)  
   except:
      out = ERROR.movida_link(placa)
      return jsonify(out), 200  

################### MOVIDA GERANOD LINK DE ASSISTENCIA
################### MOVIDA GERANOD LINK DE ASSISTENCIA




################### MOVIDA CERCA
################### MOVIDA CERCA

@api.route('/movida_cerca', methods=['POST'])
def cerca():
   
         
    #parameters = request.form.to_dict(flat=False)
    #lat = parameters['result']
    #long = parameters['total']


    ##  TREADINGS

    #callback_data = function_call.callback_Users(data, total ,slices)
    
    #json_callback = json.dumps(callback_data)

    ##  TREADINGS
    
    data = { "endpoint":"em andamento", "status": True}

    #redis.set("users", json.dumps(json_callback))
    return jsonify(data)
  
    
################### MOVIDA CERCA
################### MOVIDA CERCA
  

################### MOVIDA LOCAL DO USUARIO
################### MOVIDA LOCAL DO USUARIO


@api.route('/movida_result/<placa>', methods=['GET'])

def webhook(placa):
    
    try: 
      data  = json.loads(redis.get(placa))

      lat_  = data["tracker"]["latitude"]
      long_ = data["tracker"]["longitude"]

    
      lat_  = str(lat_)
      long_ = str(long_)


      result_lat_long = lat_ + "," + long_

      address = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng=' + result_lat_long  + '&key=' + GOOGLE)


      result_= json.loads(address.text)
      rua    = result_["results"][0]["address_components"][1]["long_name"]
      numero = result_["results"][0]["address_components"][0]["long_name"] 
      bairro = result_["results"][0]["address_components"][2]["long_name"]
      cidade = result_["results"][0]["address_components"][3]["long_name"]
      estado = result_["results"][0]["address_components"][4]["long_name"]
      pais   = result_["results"][0]["address_components"][5]["long_name"]
      cep    = result_["results"][0]["address_components"][6]["long_name"]

      endereco = rua + "," + numero + "," + bairro  + "," + estado + "," + cidade + "," + pais + "," + cep
      

      
      data_result =  {

        "status":True,
        "rastreador": data["tracker"],
        "usuario":data["user"],
        "veiculo":data["vehicle"],
        "local":{
          "endereco":endereco,
          "rua":rua,
          "numero":numero,
          "bairro":bairro,
          "cidade":cidade,
          "estado":estado,
          "pais":pais,
          "cep":cep
        }

      }
          
      #######LOGS//////////////////
      formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
      LOGS_BY_SYSTEM.LOGSYS("logs/data.log", formatLOG , str(data_result), logging.INFO)
      #######LOGS//////////////////

      return jsonify(data_result), 200
   
    except:
      out = ERROR.movida_locations(placa)
      return jsonify(out), 200



################### MOVIDA LOCAL DO USUARIO
################### MOVIDA LOCAL DO USUARIO




################### CONSULTA DE BOLETOS
################### CONSULTA DE BOLETOS

@api.route('/boletos/<cpf>/<marketing>', methods=['GET'])
def boletosbycpf(cpf,marketing):
    print("OK")
    try: 
      # data = json.loads(redis.get("historico_boletos"))
      t = threading.Thread(target=pagamentos_.boletos, args=(cpf,marketing))
      t.start()
    
      
      data_result =  {

        "status":True,
        "data": data,

      }

      return jsonify(data_result), 200

    except:
      out = ERROR.boletoserror(cpf)
      return jsonify(out), 200


################### CONSULTA DE BOLETOS
################### CONSULTA DE BOLETOS




################### PLACAS USUARIOS IMPORTADOS CONSULTA
################### PLACAS USUARIOS IMPORTADOS CONSULTA

@api.route('/usuarios_importadas', methods=['GET'])
def usuarios_importadas():
    

    try: 
      data = json.loads(redis.get("usuarios_importados"))
      
      data_result =  {

        "status":True,
        "data": data,

      }

      return jsonify(data_result), 200

    except:
      out = ERROR.usuarios_importados()
      return jsonify(out), 200

################### PLACAS USUARIOS IMPORTADOS CONSULTA
################### PLACAS USUARIOS IMPORTADOS CONSULTA



################### PLACAS VEICULOS POR REGIONAL
################### PLACAS VEICULOS POR REGIONAL

@api.route('/veiculos_regional/ativos/<codigo_regional>', methods=['GET'])

def veiculos_regional_ativos(codigo_regional):
    
    try: 
      data = json.loads(redis.get("ativos_regional" + str(codigo_regional)))
      
      data_result =  {

        "status":True,
        "data": data,

      }

      return jsonify(data_result), 200

    except:
      out = ERROR.consulta_veiculos()
      return jsonify(out), 200



@api.route('/veiculos_regional/inadimplentes/<codigo_regional>', methods=['GET'])

def veiculos_regional_inadimplentes(codigo_regional):
    
    try: 
      data = json.loads(redis.get("inadimplentes_regional" + str(codigo_regional)))
      
      data_result =  {

        "status":True,
        "data": data,

      }

      return jsonify(data_result), 200

    except:
      out = ERROR.consulta_veiculos()
      return jsonify(out), 200



@api.route('/veiculos_regional/inativos/<codigo_regional>', methods=['GET'])

def veiculos_regional_inativos(codigo_regional):
    
    try: 
      data = json.loads(redis.get("inativos_regional" + str(codigo_regional)))
      
      data_result =  {

        "status":True,
        "data": data,

      }

      return jsonify(data_result), 200

    except:
      out = ERROR.consulta_veiculos()
      return jsonify(out), 200



################### PLACAS VEICULOS POR REGIONAL
################### PLACAS VEICULOS POR REGIONAL







################### PLACAS VEICULOS POR SITUACAO
################### PLACAS VEICULOS POR SITUACAO

@api.route('/veiculos_situacao/ativos/<codigo_situacao>', methods=['GET'])

def veiculos_situacao_ativos(codigo_situacao):
    
    try: 
      data = json.loads(redis.get("ativos_situacao" + str(codigo_situacao)))
      
      data_result =  {

        "status":True,
        "data": data,

      }

      return jsonify(data_result), 200

    except:
      out = ERROR.consulta_veiculos()
      return jsonify(out), 200



@api.route('/veiculos_situacao/inadimplentes/<codigo_situacao>', methods=['GET'])

def veiculos_situacao_inadimplentes(codigo_situacao):
    
    try: 
      data = json.loads(redis.get("inadimplentes_situacao" + str(codigo_situacao)))
      
      data_result =  {

        "status":True,
        "data": data,

      }

      return jsonify(data_result), 200

    except:
      out = ERROR.consulta_veiculos()
      return jsonify(out), 200





@api.route('/veiculos_situacao/inativos/<codigo_situacao>', methods=['GET'])

def veiculos_situacao_inativos(codigo_situacao):
    
    try: 
      data = json.loads(redis.get("inativos_situacao" + str(codigo_situacao)))
      
      data_result =  {

        "status":True,
        "data": data,

      }

      return jsonify(data_result), 200

    except:
      out = ERROR.consulta_veiculos()
      return jsonify(out), 200


################### PLACAS VEICULOS POR SITUACAO
################### PLACAS VEICULOS POR SITUACAO





################### PLACAS VEICULOS POR COOPERATIVA ID
################### PLACAS VEICULOS POR COOPERATIVA ID

@api.route('/veiculos_cooperativa/ativos/<codigo_cooperativa>', methods=['GET'])

def veiculos_cooperativa_ativos(codigo_cooperativa):
    
    try: 
      data = json.loads(redis.get("ativos_cooperativas" + str(codigo_cooperativa)))
      
      data_result =  {

        "status":True,
        "data": data,

      }

      return jsonify(data_result), 200

    except:
      out = ERROR.consulta_veiculos()
      return jsonify(out), 200



@api.route('/veiculos_cooperativa/inadimplentes/<codigo_cooperativa>', methods=['GET'])

def veiculos_cooperativa_inadimplentes(codigo_cooperativa):
    
    try: 
      data = json.loads(redis.get("inadimplentes_cooperativas" + str(codigo_cooperativa)))
      
      data_result =  {

        "status":True,
        "data": data,

      }

      return jsonify(data_result), 200

    except:
      out = ERROR.consulta_veiculos()
      return jsonify(out), 200



@api.route('/veiculos_cooperativa/inativos/<codigo_cooperativa>', methods=['GET'])

def veiculos_cooperativa_inativos(codigo_cooperativa):
    
    try: 
      data = json.loads(redis.get("inativos_cooperativas" + str(codigo_cooperativa)))
      
      data_result =  {

        "status":True,
        "data": data,

      }

      return jsonify(data_result), 200

    except:
      out = ERROR.consulta_veiculos()
      return jsonify(out), 200





################### PLACAS VEICULOS POR COOPERATIVA ID
################### PLACAS VEICULOS POR COOPERATIVA ID



################### PLACAS VEICULOS IMPORTADOS CONSULTA
################### PLACAS VEICULOS IMPORTADOS CONSULTA


@api.route('/veiculos_importados', methods=['GET'])
def veiculos_importadas():
    
    try: 
      data = json.loads(redis.get("veiculos_importados"))
      
      data_result =  {

        "status":True,
        "data": data,

      }

      return jsonify(data_result), 200

    except:
      out = ERROR.veiculos_importados()
      return jsonify(out), 200


################### PLACAS VEICULOS IMPORTADOS CONSULTA
################### PLACAS VEICULOS IMPORTADOS CONSULTA



################### PLACAS REGIONAIS CONSULTA
################### PLACAS REGIONAIS CONSULTA

@api.route('/regionais_todas', methods=['GET'])
def regionais_todas():


    try: 

      data = json.loads(redis.get("regionais_todas"))
      
      data_result =  {

        "status":True,
        "data": data,

      }

      return jsonify(data_result), 200 

    except:
      out = ERROR.regionais()
      return jsonify(out), 200

################### PLACAS REGIONAIS CONSULTA
################### PLACAS REGIONAIS CONSULTA


################### PLACAS COOPERATIVAS  CONSULTA
################### PLACAS COOPERATIVAS  CONSULTA

@api.route('/cooperativas_todas', methods=['GET'])
def cooperativas_todas():
    
    try:
        
      data = json.loads(redis.get("cooperativas_todas"))
      
      data_result =  {

        "status":True,
        "data": data,

      }

      return jsonify(data_result), 200  

    except:
      out = ERROR.cooperativas()
      return jsonify(out), 200

################### PLACAS COOPERATIVAS  CONSULTA
################### PLACAS COOPERATIVAS  CONSULTA


################### PLACAS VOLUNTARIOS CONSULTA
################### PLACAS VOLUNTARIOS CONSULTA

@api.route('/voluntarios_todas', methods=['GET'])
def voluntarios_todas():
    
    try:
      data = json.loads(redis.get("voluntarios_todas"))
      
      data_result =  {

        "status":True,
        "data": data,

      }

      return jsonify(data_result), 200    
    except: 
      out = ERROR.voluntarios()
      return jsonify(out), 200
################### PLACAS VOLUNTARIOS CONSULTA
################### PLACAS VOLUNTARIOS CONSULTA




################### PLACAS PRODUTOSCONSULTA
################### PLACAS PRODUTOSCONSULTA

@api.route('/produtos_todas', methods=['GET'])
def produtos_todas():
    
    try:
      data = json.loads(redis.get("produtos_todas"))
      
      data_result =  {

        "status":True,
        "data": data,

      }

      return jsonify(data_result), 200  
    except:
      
      out = ERROR.produtos()
      return jsonify(out), 200

################### PLACAS PRODUTOSCONSULTA
################### PLACAS PRODUTOSCONSULTA


@api.route('/situacao_todas', methods=['GET'])
def situacao_todas():
    
    try: 
      data = json.loads(redis.get("situacao_todas"))
      
      data_result =  {

        "status":True,
        "data": data,

      }

      return jsonify(data_result), 200  

    except:
      
      out = ERROR.situacao()
      return jsonify(out), 200






################### PLACAS INADIMPLENTES DA SIMOVSAT CONSULTA
################### PLACAS INADIMPLENTES DA SIMOVSAT CONSULTA


@api.route('/placas_inadimplentes/<placa>', methods=['GET'])
def placas_inadimplentes(placa):
    
    try:
      data = json.loads(redis.get("inadimplentes_" + str(placa)))
      
      data_result =  {

        "status":True,
        "data": data,

      }

      return jsonify(data_result), 200


    except:
      out = ERROR.inadimplentes_simovsat(placa)
      return jsonify(out), 200

################### PLACAS INADIMPLENTES DA SIMOVSAT CONSULTA
################### PLACAS INADIMPLENTES DA SIMOVSAT CONSULTA


################### PLACAS INADIMPLENTES DA HINOVA CONSULTA
################### PLACAS INADIMPLENTES DA HINOVA CONSULTA

@api.route('/placas_inadimplentes_hinova/<placa>', methods=['GET'])
def placas_inadimplentes_hinova(placa):
     
    try: 

      data = json.loads(redis.get("inadimplentes_hinova" + str(placa)))
      
      data_result =  {

        "status":True,
        "data": data,

      }

      return jsonify(data_result), 200

    except:
      out = ERROR.inadimplentes_hinova(placa)
      return jsonify(out), 200


################### PLACAS INADIMPLENTES DA HINOVA CONSULTA
################### PLACAS INADIMPLENTES DA HINOVA CONSULTA



################### PLACAS INATIVOS DA SIMOVSAT CONSULTA
################### PLACAS INATIVOS  DA SIMOVSAT CONSULTA


@api.route('/placas_inativos/<placa>', methods=['GET'])
def placas_inativos(placa):
    
    try:
      data = json.loads(redis.get("inativos_" + str(placa)))
      
      data_result =  {

        "status":True,
        "data": data,

      }

      return jsonify(data_result), 200


    except:
      out = ERROR.inadimplentes_simovsat(placa)
      return jsonify(out), 200

################### PLACAS INATIVOS  DA SIMOVSAT CONSULTA
################### PLACAS INATIVOS  DA SIMOVSAT CONSULTA



################### PLACAS INATIVOS  DA HINOVA CONSULTA
################### PLACAS INATIVOS  DA HINOVA CONSULTA

@api.route('/placas_inativos_hinova/<placa>', methods=['GET'])
def placas_inativos_hinova(placa):
     
    try: 

      data = json.loads(redis.get("inativos_hinova" + str(placa)))
      
      data_result =  {

        "status":True,
        "data": data,

      }

      return jsonify(data_result), 200

    except:
      out = ERROR.inadimplentes_hinova(placa)
      return jsonify(out), 200


################### PLACAS INADIMPLENTES DA HINOVA CONSULTA
################### PLACAS INADIMPLENTES DA HINOVA CONSULTA








################### PLACAS ATIVAS DA SIMOVSAT CONSULTA
################### PLACAS ATIVAS DA SIMOVSAT CONSULTA
################### PLACAS ATIVAS DA SIMOVSAT CONSULTA

@api.route('/placas_ativas/<placa>', methods=['GET'])
def placas_ativas(placa):
    
    try: 
      data = json.loads(redis.get("ativas_" + str(placa)))
      
      data_result =  {

        "status":True,
        "data": data,

      }

      return jsonify(data_result), 200
    
    except:

      out = ERROR.ativos_simovsat(placa)
      return jsonify(out), 200



################### PLACAS ATIVAS DA SIMOVSAT CONSULTA
################### PLACAS ATIVAS DA SIMOVSAT CONSULTA
################### PLACAS ATIVAS DA SIMOVSAT CONSULTA







################### PLACAS ATIVAS DA HINOVA CONSULTA
################### PLACAS ATIVAS DA HINOVA CONSULTA
################### PLACAS ATIVAS DA HINOVA CONSULTA


@api.route('/placas_ativas_hinova/<placa>', methods=['GET'])
def placas_ativas_hinova(placa):
    
    try: 

      data = json.loads(redis.get("ativas_hinova" + str(placa)))
      
      data_result =  {

        "status":True,
        "data": data,

      }

      return jsonify(data_result), 200

    except:

      out = ERROR.ativos_hinova(placa)
      return jsonify(out), 200



################### PLACAS ATIVAS DA HINOVA CONSULTA
################### PLACAS ATIVAS DA HINOVA CONSULTA
################### PLACAS ATIVAS DA HINOVA CONSULTA









###############ENDPOINT HINOVA
###############
@api.route('/hinova_result/<uid>', methods=['GET'])

def hinova(uid):

    data = json.loads(redis.get(uid))
    
    data_result =  {

      "status":True,
      "data": data,
      "requests_methods":{
        "users":"/hinova_result/users",
        "situation":"/hinova_result/situation",
        "vehicles":"/hinova_result/vehicles",
        "last_result":"/hinova_result/last_result",
      }

    }
    #######LOGS//////////////////
    formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    LOGS_BY_SYSTEM.LOGSYS("logs/data.log", formatLOG , str(data_result), logging.INFO)
    #######LOGS//////////////////

    return jsonify(data_result), 200
###############ENDPOINT HINOVA
###############






###############ENDPOINT PEGA TODOS OS USUARIOS SEM FILTRO
###############

@api.route('/usuarios', methods=['POST'])
def usuarios():

  try: 
    params = request.get_json(force=True)
    
    codigo_situacao = params["codigo_situacao"]
    inicio_paginacao = params["inicio_paginacao"]
    quantidade_por_pagina = params["quantidade_por_pagina"]
    data_inicio = params['data_inicio']
    data_fim = params['data_fim']
    total = params["total"]
    
    t = threading.Thread(target=hinova_.usuarios, args=(codigo_situacao, inicio_paginacao, quantidade_por_pagina, total, data_inicio, data_fim,))
    t.start()
    
    data_return = {

        "status":True,
        "process": "OK",
        "result": url + "hinova_result/users"
        
    }
    
    #######LOGS//////////////////
    formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    LOGS_BY_SYSTEM.LOGSYS("logs/data.log", formatLOG , str(data_return), logging.INFO)
    #######LOGS//////////////////
    
    return jsonify(data_return), 200

  except:

      out = ERROR.usuarios_post()
      return jsonify(out), 200

###############ENDPOINT PEGA TODOS OS USUARIOS SEM FILTRO
###############




###############ENDPOINT PEGA TODOS OS VEICULOS COM FILTRO
###############
@api.route('/veiculos_filter', methods=['POST'])
def veiculos_filter():

  try: 
    params = request.get_json(force=True)

    codigo_situacao = params["codigo_situacao"]
    inicio_paginacao = params["inicio_paginacao"]
    quantidade_por_pagina = params["quantidade_por_pagina"]
    data_inicio = params['data_inicio']
    data_fim = params['data_fim']
    codigo_regional = params['codigo_regional']
    codigo_cooperativa = params['codigo_cooperativa']
    codigo_tipo_veiculo = params['codigo_tipo_veiculo']
    valor_fipe = params['valor_fipe']
    cilindrada = params['cilindrada']


  

    t = threading.Thread(target=hinova_.veiculos_filter, args=(codigo_situacao, inicio_paginacao, quantidade_por_pagina, codigo_regional, codigo_cooperativa, codigo_tipo_veiculo, valor_fipe, cilindrada, data_inicio, data_fim))
    t.start()
    
    data_return = {

        "status":True,
        "process": "OK",
        "result": url + "hinova_result/vehicles"
        
    }

    #######LOGS//////////////////
    formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    LOGS_BY_SYSTEM.LOGSYS("logs/data.log", formatLOG , str(data_return), logging.INFO)
    #######LOGS//////////////////

    return jsonify(data_return),200
    
  except:  
    out = ERROR.veiculos_filter_post()
    return jsonify(out), 200  

###############ENDPOINT PEGA TODOS OS VEICULOS COM FILTRO
###############



###############ENDPOINT IMPORTAR TODAS OS VEICULOS COM FILTRO
###############

@api.route('/veiculos_filter_import', methods=['POST'])
def veiculos_filter_import():

  try: 
    params = request.get_json(force=True)

    codigo_situacao = params["codigo_situacao"]
    inicio_paginacao = params["inicio_paginacao"]
    quantidade_por_pagina = params["quantidade_por_pagina"]
    data_inicio = params['data_inicio']
    data_fim = params['data_fim']
    codigo_regional = params['codigo_regional']
    codigo_cooperativa = params['codigo_cooperativa']
    codigo_tipo_veiculo = params['codigo_tipo_veiculo']
    valor_fipe = params['valor_fipe']
    cilindrada = params['cilindrada']


  

    t = threading.Thread(target=hinova_.veiculos_filter_import_data, args=(codigo_situacao, inicio_paginacao, quantidade_por_pagina, codigo_regional, codigo_cooperativa, codigo_tipo_veiculo, valor_fipe, cilindrada, data_inicio, data_fim))
    t.start()
    
    data_return = {

        "status":True,
        "process": "OK",
        "result": url + "hinova_result/vehicles"
        
    }
    #redis
    #redis.set(str(uid), json.dumps(result))
    #requests.post(url_callback, data=result)  ## use callback to call return in another function

    #######LOGS//////////////////
    formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    LOGS_BY_SYSTEM.LOGSYS("logs/data.log", formatLOG , str(data_return), logging.INFO)
    #######LOGS//////////////////

    return jsonify(data_return),200

  except:  
    out = ERROR.veiculos_filter_import_post()
    return jsonify(out), 200  

###############ENDPOINT IMPORTAR TODAS OS VEICULOS COM FILTRO
###############






###############ENDPOINT PEGA TODAS AS SITUAÇÕES
###############
@api.route('/situacao', methods=['POST'])
def situacao():

  try: 
    params = request.get_json(force=True)



    t = threading.Thread(target=hinova_.situacao, args=())
    t.start()
    
    data_return = {

        "status":True,
        "process": "OK",
        
    }
    #redis
    #redis.set(str(uid), json.dumps(result))
    #requests.post(url_callback, data=result)  ## use callback to call return in another function

    #######LOGS//////////////////
    formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    LOGS_BY_SYSTEM.LOGSYS("logs/data.log", formatLOG , str(data_return), logging.INFO)
    #######LOGS//////////////////

    return jsonify(data_return),200

  except:  
    out = ERROR.situacao_post()
    return jsonify(out), 200  
###############ENDPOINT PEGA TODAS OS PRODUTOS
###############






#########////////////////////







###############ENDPOINT PEGA TODAS OS PRODUTOS
###############
@api.route('/produto', methods=['POST'])
def produto():

  try:
    params = request.get_json(force=True)

    codigo_regional = params["codigo_regional"]
    codigo_cooperativa = params["codigo_cooperativa"]
    codigo_tipo_veiculo = params["codigo_tipo_veiculo"]
    valor_fipe  = params["valor_fipe"]
    cilindrada  = params["cilindrada"]
    

    t = threading.Thread(target=hinova_.produto, args=(codigo_regional, codigo_cooperativa, codigo_tipo_veiculo, valor_fipe, cilindrada, ))
    t.start()
    
    data_return = {

        "status":True,
        "process": "OK",
        
    }
    #redis
    #redis.set(str(uid), json.dumps(result))
    #requests.post(url_callback, data=result)  ## use callback to call return in another function

    #######LOGS//////////////////
    formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    LOGS_BY_SYSTEM.LOGSYS("logs/data.log", formatLOG , str(data_return), logging.INFO)
    #######LOGS//////////////////

    return jsonify(data_return),200

  except:  
    out = ERROR.produto_post()
    return jsonify(out), 200  

###############ENDPOINT PEGA TODAS OS PRODUTOS
###############







##################/////////////////







###############ENDPOINT PEGA TODAS OS VOLUNTARIOS
###############
@api.route('/voluntarios', methods=['POST'])
def voluntario():

  try:
      
    params = request.get_json(force=True)


    t = threading.Thread(target=hinova_.voluntario, args=())
    t.start()
    
    data_return = {

        "status":True,
        "process": "OK",
        
    }
    #redis
    #redis.set(str(uid), json.dumps(result))
    #requests.post(url_callback, data=result)  ## use callback to call return in another function


    #######LOGS//////////////////
    formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    LOGS_BY_SYSTEM.LOGSYS("logs/data.log", formatLOG , str(data_return), logging.INFO)
    #######LOGS//////////////////


    return jsonify(data_return),200
  except:

    out = ERROR.voluntarios_post()
    return jsonify(out), 200  
###############ENDPOINT PEGA TODAS OS VOLUNTARIOS
###############






#############////////////////////






###############ENDPOINT PEGA TODAS AS COOPERATIVAS
###############
@api.route('/cooperativa', methods=['POST'])
def cooperativa():

  
  try: 
    params = request.get_json(force=True)


    t = threading.Thread(target=hinova_.cooperativa, args=())
    t.start()
    
    data_return = {

        "status":True,
        "process": "OK",
        
    }
    #redis
    #redis.set(str(uid), json.dumps(result))
    #requests.post(url_callback, data=result)  ## use callback to call return in another function


    #######LOGS//////////////////
    formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    LOGS_BY_SYSTEM.LOGSYS("logs/data.log", formatLOG , str(data_return), logging.INFO)
    #######LOGS//////////////////


    return jsonify(data_return),200
  except:

    out = ERROR.cooperativa_post()
    return jsonify(out), 200  
###############ENDPOINT PEGA TODAS AS COOPERATIVAS
###############





########/////////////////////////////




###############ENDPOINT PEGA TODAS AS REGIONAIS
###############
@api.route('/regionais', methods=['POST'])
def regionais():

  try: 
    params = request.get_json(force=True)

   

    t = threading.Thread(target=hinova_.regionais, args=())
    t.start()
    
    data_return = {

        "status":True,
        "process": "OK",
        
    }
    #redis
    #redis.set(str(uid), json.dumps(result))
    #requests.post(url_callback, data=result)  ## use callback to call return in another function


    #######LOGS//////////////////
    formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    LOGS_BY_SYSTEM.LOGSYS("logs/data.log", formatLOG , str(data_return), logging.INFO)
    #######LOGS//////////////////


    return jsonify(data_return),200
  except:
      out = ERROR.regionais_post()
      return jsonify(out), 200  
###############ENDPOINT PEGA TODAS AS REGIONAIS
###############



###############ENDPOINT CADASTRAR NOVO PACIENTE
###############
@api.route('/pacientes', methods=['POST'])
def pacientes():

  try: 
    params = request.get_json(force=True)

    name                = params["name"]
    dia                 = params["dia"]
    mes                 = params["mes"]
    ano                 = params["ano"]
    cpf                 = params["cpf"]
    agenda              = params["agenda"]
    especialidade       = params["especialidade"]
    telefone            = params["telefone"]
    
    LOGPATH = "./logs/conexa.log"
    DATENOW = date.today()

    if (len(ano) > 3 and  len(name) > 2 and len(cpf) > 10 ):
        
        ## READY DOCUMENT FOR SEE IF DATA EXISTE
        with open(LOGPATH) as file:   
            
            ## OPEN DOCUMENT 
            if str(DATENOW) in str(file.read()): 

                # IF EXISTE DATA COMPARE AND WAIT ONE DAY  
                print("WAIT TIME....") 
                time.sleep(4.32e+7)
                print("CADASTRANDO PACIENTE")

                dates = dia +"/" + mes + "/"+ ano     
                t    = threading.Thread(target=conexa_.pacientes, args=(name, dates, cpf, agenda, especialidade, telefone, ))
                t.start()
                
                data_return = {

                    "status":True,
                    "process": "ok",
                    "name": name,
                    "cpf":  cpf,
                    "nascimento": dates,
                    "agenda":agenda,
                    "especialidade":especialidade,
                    "telefone":telefone

                }
                
                
                #######LOGS//////////////////
                formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
                LOGS_BY_SYSTEM.LOGSYS("logs/conexa.log", formatLOG , str(data_return), logging.INFO)
                #######LOGS//////////////////


                return jsonify(data_return),200

            else:
                # IF NOT EXISTE DATA EXECTE 
                dates = dia +"/" + mes + "/"+ ano     
                t    = threading.Thread(target=conexa_.pacientes, args=(name, dates, cpf, agenda, especialidade, telefone, ))
                t.start()
                
                data_return = {

                    "status":True,
                    "process": "ok",
                    "name": name,
                    "cpf":  cpf,
                    "nascimento": dates,
                    "agenda":agenda,
                    "especialidade":especialidade,
                    "telefone":telefone

                }
                
                
                #######LOGS//////////////////
                formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
                LOGS_BY_SYSTEM.LOGSYS("logs/conexa.log", formatLOG , str(data_return), logging.INFO)
                #######LOGS//////////////////


                return jsonify(data_return),200
        
    else:
        
        data_returnERROR = {

            "status":True,
            "process": "failed",

        }
        
        
        #######LOGS//////////////////
        formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        LOGS_BY_SYSTEM.LOGSYS("logs/data.log", formatLOG , str(data_return), logging.INFO)
        #######LOGS//////////////////


        return jsonify(data_returnERROR),200
    #redis
    #redis.set(str(uid), json.dumps(result))
    #requests.post(url_callback, data=result)  ## use callback to call return in another function




  except:
      return 'error'

###############ENDPOINT CADASTRAR NOVO PACIENTE
###############





###############ENDPOINT CADASTRAR NOVO PACIENTE
###############
@api.route('/infornet', methods=['POST'])
def infornetUsers():

  try: 
    params = request.get_json(force=True)

    cnpj                  = params["cnpj"]

    t    = threading.Thread(target=infornet_.infornet, args=(cnpj, ))
    t.start()
    
    data_return = {

        "status":True,
        "process": "ok",
        "login": login,
        "senha": senha
    }

    #######LOGS//////////////////
    formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    LOGS_BY_SYSTEM.LOGSYS("logs/conexa.log", formatLOG , str(data_return), logging.INFO)
    #######LOGS//////////////////

    return jsonify(data_return),200

  except:
      return 'error'

###############ENDPOINT CADASTRAR NOVO PACIENTE
###############




MAX_TIMEOUT = 900000
if __name__ == '__main__':
    threading.TIMEOUT_MAX
    socket.setdefaulttimeout(999999999)
    api.run(debug=True, host="0.0.0.0") 