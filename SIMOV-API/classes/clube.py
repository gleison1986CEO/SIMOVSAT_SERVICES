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

from extra_classe.clube   import CLUBEPASS
from repository.query     import QUERY
from repository.insert    import SQLSERVER
database_query   = QUERY()
database_        = SQLSERVER()
clubePass        = CLUBEPASS()

class CLUBE:



    def clubesativos(self, name, date, cpf, agenda, especialidade, telefone, email, keyClube):
        try:
            cpfs = str(cpf).replace(" ","").replace("-","").replace(".","")
            situacao = "ATIVO"
            out = database_query.CLUBEBYCPF(cpfs)
            if out == "None":
               database_.CLUBE(situacao, name, date, cpfs, agenda, especialidade, telefone, email)
               return "Ok"
            else: 
               print(cpfs)
               print("JA EXISTE")
               return "Ok"

        except:
            pass    
            
        

    def clubesinativos(self, name, date, cpf, agenda, especialidade, telefone, email, keyClube):
    
        try:
            cpfs = str(cpf).replace(" ","").replace("-","").replace(".","")
            situacao = "INATIVO"
            out = database_query.CLUBEBYCPF(cpfs)
            if out == "None":
               database_.CLUBE(situacao, name, date, cpfs, agenda, especialidade, telefone, email)
               return "Ok"
            else:
               return "Ok"

        except:
            pass   








    def clube(self):

        try:

            key      = clubePass.auth()
            clube    = database_query.CLUBE()

            all      = len(clube)
            co       = all-2
            while co >= 0:

                situacao= clube[co][1].replace(" ","")
                name    = clube[co][2].replace(" ","")
                date    = clube[co][3]
                cpf     = clube[co][4].replace(" ","")
                agenda  = clube[co][5]
                email   = clube[co][6]
                especialidade  = clube[co][7]
                telefone= clube[co][8]
                status  = clube[co][9]
                whatsapp= telefone.replace(" ","").replace("-","").replace("+","")

                

                if situacao == "ATIVO":
                    serchcpf   = clubePass.getcpf(cpf,  key) 
                    print("##############")
                    print(serchcpf)
                    print(co)
                    print("##############\n")
                    if serchcpf == None:
                        
                        clubePass.autorizar(cpf, key)
                        time.sleep(4)
                        Id_signup = clubePass.cadastro(name, date, cpf, agenda, especialidade, telefone, email, key)
                        clubePass.update(name, True, cpf, Id_signup, key)
                    
                    else:
                        
                        clubePass.update(name, True, cpf, serchcpf["id"], key)

                
                elif situacao == "INATIVO":  

                    serchcpf   = clubePass.getcpf(cpf,  key) 

                    if serchcpf == None:
                        
                        clubePass.autorizar(cpf, key)
                        time.sleep(4)
                        Id_signup = clubePass.cadastro(name, date, cpf, agenda, especialidade, telefone, email, key)
                        clubePass.update(name, False, cpf, Id_signup, key)
                    
                    else:
                        clubePass.update(name, False, cpf, serchcpf["id"], key)
                    
                   

     
                co = co - 1

        except:
            pass        



########### DELETE E UPDATE SENHA
# ## REMOVE USUARIOS E ADICIONAR NOVAMENTE
# clubePass.delete(serchcpf["id"], keyClube)
# clubePass.autorizar(cpf_search, keyClube)
# Id_signup = clubePass.cadastro(name, date, cpf, agenda, especialidade, telefone, email, keyClube)
# clubePass.update(name, True, cpf, Id_signup, keyClube)
# ## REMOVE USUARIOS E ADICIONAR NOVAMENTE