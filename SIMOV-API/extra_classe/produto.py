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
ENDPOINTPRODUTO   = os.getenv('ENDPOINTPRODUTO')
COOKIE         = os.getenv('COOKIE')
MSGDATA        = os.getenv('MSGDATA')
###############LOAD ENV 


from classes.key import key_acess
generate_key     = key_acess


class PRODUTO:
    def listar(self, codigo_regional, codigo_cooperativa, codigo_tipo_veiculo, valor_fipe, cilindrada):

        key = generate_key.key_hinova()

        url = ENDPOINTPRODUTO + codigo_regional + "/" + codigo_cooperativa + "/" + codigo_tipo_veiculo + "/" + valor_fipe + "/" + cilindrada + ""
        

        payload = {
          "usuario": USERHINOVA,
          "senha"  : PASSWORDHINOVA
        } 
  
        headers = {
          "cookie": COOKIE,
          "Content-Type": "application/json",
          "Authorization": "Bearer " + key
        }


        response = requests.request("GET", url,  headers=headers)

        params = json.loads(response.text)

        return  params


