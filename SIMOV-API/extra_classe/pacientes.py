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

KEYCONEXA    = os.getenv('CONEXAKEY')
URICONEXA    = os.getenv('CONEXAURI')
URIPACIENTES = os.getenv('CONEXAURIPACIENTES')
ACTIVEPACIENTES=os.getenv('ACTIVEPACIENTES')

class PACIENTES:
    def post(self, name, dateBirthPerson, cpf, agendaDateTime, especialidade, whatsapp, email):

        #==========================================  
        url = URICONEXA
        payload = {

                    "name": name,
                    "dateBirth": dateBirthPerson,
                    "cpf":  cpf,
                    "mail": email

                } 
        
  
        headers = {
          "Content-Type": "application/json",
          "token": KEYCONEXA
        }

        #========================================== 

        response = requests.request("POST", url, json=payload, headers=headers)
        params = json.loads(response.text)
        return params


    def update(self, id, email):
    
        #==========================================  
        url = URICONEXA
        payload = {
                    "id"  : str(id),
                    "mail": email

                } 
        
  
        headers = {
          "Content-Type": "application/json",
          "token": KEYCONEXA
        }

        #========================================== 

        response = requests.request("POST", url, json=payload, headers=headers)
        params = json.loads(response.text)
        return params


    def ativando(self, id):
    
        #==========================================  
        url = ACTIVEPACIENTES + str(id) + "/activate"
        
        

        headers = {
          "Content-Type": "application/json",
          "token": KEYCONEXA
        }

        #========================================== 

        response = requests.request("POST", url, headers=headers)
        params = json.loads(response.text)
        return params





    def inativando(self,id):
    
        #==========================================  
        url = ACTIVEPACIENTES + str(id) + "/inactivate"
  
        headers = {
          "Content-Type": "application/json",
          "token": KEYCONEXA
        }

        #========================================== 

        response = requests.request("POST", url, headers=headers)
        params = json.loads(response.text)
        return params





    def get(self, cpf):
    
        #==========================================  
        url = URIPACIENTES + str(cpf)
        
  
        headers = {
          "Content-Type": "application/json",
          "token": KEYCONEXA
        }

        #========================================== 


        response = requests.request("GET", url,  headers=headers)
        params   = json.loads(response.text)
        return params
        
