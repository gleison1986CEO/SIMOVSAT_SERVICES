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

LOGINCLUBE    = os.getenv('LOGINCLUBE')
PASSCLUBE     = os.getenv('PASSCLUBE')
URICLUBEAUTH  = os.getenv('URICLUBEAUTH')
URIGETUSERS   = os.getenv('URIGETUSERS')
URICLUBEAUTORIZED = os.getenv('URICLUBEAUTORIZED')
URINEWUSER    = os.getenv('URINEWUSER')
URIUPDATEUSER = os.getenv('URIUPDATEUSER')

class CLUBEPASS:
      

    ## AUTENTICAÇÃO INFORNET

    def auth(self):
          
        try:
        
          #==========================================  
          url = URICLUBEAUTH
          payload = {
                      
                      "grant_type": "client_credentials",
                      "client_id" :   LOGINCLUBE,
                      "client_secret": PASSCLUBE,
                      "scope":  "*"

                  } 
          
    
          headers = {
            "Content-Type": "application/json"
          }

          #========================================== 


          response = requests.request("POST", url, json=payload, headers=headers)
          params = json.loads(response.text)
          return params["access_token"]
        except:
            pass





    #GET ALL USERS INFORNET

    def get(self, keyClube):
         
        try:
          #==========================================  

          url = URIGETUSERS
          
          
          headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + keyClube
          }

          #========================================== 


          response = requests.request("GET", url,  headers=headers)
          params   = json.loads(response.text)
          return params
        except:
          pass  
        



    #GET ALL USERS INFORNET BY CPF

    def getcpf(self, cpf, keyClube):
        
        try: 
          #==========================================  

          url = URIGETUSERS + "?search=" + str(cpf)
          
          

          headers = {
              'Accept': 'application/json',
              "Authorization": "Bearer " + keyClube
          }

          #========================================== 


          response = requests.request("GET", url,  headers=headers)
          params   = json.loads(response.text)
          return params["data"][0]    
          
        except:
          pass  
        


    #AUTORIZAR USUARIO PARA CADASTRO VIA CPF

    def autorizar(self, cpf, keyClube):
        
        if keyClube != None or keyClube !="":


          try:
              #==========================================  
              url = URICLUBEAUTORIZED

              payload = {

                "value": str(cpf).replace(" ","").replace(".","")

              }

              headers = {

                  'Accept': "application/json",
                  "Authorization": "Bearer " + keyClube,
                  'Content-Type': "application/json"

              }

        
        
              #========================================== 

              response = requests.post(url,headers=headers,json=payload,)
              params   = json.loads(response.text)
              return params 

          except:
              print("KEY NOT ACEPT FROM LOGIN INFORNET")
              pass      

        else:
            print("KEY NOT ACEPT FROM LOGIN INFORNET")







    # CADASTRAR USUARIO APÓS AUTORIZAÇÃO

    def cadastro(self, name, date, cpf, agenda, especialidade, telefone, email, keyClube):
        

        try: 
          cpfs_ = str(cpf).replace(" ","").replace(".","").replace("-","")
          # #==========================================  
          url = URINEWUSER

          
          payload = {

            "name"      : str(name),
            "email"     : str(email),
            "birth_date": str(date),
            "cellphone" : "(99)99999-9999",
            "newsletter": True,
            "sms"       : True,
            "whatsapp"  : True,
            "password"  : cpfs_,
            "identifier": cpfs_,
            "cpf"       : cpfs_,
            "membersLimitReached": "string" 
          }
          


          #========================================== 

          
          headers = {
              "Content-Type": "application/json",
              "User-Agent": "insomnia/2023.5.8",
              "Accept": "application/json",
              "Authorization": "Bearer " + keyClube
          }
          
    
          #========================================== 

          response = requests.request("POST", url, json=payload, headers=headers)
          params   = json.loads(response.text)
          return params["id"]

        except:
          pass    
    





    # ATUALIZAR USUARIO APOS RECEBER ID(CADASTRADO)

    def update(self,name, situacao, cpf, idClube, keyClube):
          
        try:
          
          cpfs_ = str(cpf).replace(" ","").replace(".","").replace("-","")
          #==========================================  
          url = URIUPDATEUSER + str(idClube)

          payload = {

          "name": name,
          "active":situacao

          }
    
          headers = {
              "Content-Type": "application/json",
              "User-Agent": "insomnia/2023.5.8",
              "Authorization": "Bearer " + keyClube
          }
          #========================================== 
          response = requests.request("PUT", url, json=payload, headers=headers)
          params   = json.loads(response.text)
          return params

        except:
          pass  
  




    #AUTORIZAR USUARIO PARA CADASTRO VIA CPF

    def delete(self, idClube, keyClube):
        
        if keyClube != None or keyClube !="":


          try:
              #==========================================  
              url = URIUPDATEUSER + str(idClube)

              headers = {

                  'Accept': "application/json",
                  "Authorization": "Bearer " + keyClube,
                  'Content-Type': "application/json"

              }

        
        
              #========================================== 

              response = requests.request("DELETE", url, headers=headers)
              params   = json.loads(response.text)
              return params 

          except:
              print("KEY NOT ACEPT FROM LOGIN INFORNET")
              pass      

        else:
            print("KEY NOT ACEPT FROM LOGIN INFORNET")



