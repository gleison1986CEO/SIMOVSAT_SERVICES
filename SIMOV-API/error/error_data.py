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

class ERROR_DATA:


    def boletoserror(self, cpf):
    
        
        out = {

            "status":  True,
            "cpf" :  cpf,
            "type"  : "verificação de boleto error",

        }


        return out
    def boletos(self, data):

        out = data["mensagem"]

        return out


    def ativos_hinova(self,placa):

        out = {

            "status":  True,
            "placa" :  placa,
            "type"  : "placas ativas hinova",
            "error" : "consulta não existe"

        }

        return out



    def ativos_simovsat(self,placa):

        out = {

            "status": True,
            "placa" : placa,
            "type"  : "placas ativas simovsat",
            "error" : "consulta não existe"

        }

        return out



    def inadimplentes_hinova(self,placa):

        out= {

            "status": True,
            "placa" : placa,
            "type"  : "placas inadimplentes hinova",
            "error" : "consulta não existe"

        }

        return out




    def inadimplentes_simovsat(self,placa):

        out = {

            "status":  True,
            "placa" :  placa,
            "type"  : "placas inadimplentes simovsat",
            "error" : "consulta não existe"

        }

        return out


    def produtos(self):

        out = {

            "status":  True,
            "type"  : "produtos hinova",
            "error" : "consulta não existe"

        }

        return out


    def voluntarios(self):


        out = {

            "status":  True,
            "type"  : "voluntarios hinova",
            "error" : "consulta não existe"

        }

        return out


    def cooperativas(self):


        out = {

            "status":  True, 
            "type"  : "cooperativas hinova",
            "error" : "consulta não existe"

        }

        return out


        

    def situacao(self):


        out = {

            "status":  True,
            "type"  : "situacao hinova",
            "error" : "consulta não existe"

        }

        return out


    def regionais(self):


        out = {

            "status":  True,
            "type"  : "regionais hinova",
            "error" : "consulta não existe"

        }

        return out



    def veiculos_importados(self):


        out = {

            "status":  True,
            "type"  : "veiculos importados simovsat",
            "error" : "consulta não existe"

        }

        return out    


    def usuarios_importados(self):


        out = {

            "status":  True,
            "type"  : "usuarios importados simovsat",
            "error" : "consulta não existe"

        }

        return out          

   
    def movida_locations(self, placa):


        out = {

            "status":  True,
            "placa" :  placa,
            "type"  : "get user location movida",
            "error" : "consulta não existe"

        }

        return out               



    def movida_link(self, placa):


        out = {

            "status":  True,
            "placa" :  placa,
            "type"  : "link assitencia veicula movida",
            "error" : "consulta não existe"

        }

        return out                      



  ##########///////////////////////POSTS      

 
    def regionais_post(self):


        out = {

            "status":  True,
            "type"  : "post regionais",
            "error" : "post gerar regionais"

        }

        return out        

    def cooperativa_post(self):


        out = {

            "status":  True,
            "type"  : "post cooperativa",
            "error" : "post gerar cooperativa"

        }

        return out               
        

    def voluntarios_post(self):


        out = {

            "status":  True,
            "type"  : "post voluntarios",
            "error" : "post gerar voluntarios"

        }

        return out                
          

    
    def produto_post(self):


        out = {

            "status":  True,
            "type"  : "post produto",
            "error" : "post gerar produto"

        }

        return out  
                     
         
    def situacao_post(self):


        out = {

            "status":  True,
            "type"  : "post situacao ",
            "error" : "post gerar situacao "

        }

        return out  



    def veiculos_filter_import_post(self):    

        out = {

            "status":  True,
            "type"  : "post veiculos_filter_import",
            "error" : "post importar veiculos_filter_import"

        }

        return out


 
    def veiculos_filter_post(self):    

        out = {

            "status":  True,
            "type"  : "post veiculos_filter",
            "error" : "post gerar veiculos_filter"

        }

        return out        


    def usuarios_post(self):    

        out = {

            "status":  True,
            "type"  : "post usuarios",
            "error" : "post importar usuarios"

        }

        return out               



    def consulta_veiculos(self):    

        out = {

            "status":  True,
            "type"  : "get veiculos por parametros regional, cooperativa, situação",
            "error" : "get lista de veiculos não existe, faça uma consulta veiculos filter ou import"

        }

        return out                     