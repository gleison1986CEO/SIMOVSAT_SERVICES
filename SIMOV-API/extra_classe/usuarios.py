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
ENPOINTASSOCIADOS   = os.getenv('ENPOINTASSOCIADOS')
ENDPOINTGETUSERBYCPF= os.getenv('ENDPOINTGETUSERBYCPF')
COOKIE         = os.getenv('COOKIE')
MSGDATA        = os.getenv('MSGDATA')
###############LOAD ENV 



from classes.key import key_acess
generate_key = key_acess


class USUARIOS:
    def listar(self, codigo_situacao, inicio_paginacao, quantidade_por_pagina, total,  data_inicio, data_fim):

        key = generate_key.key_hinova()
        

        payload = {

            "codigo_situacao" : codigo_situacao,
	          "inicio_paginacao" : inicio_paginacao,
	          "quantidade_por_pagina" : quantidade_por_pagina
        } 
  
        headers = {
          "cookie": COOKIE,
          "Content-Type": "application/json",
          "Authorization": "Bearer " + key
        }


        response = requests.request("POST", ENPOINTASSOCIADOS, json=payload, headers=headers)
        params = json.loads(response.text)

        return  params


    def cpflist(self, cpf):
    
 
        key = generate_key.key_hinova()
        
  
        headers = {
          "cookie": COOKIE,
          "Content-Type": "application/json",
          "Authorization": "Bearer " + key
        }


        response = requests.request("GET", ENDPOINTGETUSERBYCPF + cpf, headers=headers)
        
        params = json.loads(response.text)
        return  params

