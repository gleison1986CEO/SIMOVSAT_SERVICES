import os
from flask import Flask, json, request, Response, jsonify, redirect, url_for, Response
from dotenv import load_dotenv
import time
import os, sys
import os.path
import random
import re
import sys
import requests
import redis
from flask_caching import Cache 
from threading import Thread
import traceback
import uuid
import urllib.request
import urllib
from flask_swagger_ui import get_swaggerui_blueprint

load_dotenv()

LOGININFOR          = os.getenv('INFORNETLOGIN')
SENHAINFOR          = os.getenv('INFORNETSENHA')
URIINFORNET         = os.getenv('INFORNEURI')
INFORNEURIBENEFIT   = os.getenv('INFORNEURIBENEFIT')
INFORNEURIVEICULOS  = os.getenv('INFORNEURIVEICULOS')

class INFORNETPASS:
    def post(self, cnpj):

        #==========================================  


        url = URIINFORNET
        payload = {
                        "login":LOGININFOR,
                        "senha":SENHAINFOR,
                        "cnpj" :cnpj 
                    }

    
  
        headers = {
          "Content-Type": "application/json"
        }

        #========================================== 

        response = requests.request("POST", url, json=payload, headers=headers)
        params = json.loads(response.text)
        keyinfornt = params["mensagem"]
        return keyinfornt



    def postbeneficiarios(self, cnpj, key):
    
        #==========================================  


        url = INFORNEURIBENEFIT
        payload = {
                        "login":LOGININFOR,
                        "senha":SENHAINFOR,
                        "cnpj" :cnpj ,
                        "chaveCliente": key
                    }

    
        headers = {
          "Content-Type": "application/json"
        }

        #========================================== 

        response = requests.request("POST", url, json=payload, headers=headers)
        params   = json.loads(response.text)
        uri      = params["beneficiarios"]
        return uri



    def postveiculos(self, cnpj, key):
    
        #==========================================  


        url = INFORNEURIVEICULOS
        payload = {
                        "login":LOGININFOR,
                        "senha":SENHAINFOR,
                        "chaveCliente": key,
                        "paginacao"   :50000
                    }

    
        headers = {
          "Content-Type": "application/json"
        }

        #========================================== 

        response = requests.request("POST", url, json=payload, headers=headers)
        params   = json.loads(response.text)
        uri      = params["veiculos"]
        return uri



        
    def listar(self, uri):
        
    
        headers = {
          "Content-Type": "application/json"
        }

        response = requests.request("GET", uri, headers=headers)
        params  = json.loads(response.text)
 
        return  params