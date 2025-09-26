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


from extra_classe.infornet     import INFORNETPASS
from classes.conexa            import CONEXA
from classes.tratamento        import TRATAMENTO
from extra_classe.clube        import CLUBEPASS
from classes.clube             import CLUBE

clubeCadastro = CLUBE()
clubePass     = CLUBEPASS()
infornetPass  = INFORNETPASS()
conexaPass    = CONEXA()
tratamento    = TRATAMENTO()

class INFORNET:

    def infornet(self, cnpj):



        
        keyClube      = clubePass.auth()
        usersClube    = clubePass.get(keyClube)
        key           = infornetPass.post(cnpj)
        uri           = infornetPass.postveiculos(cnpj, key)
        params        = infornetPass.listar(uri[0])

        x = len(params) - 1
        while x >= 0:

            try: 
                print(x)
                dataVeiculos        = params[x]
                dataClube           = usersClube["data"]
                veiculos            = tratamento.infornetveiculos(dataVeiculos)

                if veiculos[6] == "ATIVO" and "ASSISTENCIA" in str(veiculos[7]):
                    conexaPass.pacientesativos(veiculos[0], veiculos[1], veiculos[2], veiculos[3], veiculos[4], veiculos[5], veiculos[8])
                    


                elif veiculos[6] == "ATIVO" and "CLUBE" in str(veiculos[7]):
                    clubeCadastro.clubesativos(veiculos[0], veiculos[1], veiculos[2], veiculos[3], veiculos[4], veiculos[5], veiculos[8], keyClube)


            except:
                pass  
            
            x = x - 1 
                  
  
      