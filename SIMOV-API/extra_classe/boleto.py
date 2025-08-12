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


###############LOAD ENV
load_dotenv()
BEARTOKEN      = os.getenv('BEARTOKEN')
USERHINOVA     = os.getenv('USERHINOVA')
PASSWORDHINOVA = os.getenv('PASSWORDHINOVA')
ENDPOINTCODIGOBOLETO   = os.getenv('ENDPOINTCODIGOBOLETO')
ENDPOINTGETBOLETO      = os.getenv('ENDPOINTGETBOLETO')
ENDPOINTWHATSAPP       = os.getenv('ENDPOINTWHATSAPP')
COOKIE         = os.getenv('COOKIE')
MSGDATA        = os.getenv('MSGDATA')
###############LOAD ENV


from classes.key  import key_acess
from classes.time import TIME
timedata         = TIME()
generate_key     = key_acess


class BOLETO:
    def boletosdisponivel(self, codigo_associado):
        time.sleep(2)
        key = generate_key.key_hinova()
        
        payload = {

              "codigo_associado" : codigo_associado,
              "codigo_situacao_boleto"  : "2", ## SITUACAO DO BOLETO ABERTO
              "data_vencimento_inicial" : timedata.timedate25(),
              "data_vencimento_final"   : timedata.timedatenow(),
              "data_pagamento_inicial"  : timedata.timedate25(),
              "data_pagamento_final"    : timedata.timedatenow(),
              "data_vencimento_original_inicial" : timedata.timedate25(),
              "data_vencimento_original_final"   : timedata.timedatenow(),
              "data_emissao_inicial"    : timedata.timedate25(),
              "data_emissao_final"      : timedata.timedatenow()
        
        } 
        headers = {
          "cookie": COOKIE,
          "Content-Type": "application/json",
          "Authorization": "Bearer " + key
        }




        response = requests.request("POST", ENDPOINTCODIGOBOLETO, json=payload, headers=headers)
        params = json.loads(response.text)

 
        return  params


    def boletosbaixado(self, codigo_associado):
        time.sleep(2)

        key = generate_key.key_hinova()
        
        payload = {

              "codigo_associado" :codigo_associado,
              "codigo_situacao_boleto" : "1", ## SITUACAO DO BOLETO BAIXADO
              "data_vencimento_inicial" : timedata.timedate25(),
              "data_vencimento_final"   : timedata.timedatenow(),
              "data_pagamento_inicial"  : timedata.timedate25(),
              "data_pagamento_final"    : timedata.timedatenow(),
              "data_vencimento_original_inicial" : timedata.timedate25(),
              "data_vencimento_original_final" : timedata.timedatenow(),
              "data_emissao_inicial"    : timedata.timedate25(),
              "data_emissao_final"      : timedata.timedatenow()
        
        } 
        headers = {
          "cookie": COOKIE,
          "Content-Type": "application/json",
          "Authorization": "Bearer " + key
        }




        response = requests.request("POST", ENDPOINTCODIGOBOLETO, json=payload, headers=headers)
        params = json.loads(response.text)
        

        return  params


    def boletospendencia(self, codigo_associado):
        time.sleep(2)
        key = generate_key.key_hinova()
        
        payload = {

              "codigo_associado" : codigo_associado,
              "codigo_situacao_boleto" : "4",  ## SITUACAO DO BOLETO PENDENTE
              "data_vencimento_inicial" : timedata.timedate25(),
              "data_vencimento_final"   : timedata.timedatenow(),
              "data_pagamento_inicial"  : timedata.timedate25(),
              "data_pagamento_final"    : timedata.timedatenow(),
              "data_vencimento_original_inicial" : timedata.timedate25(),
              "data_vencimento_original_final" : timedata.timedatenow(),
              "data_emissao_inicial"    : timedata.timedate25(),
              "data_emissao_final"      : timedata.timedatenow()
        
        } 
        headers = {
          "cookie": COOKIE,
          "Content-Type": "application/json",
          "Authorization": "Bearer " + key
        }




        response = requests.request("POST", ENDPOINTCODIGOBOLETO, json=payload, headers=headers)
        params = json.loads(response.text)



        return  params





    def listar(self, nosso_numero):
        time.sleep(2)  
        key = generate_key.key_hinova()
        
        url = ENDPOINTGETBOLETO + str(nosso_numero)

        headers = {
          "cookie": COOKIE,
          "Content-Type": "application/json",
          "Authorization": "Bearer " + key
        }

        response = requests.request("GET", url,  headers=headers)
        params = json.loads(response.text)

        return  params



########### POST ON WHASTAPP JS
########### POST ON WHASTAPP JS

    def boletosencontrado(self, whatsapp, linha_digitavel, link_boleto, short_link, data_vencimento, valor_boleto, nome_associado, cpf_associado, vencimento, descricao):
        time.sleep(10)
        ### ENVIDO DE MENSAGEM PARA CLIENTE
        payload = {

              "linha_digitavel" : linha_digitavel,
              "link_boleto"     : link_boleto,
              "data_vencimento" : data_vencimento,
              "valor_boleto"    : valor_boleto,
              "nome_associado"  : nome_associado,
              "cpf_associado"   : cpf_associado,
              "date"            : timedata.timedatenow(),
              "descricao"       : descricao,
              "vencimento"      : vencimento,
              "whatsapp"        : str(whatsapp)
              
        
        } 

        headers = {
          "Content-Type": "application/json",
        }




        response = requests.request("POST", ENDPOINTWHATSAPP, json=payload, headers=headers)
        params   = json.loads(response.text)


        return  params






    def boletoserrorrequest(self, whatsapp):
        
        time.sleep(10)      
        payload = {

            "status"  :   True,
            "descricao" : "ERROR",
            "error"   :   "BOLETO NÃO EXISTE OU TIVEMOS UMA FALHA NO ENVIO POR FAVOR TENTE NOVAMENTE MAIS TARDE, OU SE PREFERIR ENTRE EM CONTATO COM NOSSA CENTRAL",
            "whatsapp":   str(whatsapp),


        }


        headers = {
          "Content-Type": "application/json",
        }

        response = requests.request("POST", ENDPOINTWHATSAPP, json=payload, headers=headers)
        params   = json.loads(response.text)
        

        return  params

########### POST ON WHASTAPP JS
########### POST ON WHASTAPP JS
