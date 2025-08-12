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




from classes.redis import redis_server
from classes.key      import key_acess
from classes.sendmessagem import WHATSAPP
from extra_classe.cooperativa import COOPERATIVA
from repository.insert import SQLSERVER
from extra_classe.boleto import BOLETO
from extra_classe.regionais import REGIONAIS
from extra_classe.produto import PRODUTO
from extra_classe.situacao import SITUACAO
from extra_classe.usuarios import USUARIOS
from extra_classe.veiculos import VEICULOS
from extra_classe.voluntarios import VOLUNTARIOS
from classes.tratamento import TRATAMENTO
from classes.verification  import VERIFICATION


##################################### INSTANCIAS

tratamento_data = TRATAMENTO()
usuarios_    =    USUARIOS()
boletos_     =    BOLETO()
cooperativa_ =    COOPERATIVA()
regionais_   =    REGIONAIS()
produto_     =    PRODUTO()
situacao_    =    SITUACAO()
veiculos_    =    VEICULOS()
voluntario_  =    VOLUNTARIOS()
whatsapp_    =    WHATSAPP()
database_    =    SQLSERVER()
verification_= VERIFICATION()

##################################### INSTANCIAS





class HINOVA():

  def boletos(self,codigo_situacao, inicio_paginacao, quantidade_por_pagina, total, data_inicio, data_fim):
      

      params         = usuarios_.listar(codigo_situacao, inicio_paginacao, quantidade_por_pagina, total, data_inicio, data_fim)
      time.sleep(10)
      tratamento     = tratamento_data.boletos(params, data_inicio, data_fim)

      return tratamento

      
  def usuarios(self,codigo_situacao, inicio_paginacao, quantidade_por_pagina, total, data_inicio, data_fim):
      

      params         = usuarios_.listar(codigo_situacao, inicio_paginacao, quantidade_por_pagina, total, data_inicio, data_fim)
      tratamento     = tratamento_data.usuarios(params, data_inicio, data_fim)

      return tratamento
     


  def veiculos_block(self, codigo_situacao, inicio_paginacao, quantidade_por_pagina):

      params = veiculos_.bloqueios(codigo_situacao, inicio_paginacao, quantidade_por_pagina)
      tratamento = tratamento_data.veiculos_block_tratamento(params)
      
      return tratamento



  def veiculos(self, codigo_situacao, inicio_paginacao, quantidade_por_pagina, data_inicio, data_fim):

      params = veiculos_.listar(codigo_situacao, inicio_paginacao, quantidade_por_pagina, data_inicio, data_fim)
      tratamento = tratamento_data.veiculos(params)
      return tratamento


  def veiculos_filter(self, codigo_situacao, inicio_paginacao, quantidade_por_pagina, codigo_regional, codigo_cooperativa, codigo_tipo_veiculo, valor_fipe, cilindrada, data_inicio, data_fim):
  

      cooperativa = cooperativa_.listar()
      produto = produto_.listar(codigo_regional, codigo_cooperativa, codigo_tipo_veiculo, valor_fipe, cilindrada)
      veiculo = veiculos_.listar(codigo_situacao, inicio_paginacao, quantidade_por_pagina, data_inicio, data_fim)





      total_veiculos     = len(veiculo["veiculos"])
      total_cooperativas = len(cooperativa)
      total_produtos     = len(produto)
      
      print(total_produtos)
      

       
      number_coop = 0  
      params = []

      for number_coop in range(int(total_cooperativas) - 1):
                 cooperativa_id = cooperativa[number_coop]["codigo_cooperativa"]
                
                 i = 0
                 while i <= int(total_veiculos) -1:

                    try:

                        data_cadastro = veiculo["veiculos"][i]["data_cadastro"]
                        cooperativa_veiculo_id = veiculo["veiculos"][i]["codigo_cooperativa"]

                        
                        if cooperativa_id == cooperativa_veiculo_id:

                            number_prodct = 0 
                            
                            for  number_coop in range(int(total_produtos) - 1):

                                 produto_id = produto[number_prodct]["codigo_produto"]
                                 codigo_regional_produto = produto[number_prodct]["regionais"][0]["codigo_regional"]
                                 valor_produto = produto[number_prodct]["valor_produto"]


                                  
                                 if valor_produto >= valor_fipe:
                                    params.append(i)
                                 else:
                                    print("valor  da taxa fipe não é igual ao produto ou maior que produto")
                           

                    except:
                            print("error ID")

                    i += 1  


      params[:] = list(dict.fromkeys(params)) ## ordenando lista do array removendo repetidoss
      time.sleep(2)
      tratamento = tratamento_data.veiculos_filter(params, codigo_situacao, veiculo, produto, codigo_cooperativa, cooperativa, codigo_regional, data_inicio, data_fim)
      time.sleep(2)
 
      return tratamento



  def veiculos_filter_import_data(self, codigo_situacao, inicio_paginacao, quantidade_por_pagina, codigo_regional, codigo_cooperativa, codigo_tipo_veiculo, valor_fipe, cilindrada, data_inicio, data_fim):
  

      cooperativa = cooperativa_.listar()
      produto = produto_.listar(codigo_regional, codigo_cooperativa, codigo_tipo_veiculo, valor_fipe, cilindrada)
      veiculo = veiculos_.listar(codigo_situacao, inicio_paginacao, quantidade_por_pagina, data_inicio, data_fim)





      total_veiculos     = len(veiculo["veiculos"])
      total_cooperativas = len(cooperativa)
      total_produtos     = len(produto)
      
      print(total_produtos)
      

       
      number_coop = 0  
      params = []

      for number_coop in range(int(total_cooperativas) - 1):
                 cooperativa_id = cooperativa[number_coop]["codigo_cooperativa"]
                
                 i = 0
                 while i <= int(total_veiculos) -1:

                    try:

                        data_cadastro = veiculo["veiculos"][i]["data_cadastro"]
                        cooperativa_veiculo_id = veiculo["veiculos"][i]["codigo_cooperativa"]

                        
                        if cooperativa_id == cooperativa_veiculo_id:

                            number_prodct = 0 
                            
                            for  number_coop in range(int(total_produtos) - 1):

                                 produto_id = produto[number_prodct]["codigo_produto"]
                                 codigo_regional_produto = produto[number_prodct]["regionais"][0]["codigo_regional"]
                                 valor_produto = produto[number_prodct]["valor_produto"]


                                  
                                 if valor_produto >= valor_fipe:
                                    params.append(i)
                                 else:
                                    print("valor  da taxa fipe não é igual ao produto ou maior que produto")
                           


                    except:
                            print("error ID")

                    i += 1  


      params[:] = list(dict.fromkeys(params)) ## ordenando lista do array removendo repetidos
      time.sleep(2)
      tratamento = tratamento_data.veiculos_filter_import(params, codigo_situacao, veiculo, produto, codigo_cooperativa, cooperativa, codigo_regional, data_inicio, data_fim)
      time.sleep(2)
      
      return tratamento



  def situacao(self):

      params = situacao_.listar()
      tratamento = tratamento_data.situacao(params)
      return tratamento




  def produto(self, codigo_regional, codigo_cooperativa, codigo_tipo_veiculo, valor_fipe, cilindrada):

      params = produto_.listar(codigo_regional, codigo_cooperativa, codigo_tipo_veiculo, valor_fipe, cilindrada)
      tratamento = tratamento_data.produto(params)
      
      return tratamento 




  def cooperativa(self):

      params = cooperativa_.listar()
      tratamento = tratamento_data.cooperativa(params)
      return tratamento




  def regionais(self):

      params = regionais_.listar()
      tratamento = tratamento_data.regional(params)
      return tratamento




  def voluntario(self):

      params = voluntario_.listar()
      tratamento = tratamento_data.voluntario(params)
      return tratamento





