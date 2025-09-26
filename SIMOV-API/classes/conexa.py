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
from datetime import datetime


from repository.insert import SQLSERVER
from repository.query  import QUERY
from extra_classe.pacientes import PACIENTES

database_query   = QUERY()
database_        = SQLSERVER()
conexaPacientes  = PACIENTES()

class CONEXA:
    def pacientesativos(self,  name, date, cpf, agenda, especialidade, telefone, email):

        try:    
                cpfs = str(cpf).replace(" ","").replace("-","").replace(".","")
                situacao = "ATIVO"
                out = database_query.CONEXABYCPF(cpfs)
                if out == "None":
                   database_.CONEXA(situacao, name, date, cpfs, agenda, especialidade, telefone, email)
                   return "Ok"
                   
                else:
                   print(cpfs)
                   print("JA EXISTE")
                   return "Ok"

        except:
            pass        



    def pacientesinativos(self, name, date, cpf, agenda, especialidade, telefone, email):

        try:    
                cpfs = str(cpf).replace(" ","").replace("-","").replace(".","")
                situacao = "INATIVO"
                out = database_query.CONEXABYCPF(cpfs)
                if out == "None":
                   database_.CONEXA(situacao, name, date, cpfs, agenda, especialidade, telefone, email)
                   return "Ok"
                   
                else:
                   return "Ok"

        except:
            pass   



    def pacientes(self):

        try:
            
            conexa = database_query.CONEXA()
            all = len(conexa)
            co = all-2
            while co >= 0:
                situacao= conexa[co][1].replace(" ","")
                name    = conexa[co][2].replace(" ","")
                date    = conexa[co][3]
                cpf     = conexa[co][4].replace(" ","")
                agenda  = conexa[co][5]
                email   = conexa[co][6]
                especialidade  = conexa[co][7]
                telefone= conexa[co][8]
                status  = conexa[co][9]
                whatsapp= telefone.replace(" ","").replace("-","").replace("+","")
    
                if situacao == "ATIVO":

                    try:

                        pacientesExistentes = conexaPacientes.get(cpf)
                        id                  = pacientesExistentes["object"]["patient"]["id"]
                        print("##############")
                        print(pacientesExistentes)
                        print(co)
                        print("##############\n")
                        if pacientesExistentes["status"] == 200:
                            
                            conexaPacientes.update(id, email)
                            time.sleep(6)
                            conexaPacientes.ativando(id) 
       

                        else:
                            conexaPacientes.post(name, date, cpf, agenda, especialidade, whatsapp, email)
                            time.sleep(6)
                            pacientesExistentes  = conexaPacientes.get(cpf)
                            ids                  = pacientesExistentes["object"]["patient"]["id"]
                            time.sleep(3)
                            conexaPacientes.ativando(ids)
                    except:
                        pass 

                elif situacao == "INATIVO":  
                    try:
                        pacientesExistentes = conexaPacientes.get(cpf)
                        id                  = pacientesExistentes["object"]["patient"]["id"]

                        if pacientesExistentes["status"] == 200:
                        
                            conexaPacientes.update(id, email)
                            time.sleep(6)
                            conexaPacientes.inativando(id)

                        else:

                            conexaPacientes.post(name, date, cpf, agenda, especialidade, whatsapp, email)
                            time.sleep(6)
                            pacientesExistentes  = conexaPacientes.get(cpf)
                            ids                  = pacientesExistentes["object"]["patient"]["id"]
                            time.sleep(3)
                            conexaPacientes.inativando(ids)
                    except:
                        pass 
     
                co = co - 1

        except:
            pass        
