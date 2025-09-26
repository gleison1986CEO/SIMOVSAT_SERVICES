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
from datetime import date
import os, sys
import os.path
import random
import re
import sys
import logging
import redis

#######################---------->>>>>

from classes.redis         import redis_server
from classes.logs          import log_api
from repository.insert     import SQLSERVER
from classes.save          import DATA_SAVE
from classes.pagamentos    import PAGAMENTOS



#######################---------->>>>>

####################/////////////////////////-------->>>
LOGS_BY_SYSTEM  =  log_api()
database_       =  SQLSERVER()
R               =  redis_server
redis           =  R.URI()
pagamentos_     =  PAGAMENTOS()

####################/////////////////////////-------->>>


SAVE    = DATA_SAVE()
DATENOW = date.today().strftime('%Y-%m-%d')

class TRATAMENTO():
      




    def boletos(self, params, data_inicio, data_fim):
 
      i = 0
      data_out = []
      
      data_inicio = str(data_inicio)
      data_fim = str(data_fim)
      total = params["total_associados"]
      
      ####### REDIS SAVE
      redis.set("usuarios_importados", json.dumps(params))
      ####### REDIS SAVE

      while i <= int(total):
       
        try: 

              data = params['associados']
              data_cadastro_associado = data[i]['data_cadastro_associado']
              
          
              if data_inicio < data_cadastro_associado and data_fim > data_cadastro_associado:

                 codigo_associado = data[i]['codigo_associado']
                 rg_associado = data[i]['rg_associado']
                 data_expedicao_rg = data[i]['data_expedicao_rg']
                 orgao_expedidor_rg = data[i]['orgao_expedidor_rg']
                 data_nascimento = data[i]['data_nascimento']
                 sexo = data[i]['sexo']
                 cnh = data[i]['cnh']
                 categoria_cnh = data[i]['categoria_cnh']
                 logradouro = data[i]['logradouro']
                 numero = data[i]['numero']
                 complemento = data[i]['complemento']
                 bairro = data[i]['bairro']
                 cidade = data[i]['cidade']
                 estado = data[i]['estado']
                 cep = data[i]['cep']
                 email = data[i]['email']
                 email_auxiliar = data[i]['email_auxiliar']
                 user = data[i]['nome']
                 phone = data[i]['telefone']
                 ddd = data[i]['ddd']
                 telefone = ddd+phone ## telefone
                 cellphone = data[i]['telefone_celular']
                 ddd_cell = data[i]['ddd_celular']
                 whastapp = ddd_cell + cellphone ## whastapp
                 cpf = data[i]['cpf']
                 data_cadastro_associado = data[i]['data_cadastro_associado']
                 data_contrato_associado = data[i]['data_contrato_associado']
                 hora_contrato_associado = data[i]['hora_contrato_associado']
                 
                 is_email                      =  SAVE.get_email(email,user)              ### GPWROX

                 
                 data = {  
                     
                     "number"             : i,
                     "codigo_associado"   : codigo_associado,
                     "rg_associado"       : rg_associado,
                     "email"              : email,
                     "whastapp"           : whastapp,
                     "cpf"                : cpf,
                     "rg"                 : rg_associado,
                     "associado"          : user,
                     "cnh"                : cnh
                 }  
                 
                 out = {  
                     
                     "number"             : i,
                     "codigo_associado"   : codigo_associado,
                     "rg_associado"       : rg_associado,
                     "email"              : email,
                     "whastapp"           : whastapp,
                     "cpf"                : cpf,
                     "rg"                 : rg_associado,
                     "associado"          : user,
                     "cnh"                : cnh
                 }  
                 

                                         
                 print("PAGAMENTOS")
                 ### PAGAMENTOS METODOS
                
                 time.sleep(10)
                 pagamentos_.boletos(cpf, whastapp)
                 
                 ### PAGAMENTOS METODOS

                 if is_email is None:
                        
                        
                        print("NÃO EXISTE  " + is_email)
                        #####LOGS//////////////////
                        situation = { "situacao": "HINOVA"}
                        formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
                        LOGS_BY_SYSTEM.LOGSYS("logs/usuarios/inexistentes/usuarios.log", formatLOG , str(data) + str(situation) , logging.INFO)
                        #######LOGS//////////////////

                        
                        #######SAVE ANALISES ON DATABASE SQLSERVER/////////
                        print("SALVANDO HISTÓRICO")
                        database_.HISTORICO(cpf, "HINOVA", str(out), str(DATENOW), 1)

                        print("SALVANDO DADOS")
                        database_.USERS("HINOVA",codigo_associado, cpf, rg_associado, email, whastapp, cnh, str(out))
                        #######SAVE ANALISES ON DATABASE SQLSERVER/////////
                
                        
                        
                 else:
                        
                        print("EXISTE:: " + is_email)
                        #######LOGS//////////////////
                        situation = { "situacao": "SIMOVSAT"}
                        #######SAVE ANALISES ON DATABASE SQLSERVER/////////
                        
                       
                        print("SALVANDO HISTÓRICO")
                        database_.HISTORICO(cpf, "SIMOVSAT", str(out), str(DATENOW), 1)
                        
                        print("SALVANDO DADOS")
                        database_.USERS("SIMOVSAT",codigo_associado, cpf, rg_associado, email, whastapp, cnh, str(out))
                        #######SAVE ANALISES ON DATABASE SQLSERVER/////////
                        

                        formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
                        LOGS_BY_SYSTEM.LOGSYS("logs/usuarios/existentes/usuarios.log", formatLOG , str(data) + str(situation) , logging.INFO)
                        #######LOGS//////////////////
              


        except:
           pass


        i += 1
      return  "OK" 


    def usuarios(self, params, data_inicio, data_fim):
 
      i = 0
      data_out = []
      
      data_inicio = str(data_inicio)
      data_fim = str(data_fim)
      total = params["total_associados"]
      
      ####### REDIS SAVE
      redis.set("usuarios_importados", json.dumps(params))
      ####### REDIS SAVE

      while i <= int(total):
       
        try: 

              data = params['associados']
              data_cadastro_associado = data[i]['data_cadastro_associado']
              
          
              if data_inicio < data_cadastro_associado and data_fim > data_cadastro_associado:

                 codigo_associado = data[i]['codigo_associado']
                 rg_associado = data[i]['rg_associado']
                 data_expedicao_rg = data[i]['data_expedicao_rg']
                 orgao_expedidor_rg = data[i]['orgao_expedidor_rg']
                 data_nascimento = data[i]['data_nascimento']
                 sexo = data[i]['sexo']
                 cnh = data[i]['cnh']
                 categoria_cnh = data[i]['categoria_cnh']
                 logradouro = data[i]['logradouro']
                 numero = data[i]['numero']
                 complemento = data[i]['complemento']
                 bairro = data[i]['bairro']
                 cidade = data[i]['cidade']
                 estado = data[i]['estado']
                 cep = data[i]['cep']
                 email = data[i]['email']
                 email_auxiliar = data[i]['email_auxiliar']
                 user = data[i]['nome']
                 phone = data[i]['telefone']
                 ddd = data[i]['ddd']
                 telefone = ddd+phone ## telefone
                 cellphone = data[i]['telefone_celular']
                 ddd_cell = data[i]['ddd_celular']
                 whastapp = ddd_cell + cellphone ## whastapp
                 cpf = data[i]['cpf']
                 data_cadastro_associado = data[i]['data_cadastro_associado']
                 data_contrato_associado = data[i]['data_contrato_associado']
                 hora_contrato_associado = data[i]['hora_contrato_associado']
                 
                 is_email                      =  SAVE.get_email(email,user)              ### GPWROX


                 data = {  
                     
                     "number"             : i,
                     "codigo_associado"   : codigo_associado,
                     "rg_associado"       : rg_associado,
                     "email"              : email,
                     "whastapp"           : whastapp,
                     "cpf"                : cpf,
                     "rg"                 : rg_associado,
                     "associado"          : user,
                     "cnh"                : cnh
                 }  
                 

                 out = {  
                     
                     "number"             : i,
                     "codigo_associado"   : codigo_associado,
                     "rg_associado"       : rg_associado,
                     "email"              : email,
                     "whastapp"           : whastapp,
                     "cpf"                : cpf,
                     "rg"                 : rg_associado,
                     "associado"          : user,
                     "cnh"                : cnh
                 }  
                                                    


                 if is_email is None:
                        
                        
                        print("NÃO EXISTE  " + is_email)
                        #####LOGS//////////////////
                        situation = { "situacao": "HINOVA"}
                        formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
                        LOGS_BY_SYSTEM.LOGSYS("logs/usuarios/inexistentes/usuarios.log", formatLOG , str(data) + str(situation) , logging.INFO)
                        #######LOGS//////////////////

                        #######SAVE ANALISES ON DATABASE SQLSERVER/////////
                        print("SALVANDO HISTÓRICO")
                        database_.HISTORICO(cpf, "HINOVA", str(out), str(DATENOW), 1)

                        print("SALVANDO DADOS")
                        database_.USERS("HINOVA",codigo_associado, cpf, rg_associado, email, whastapp, cnh, str(out))
                        #######SAVE ANALISES ON DATABASE SQLSERVER/////////
                        

                        ###### SAVE ON MYSQL SIMOVSAT
                        SAVE.usuarios(codigo_associado, rg_associado, data_expedicao_rg, orgao_expedidor_rg, data_nascimento, sexo, cnh, categoria_cnh, logradouro, numero, complemento, bairro, cidade, estado, cep, email, email_auxiliar, user, telefone, whastapp, cpf, data_cadastro_associado, data_contrato_associado, hora_contrato_associado)
                        ###### SAVE ON MYSQL SIMOVSAT
                        
                        print("SALVANDO USUARIUOS")
                        
                        
                 else:
                        
                        print("EXISTE:: " + is_email)
                        #######LOGS//////////////////
                        situation = { "situacao": "SIMOVSAT"}
                        #######SAVE ANALISES ON DATABASE SQLSERVER/////////
                        
                       
                        print("SALVANDO HISTÓRICO")
                        database_.HISTORICO(cpf, "SIMOVSAT", str(out), str(DATENOW), 1)
                        
                        print("SALVANDO DADOS")
                        database_.USERS("SIMOVSAT",codigo_associado, cpf, rg_associado, email, whastapp, cnh, str(out))
                        #######SAVE ANALISES ON DATABASE SQLSERVER/////////
                        

                        formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
                        LOGS_BY_SYSTEM.LOGSYS("logs/usuarios/existentes/usuarios.log", formatLOG , str(data) + str(situation) , logging.INFO)
                        #######LOGS//////////////////
              


        except:
           pass


        i += 1
      return  "OK" 



    def veiculos_filter(self, params, codigo_situacao, veiculo, produto, codigo_cooperativa, cooperativa, codigo_regional, data_inicio, data_fim):
      


      ############### SAVE DATA ON CONSULTING DATABASE HINOVA
      
      if    codigo_situacao == "1":

            redis.set("ativos_cooperativas" + str(codigo_cooperativa), json.dumps(veiculo))
            redis.set("ativos_situacao"     + str(codigo_situacao),    json.dumps(veiculo))
            redis.set("ativos_regional"     + str(codigo_regional),    json.dumps(veiculo))
            
            
            redis.set("internal_search_ativos",    json.dumps(veiculo))
            dataVehicles = json.loads(redis.get("internal_search_ativos"))


      elif  codigo_situacao == "4": 
            
            redis.set("inadimplentes_cooperativas" + str(codigo_cooperativa), json.dumps(veiculo))
            redis.set("inadimplentes_situacao"     + str(codigo_situacao),    json.dumps(veiculo))
            redis.set("inadimplentes_regional"     + str(codigo_regional),    json.dumps(veiculo))

            redis.set("internal_search_inadimplentes",    json.dumps(veiculo))
            dataVehicles = json.loads(redis.get("internal_search_inadimplentes"))


      elif  codigo_situacao == "2": 
            
            redis.set("inativos_cooperativas" + str(codigo_cooperativa), json.dumps(veiculo))
            redis.set("inativos_situacao"     + str(codigo_situacao),    json.dumps(veiculo))
            redis.set("inativos_regional"     + str(codigo_regional),    json.dumps(veiculo))


            redis.set("internal_search_inativos",    json.dumps(veiculo))
            dataVehicles = json.loads(redis.get("internal_search_inativos"))
 
      ############### SAVE DATA ON CONSULTING DATABASE HINOVA
 



      data_out = []
      data_inicio = data_inicio
      data_fim = data_fim
      list_ = dataVehicles["veiculos"]
  
      print(veiculo)
      i = 0
      while i < len(list_):
              
              
        try: 
            
           data              = list_[i]
           codigo_veiculo    = data['codigo_veiculo']
           placa             = data['placa']
           chassi            = data['chassi']
           renavam           = data['renavam']
           codigo_associado  = data['codigo_associado']
           codigo_tipo       = data['codigo_tipo']
           codigo_categoria  = data['codigo_categoria']
           tipo              = data['tipo']
           categoria         = data['categoria']
           marca             = data['marca']
           modelo            = data['modelo']
           tipo              = data['tipo']
           cpf_associado     = data['cpf_associado']
           rg_associado      = data['rg_associado']
           email             = data['email']
           codigo_situacao   = data['codigo_situacao']
           codigo_voluntario = data['codigo_voluntario']
           nome_associado    = data['nome_associado']
           telefone          = data['telefone']
           ddd               = data['ddd']
           whatsapp          = ddd+telefone  

           
           data = {  
              "id"      : i,
              "placa"   : placa,
              "codigo"  : codigo_veiculo,
              "chassi"  : chassi,
              "renavam" : renavam,
              "cpf"     : cpf_associado,
              "rg"      : rg_associado,
              "nome_associado": nome_associado
           }  
                     
           out= {  
              "id"      : i,
              "placa"   : placa,
              "codigo"  : codigo_veiculo,
              "chassi"  : chassi,
              "renavam" : renavam,
              "cpf"     : cpf_associado,
              "rg"      : rg_associado,
              "nome_associado": nome_associado
           }  
          
           ###################//////////////
           traccar_id                       =  SAVE.get_traccar_id(placa)               ### GPWROX
           


           #   ###################//////////////

           if int(codigo_situacao) == 1:   ##  ATIVO
              print("executando ativos \n")
              codigo           =  1
              print("executando salvar...\n")

              

              
              if traccar_id is None:
              
                  print("\n\n")
                  print("NONE:::" + placa)
                  print("\n\n")

                  #######LOGS//////////////////
                  situation = { "situacao": "não existe"}
                  formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
                  LOGS_BY_SYSTEM.LOGSYS("logs/inexistente/ativos/placas_filter.log", formatLOG , str(data) + str(situation) , logging.INFO)
                 

                  print("SAVE DATA REDIS")

                  redis.set("ativas_hinova" + str(placa), json.dumps(data))
                  #######LOGS//////////////////

              else:
                  
                  print("\n\n")
                  print("SIMOVSAT:: " + traccar_id )
                  print("SIMOVSAT:: " + placa )
                  print("\n\n")

                  #######LOGS//////////////////
                  situation = { "situacao": "ativos"}
                  formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
                  LOGS_BY_SYSTEM.LOGSYS("logs/simovsat/ativos/placas_filter.log", formatLOG , str(data) + str(situation) , logging.INFO)
                  #######LOGS//////////////////

                  #######SAVE ANALISES ON DATABASE SQLSERVER/////////
                  print("SALVANDO HISTÓRICO")
                  database_.HISTORICO(placa, "ATIVO", str(out), str(DATENOW), 1)
                  #######SAVE ANALISES ON DATABASE SQLSERVER/////////

                  print("SAVE DATA REDIS")
                  redis.set("ativas_" + str(placa), json.dumps(data))
                  
                  ### UPDATE ACTIVE DEVICES
                  SAVE.active_vehicles(traccar_id, codigo)  


           elif int(codigo_situacao) == 2:
              print("executando inativos \n")
              codigo          =  0
              print("executando salvar inativos...\n")
              
  
              ############ VERIFICAÇÃO DE ATIVOS E INATIVOS E INADIMPLEMNTES

              if traccar_id is None:
              
                  print("\n\n")
                  print("NONE:::" + placa)
                  print("\n\n")

                  #######LOGS//////////////////
                  situation = { "situacao": "não existe"}
                  formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
                  LOGS_BY_SYSTEM.LOGSYS("logs/inexistente/inativos/placas_filter.log", formatLOG , str(data) + str(situation) , logging.INFO)

                  print("SAVE DATA REDIS")
                  redis.set("inativos_hinova" + str(placa), json.dumps(data))
                  #######LOGS//////////////////

              else:
                  
                  print("\n\n")
                  print("SIMOVSAT:: " + traccar_id )
                  print("SIMOVSAT:: " + placa )
                  print("\n\n")

                  #######LOGS//////////////////
                  situation = { "situacao": "inativos"}
                  formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
                  LOGS_BY_SYSTEM.LOGSYS("logs/simovsat/inativos/placas_filter.log", formatLOG , str(data) + str(situation) , logging.INFO)
                  #######LOGS//////////////////
                  
                  #######SAVE ANALISES ON DATABASE SQLSERVER/////////
                  print("SALVANDO HISTÓRICO")
                  database_.HISTORICO(placa, "INATIVO", str(out), str(DATENOW), 1)
                  #######SAVE ANALISES ON DATABASE SQLSERVER/////////
                  
                  print("SAVE DATA REDIS")
                  redis.set("inativos_" + str(placa), json.dumps(data))
                  
                  ### UPDATE ACTIVE DEVICES
                  SAVE.active_vehicles(traccar_id, codigo) 
               
               ############ VERIFICAÇÃO DE ATIVOS E INATIVOS E INADIMPLEMNTES

           elif int(codigo_situacao) == 4:
              print("executando inadimplentes \n")
              codigo          =  0
              print("executando salvar inadimplentes...\n")
              
              


               
              ############ VERIFICAÇÃO DE ATIVOS E INATIVOS E INADIMPLEMNTES

              if traccar_id is None or traccar_id == '':
                  

                  print("\n\n")
                  print("NONE:::" + placa)
                  print("\n\n")


                  #######LOGS//////////////////
                  situation = { "situacao": "não existe"}
                  formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
                  LOGS_BY_SYSTEM.LOGSYS("logs/inexistente/inadimplentes/placas_filter.log", formatLOG , str(data) + str(situation) , logging.INFO)
                  print("SAVE DATA ON REDIS :: " + placa)
                  redis.set("inadimplentes_hinova" + str(placa), json.dumps(data))
                  #######LOGS//////////////////

              else:
                  
                  print("\n\n")
                  print("SIMOVSAT:: " + traccar_id )
                  print("SIMOVSAT:: " + placa )
                  print("\n\n")


                  #######LOGS//////////////////
                  situation = { "situacao": "inadimplemtes"}
                  formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
                  LOGS_BY_SYSTEM.LOGSYS("logs/simovsat/inadimplentes/placas_filter.log", formatLOG , str(data) + str(situation) , logging.INFO)
                  #######LOGS//////////////////
                  
                  #######SAVE ANALISES ON DATABASE SQLSERVER/////////
                  print("SALVANDO HISTÓRICO")
                  database_.HISTORICO(placa, "INADIMPLENTE", str(out), str(DATENOW), 1)
                  #######SAVE ANALISES ON DATABASE SQLSERVER/////////

                  print("SAVE DATA ON REDIS :: " + placa)
                  redis.set("inadimplentes_" + str(placa), json.dumps(data))

                  ### UPDATE ACTIVE DEVICES
                  SAVE.active_vehicles(traccar_id, codigo) 
               
               ############ VERIFICAÇÃO DE ATIVOS E INATIVOS E INADIMPLEMNTES

 
  
        except:
           # URLde RETORNO e finaliza
           print('processo finalizado com sucesso')
           break

        i = i + 1
        ## CALLBACK IS HERE
      return  "OK"     
      




    def veiculos_filter_import(self, params, codigo_situacao, veiculo, produto, codigo_cooperativa, cooperativa, codigo_regional, data_inicio, data_fim):
      





      ############### SAVE DATA ON CONSULTING DATABASE HINOVA

      if    codigo_situacao == "1":

            redis.set("ativos_cooperativas" + str(codigo_cooperativa), json.dumps(veiculo))
            redis.set("ativos_situacao"     + str(codigo_situacao),    json.dumps(veiculo))
            redis.set("ativos_regional"     + str(codigo_regional),    json.dumps(veiculo))
            
            
            redis.set("internal_search_ativos",    json.dumps(veiculo))
            dataVehicles = json.loads(redis.get("internal_search_ativos"))


      elif  codigo_situacao == "4": 
            
            redis.set("inadimplentes_cooperativas" + str(codigo_cooperativa), json.dumps(veiculo))
            redis.set("inadimplentes_situacao"     + str(codigo_situacao),    json.dumps(veiculo))
            redis.set("inadimplentes_regional"     + str(codigo_regional),    json.dumps(veiculo))

            redis.set("internal_search_inadimplentes",    json.dumps(veiculo))
            dataVehicles = json.loads(redis.get("internal_search_inadimplentes"))


      elif  codigo_situacao == "2": 
            
            redis.set("inativos_cooperativas" + str(codigo_cooperativa), json.dumps(veiculo))
            redis.set("inativos_situacao"     + str(codigo_situacao),    json.dumps(veiculo))
            redis.set("inativos_regional"     + str(codigo_regional),    json.dumps(veiculo))


            redis.set("internal_search_inativos",    json.dumps(veiculo))
            dataVehicles = json.loads(redis.get("internal_search_inativos"))
 
      ############### SAVE DATA ON CONSULTING DATABASE HINOVA
 

      data_out = []
      data_inicio = data_inicio
      data_fim = data_fim
      list_ = dataVehicles["veiculos"]


      ####### REDIS SAVE
      redis.set("veiculos_importados", json.dumps(veiculo))
      ####### REDIS SAVE
 
 

  
      
  
      print(len(list_))
      i = 0
      while i < len(list_):
              
              
        try: 
           
           data              = list_[i]
           codigo_veiculo    = data['codigo_veiculo']
           placa             = data['placa']
           chassi            = data['chassi']
           renavam           = data['renavam']
           codigo_associado  = data['codigo_associado']
           codigo_tipo       = data['codigo_tipo']
           codigo_categoria  = data['codigo_categoria']
           tipo              = data['tipo']
           categoria         = data['categoria']
           marca             = data['marca']
           modelo            = data['modelo']
           tipo              = data['tipo']
           cpf_associado     = data['cpf_associado']
           rg_associado      = data['rg_associado']
           email             = data['email']
           codigo_situacao   = data['codigo_situacao']
           codigo_voluntario = data['codigo_voluntario']
           nome_associado    = data['nome_associado']
           telefone          = data['telefone']
           ddd               = data['ddd']
           whatsapp          = ddd+telefone  

          
           data = {  
              "placa"   : placa,
              "codigo"  : codigo_veiculo,
              "chassi"  : chassi,
              "renavam" : renavam,
              "cpf"     : cpf_associado,
              "rg"      : rg_associado,
              "nome_associado": nome_associado
           }  
          
           out = {
              "placa"   : placa,
              "codigo"  : codigo_veiculo,
              "chassi"  : chassi,
              "renavam" : renavam,
              "cpf"     : cpf_associado,
              "rg"      : rg_associado,
              "nome_associado": nome_associado
           }
           ###################//////////////
           traccar_id                       =  SAVE.get_traccar_id(placa)               ### GPWROX
           


           #   ###################//////////////
           

            
           if traccar_id is None or traccar_id == '':
            
                print("NÃO EXISTE::" + placa)
                print("CADASTRANDO PLACA:::" + placa)
                #######LOGS//////////////////
                situation = { "situacao": "importando"}
                formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
                LOGS_BY_SYSTEM.LOGSYS("logs/importadas/placas.log", formatLOG , str(data) + str(situation) , logging.INFO)
                #######LOGS//////////////////

                #######SAVE ANALISES ON DATABASE SQLSERVER/////////
                print("SALVANDO HISTÓRICO")
                database_.HISTORICO(placa, "VEICULO HINOVA", str(out), str(DATENOW), 1)
                #######SAVE ANALISES ON DATABASE SQLSERVER/////////

                id          =  SAVE.traccar(codigo_veiculo, placa, chassi, renavam, codigo_associado, codigo_tipo, codigo_categoria, tipo, categoria, marca, modelo, cpf_associado, rg_associado, nome_associado, codigo_situacao, codigo_voluntario, whatsapp, email)
  
                id_vehicles =  SAVE.veiculos(codigo_veiculo, id, placa, chassi, renavam, codigo_associado, codigo_tipo, codigo_categoria, tipo, categoria, marca, modelo, cpf_associado, rg_associado, nome_associado, codigo_situacao, codigo_voluntario, whatsapp, email)
                print(id_vehicles)
                time.sleep(5)

           else:
  
                print("CADASTRADAS:: " + placa)
                #######LOGS//////////////////
                situation = { "situacao": "ativos"}
                formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
                LOGS_BY_SYSTEM.LOGSYS("logs/cadastradas/placas.log", formatLOG , str(data) + str(situation) , logging.INFO)
                
                #######SAVE ANALISES ON DATABASE SQLSERVER/////////
                print("SALVANDO HISTÓRICO")
                database_.HISTORICO(placa, "VEICULO SIMOVSAT", str(out), str(DATENOW), 1)
                #######SAVE ANALISES ON DATABASE SQLSERVER/////////
                #######LOGS//////////////////



 

        except:
           # URLde RETORNO e finaliza
           pass

        i = i + 1
        ############# AFTER TRATAMENT SEND TO CALLBACK DATA
        ## CALLBACK IS HERE

      return  "OK"     



    # def veiculos(self, params):

   
    #   data_out = []
      
    #   list_ = params
    #   total = params["veiculos"]

    #   print(len(total))
  
    #   i = 0
    #   while i < int(len(total)):
              
              
    #     try: 

    #        data              = list_["veiculos"][i]
    #        codigo_veiculo    = data['codigo_veiculo']
    #        placa             = data['placa']
    #        chassi            = data['chassi']
    #        renavam           = data['renavam']
    #        codigo_associado  = data['codigo_associado']
    #        codigo_tipo       = data['codigo_tipo']
    #        codigo_categoria  = data['codigo_categoria']
    #        tipo              = data['tipo']
    #        categoria         = data['categoria']
    #        marca             = data['marca']
    #        modelo            = data['modelo']
    #        tipo              = data['tipo']
    #        cpf_associado     = data['cpf_associado']
    #        rg_associado      = data['rg_associado']
    #        email             = data['email']
    #        codigo_situacao   = data['codigo_situacao']
    #        codigo_voluntario = data['codigo_voluntario']
    #        nome_associado    = data['nome_associado']
    #        telefone          = data['telefone']
    #        ddd               = data['ddd']
    #        whatsapp          = ddd+telefone  
           
    #                  ###################//////////////
    #        traccar_id                       =  SAVE.get_traccar_id(placa)               ### GPWROX
           


    #        #   ###################//////////////

            
    #        if traccar_id is None:
            
    #             print("não existe no simovsat")
    #             #######LOGS//////////////////
    #             situation = { "situacao": "importando"}
    #             formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    #             LOGS_BY_SYSTEM.LOGSYS("logs/importadas/placas.log", formatLOG , str(data) + str(situation) , logging.INFO)
    #             #######LOGS//////////////////

    #             id =  SAVE.traccar(codigo_veiculo, placa, chassi, renavam, codigo_associado, codigo_tipo, codigo_categoria, tipo, categoria, marca, modelo, cpf_associado, rg_associado, nome_associado, codigo_situacao, codigo_voluntario, whatsapp, email)
    #             SAVE.veiculos(codigo_veiculo, id, placa, chassi, renavam, codigo_associado, codigo_tipo, codigo_categoria, tipo, categoria, marca, modelo, cpf_associado, rg_associado, nome_associado, codigo_situacao, codigo_voluntario, whatsapp, email)
              

    #        else:
                
    #             print(placa)
    #             print("SIMOVSAT:: " + traccar_id )
    #             #######LOGS//////////////////
    #             situation = { "situacao": "ativos"}
    #             formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    #             LOGS_BY_SYSTEM.LOGSYS("logs/cadastradas/placas.log", formatLOG , str(data) + str(situation) , logging.INFO)
    #             #######LOGS//////////////////
     
    #     except:
    #        # URLde RETORNO e finaliza
    #        print('ERROR processo::::' + placa)
    #        break

    #     i = i + 1

    #   return  "OK"     
      


    # def veiculos_block_tratamento(self, params):
      

    #   data_out = []
      
    #   list_ = params
    #   total = params["veiculos"]

    #   print(len(total))
  
    #   i = 0
    #   while i < int(len(total)):
              
              
    #     try: 
           
    #        ## inativo 2 ativo 1

    #        data            = list_["veiculos"][i]
    #        codigo_veiculo  = data['codigo_veiculo']
    #        placa           = data['placa']
    #        chassi          = data['chassi']
    #        renavam         = data['renavam']
    #        cpf_associado   = data['cpf_associado']
    #        rg_associado    = data['rg_associado']
    #        codigo_situacao = data['codigo_situacao']
    #        nome_associado  = data['nome_associado']
          
    #        data = {  
    #         "placa"   : placa,
    #         "codigo"  : codigo_veiculo,
    #         "chassi"  : chassi,
    #         "renavam" : renavam,
    #         "cpf"     : cpf_associado,
    #         "rg"      : rg_associado,
    #         "nome_associado": nome_associado
    #        }      

    #        ###################//////////////
    #        traccar_id                       =  SAVE.get_traccar_id(placa)               ### GPWROX
           


    #      #   ###################//////////////

    #        if int(codigo_situacao) == 1:   ##  ATIVO
    #           print("executando ativos \n")
    #           codigo           =  1
    #           #update_user     =  SAVE.active_users(id_users, codigo) 
    #           print("executando salvar...\n")

              
    #           if traccar_id is None:
              
    #               print("não existe no simovsat")
    #               #######LOGS//////////////////
    #               situation = { "situacao": "não existe"}
    #               formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    #               LOGS_BY_SYSTEM.LOGSYS("logs/inexistente/ativos/placas.log", formatLOG , str(data) + str(situation) , logging.INFO)
    #               #######LOGS//////////////////

    #           else:
                  
    #               print(placa)
    #               print("SIMOVSAT:: " + traccar_id )
    #               #######LOGS//////////////////
    #               situation = { "situacao": "ativos"}
    #               formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    #               LOGS_BY_SYSTEM.LOGSYS("logs/simovsat/ativos/placas.log", formatLOG , str(data) + str(situation) , logging.INFO)
    #               #######LOGS//////////////////

    #               SAVE.active_vehicles(traccar_id, codigo)


    #        elif int(codigo_situacao) == 2:
    #           print("executando inativos \n")
    #           codigo          =  0
    #           #update_user    =  SAVE.active_users(id_users, codigo) 
    #           print("executando salvar inativos...\n")
              
  
    #           ############ VERIFICAÇÃO DE ATIVOS E INATIVOS E INADIMPLEMNTES

    #           if traccar_id is None:
              
    #               print("não existe no simovsat")
    #               #######LOGS//////////////////
    #               situation = { "situacao": "não existe"}
    #               formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    #               LOGS_BY_SYSTEM.LOGSYS("logs/inexistente/inativos/placas.log", formatLOG , str(data) + str(situation) , logging.INFO)
    #               #######LOGS//////////////////

    #           else:
                  
    #               print(placa)
    #               print("SIMOVSAT:: " + traccar_id )

    #               #######LOGS//////////////////
    #               situation = { "situacao": "inativos"}
    #               formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    #               LOGS_BY_SYSTEM.LOGSYS("logs/simovsat/inativos/placas.log", formatLOG , str(data) + str(situation) , logging.INFO)
    #               #######LOGS//////////////////

    #               SAVE.active_vehicles(traccar_id, codigo) 
               
    #            ############ VERIFICAÇÃO DE ATIVOS E INATIVOS E INADIMPLEMNTES

    #        elif int(codigo_situacao) == 4:
    #           print("executando inadimplemtes \n")
    #           codigo          =  0
    #           #update_user    =  SAVE.active_users(id_users, codigo) 
    #           print("executando salvar inadimplemtes...\n")
              


               
    #           ############ VERIFICAÇÃO DE ATIVOS E INATIVOS E INADIMPLEMNTES

    #           if traccar_id is None:
              
    #               print("não existe no simovsat")
    #               #######LOGS//////////////////
    #               situation = { "situacao": "não existe"}
    #               formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    #               LOGS_BY_SYSTEM.LOGSYS("logs/inexistente/inadimplentes/placas.log", formatLOG , str(data) + str(situation) , logging.INFO)
    #               #######LOGS//////////////////

    #           else:
                  
    #               print(placa)
    #               print("SIMOVSAT:: " + traccar_id )

    #               #######LOGS//////////////////
    #               situation = { "situacao": "inadimplemtes"}
    #               formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    #               LOGS_BY_SYSTEM.LOGSYS("logs/simovsat/inadimplentes/placas.log", formatLOG , str(data) + str(situation) , logging.INFO)
    #               #######LOGS//////////////////

    #               SAVE.active_vehicles(traccar_id, codigo) 
               
    #            ############ VERIFICAÇÃO DE ATIVOS E INATIVOS E INADIMPLEMNTES

 
    #      #   ###################//////////////
           
    #     except:
    #        print('processo:::' + placa)
    #        pass

    #     i = i + 1

    #   return  "OK"     
      



    def situacao(self, params):
 
        
      i = 0
      redis.set("situacao_todas", json.dumps(params))
      data= []


      while i <= 4:
  
        codigo_situacao = params[i]['codigo_situacao']
        descricao_situacao = params[i]['descricao_situacao']
        situacao = params[i]['situacao']
   
        desc     = descricao_situacao
        situacao = situacao
        
        result = {

            i:{
            "descricao":desc,
            "situacao":situacao
            }
        }

        data.append(result)
        
        i += 1
        ## CALLBACK IS HERE

      json8 = data
      out  = json.dumps(json8)
      return out     
      




    ###LISTAR PRODUTO NA API PARA FRONTEND
    def produto(self, params):

        redis.set("produtos_todas", json.dumps(params))

        codigo_produto = params[0]["codigo_produto"]
        decricao_produto = params[0]["decricao_produto"]
        descricao_produto_boleto = params[0]["descricao_produto_boleto"]
        valor_produto= params[0]["valor_produto"]
        valor_fipe_inicial = params[0]["valor_fipe_inicial"]
        codigo_classificacao_produto = params[0]["codigo_classificacao_produto"]
        compulsorio = params[0]["compulsorio"]
        formato_cobranca = params[0]["formato_cobranca"]
        codigo_tipo_veiculo = params[0]["codigo_tipo_veiculo"]
        descricao_tipo_veiculo = params[0]["descricao_tipo_veiculo"]
        regionais_cod = params[0]["regionais"][0]["codigo_regional"]
        regionais_name = params[0]["regionais"][0]["nome_regional"]
        return "OK"    



    ###LISTAR PRODUTO NA API PARA FRONTEND
    def regional(self, params):
        total = len(params) # 501
        redis.set("regionais_todas", json.dumps(params))
        print(total)
        
        i = 0
        while i <=  int(total) -1: 
          codigo_regional = params[i]["codigo_regional"]
          nome            = params[i]["nome"]
          nome_fantasia   = params[i]["nome_fantasia"]
          cnpj            = params[i]["cnpj"]
          logradouro      = params[i]["logradouro"]
          numero          = params[i]["numero"]
          complemento     = params[i]["complemento"]
          bairro          = params[i]["bairro"]
          complemento     = params[i]["complemento"]
          bairro          = params[i]["bairro"]
          cidade          = params[i]["cidade"]
          estado          = params[i]["estado"]
          cep             = params[i]["cep"]
          email           = params[i]["email"]
          website         = params[i]["website"]
          telefone        = params[i]["telefone"]
          situacao        = params[i]["situacao"]
          i +=1

        return "OK"    





    ###LISTAR VOLUNTARIOS NA API PARA FRONTEND
    def voluntario(self, params):
        print("VOLUNTARIOS")
        redis.set("voluntarios_todas", json.dumps(params))
        total = len(params) # 501

                 
        i = 0
        while i <=  int(total) -1: 
    
            codigo_voluntario = params[i]["codigo_voluntario"]
            nome = params[i]["nome"]
            cpf = params[i]["cpf"]
            telefone = params[i]["telefone"]
            telefone_comercial = params[i]["telefone_comercial"]
            cep = params[i]["cep"]
            celular = params[i]["celular"]
            email= params[i]["email"]
            situacao = params[i]["situacao"]
            formato_pagamento = params[i]["formato_pagamento"]
            valor_pagamento = params[i]["valor_pagamento"]
            formato_pagamento_residual = params[i]["formato_pagamento_residual"]
            codigo_classificacao = params[i]["codigo_classificacao"]
            valor_pagamento_residual = params[i]["valor_pagamento_residual"]
            obs = params[i]["obs"]
            logradouro = params[i]["logradouro"]
            numero = params[i]["numero"]
            complemento = params[i]["complemento"]
            bairro = params[i]["bairro"]
            cidade = params[i]["cidade"]
            estado = params[i]["estado"]


            i += 1

        return "OK"            
             


    ###LISTAR COOPERATIVAS NA API PARA FRONTEND
    def cooperativa(self, params):
        redis.set("cooperativas_todas", json.dumps(params))
        total = len(params) #19
         
        i = 0
        while i <=  int(total) - 1: 
          
          
           codigo = params[i]["codigo_cooperativa"]
           nome   = params[i]["nome"]
           valor_pagamento = params[0]["valor_pagamento"]
           logradouro = params[i]["logradouro"]
           numero = params[i]["numero"]
           complemento = params[0]["complemento"]
           bairro = params[i]["bairro"]
           cidade = params[i]["cidade"]
           estado = params[i]["estado"]
           cep = params[i]["cep"]
           email = params[i]["email"]
           cpf = params[i]["cpf"]
           contato = params[i]["contato"]
           telefone = params[i]["telefone"]
           valor_pagamento_residual = params[i]["valor_pagamento_residual"]
           telefone_comercial = params[i]["telefone_comercial"]
           formato_pagamento_residual = params[i]["formato_pagamento_residual"]
           formato_pagamentol = params[i]["formato_pagamento"]
           situacao = params[i]["situacao"]
           
           i += 1
        
        
        return "OK"                    


  



    def infornetbeneficiarios(self, params):
        nameStr = str(params).split("nome",1)[1] 
        name    = nameStr.split("documentoBeneficiario",1)[0].replace("'","").replace(":","").replace(",","")
        cpfStr = str(params).split("documentoBeneficiario",1)[1] 
        cpf    = cpfStr.split("situacao",1)[0].replace("'","").replace(":","").replace(",","")
        situacaoStr = str(params).split("situacao",1)[1] 
        situacao    = situacaoStr.split("codigoProduto",1)[0].replace("'","").replace(":","").replace(",","").replace(" ","")
        produto  = str(params).split("nomeProduto",1)[1].replace("'","").replace(":","").replace(",","").replace(" ","")

        name = name
        date = "01/01/2024"
        cpf  = cpf
        agenda  = DATENOW
        especialidade = "clinico geral"
        telefone  = "21000000000"
        situacao  = situacao
        produto   = produto
        
        out = [name,date,cpf,agenda,especialidade,telefone, situacao, produto]
        return out                 


    def infornetveiculos(self, params):
        nameStr = str(params).split("nomeBeneficiario",1)[1] 
        name    = nameStr.split("situacao",1)[0].replace("'","").replace(":","").replace(",","")
        cpfStr  = str(params).split("documentoBeneficiario",1)[1] 
        cpf     = cpfStr.split("nomeBeneficiario",1)[0].replace("'","").replace(":","").replace(",","")
        situacaoStr = str(params).split("situacao",1)[1] 
        situacao    = situacaoStr.split("codigoProduto",1)[0].replace("'","").replace(":","").replace(",","").replace(" ","")
        produtoStr  = str(params).split("nomeProduto",1)[1]
        produto     = produtoStr.split("email",1)[0].replace("'","").replace(":","").replace(",","").replace(" ","")
        email       = situacaoStr.split("email",1)[1].replace("'","").replace(":","").replace(",","").replace(" ","").replace("}","")

        name      = name
        date      = "01/01/2024"
        cpf       = cpf
        agenda    = DATENOW
        especialidade = "clinico geral"
        telefone  = "21000000000"
        situacao  = situacao
        produto   = produto
        email     = email
        
        out = [name,date,cpf,agenda,especialidade,telefone, situacao, produto, email]
        time.sleep(5)
        return out      




    def infornetclube(self, params):
        cpf = params["cpf"]
        id  = params["id"]
        out = [id,cpf]
        return out      
