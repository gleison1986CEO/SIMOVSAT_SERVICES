import os
from datetime import datetime
import pytz
import time
from dotenv import load_dotenv
load_dotenv()



##############------------------------>>>>>
from classes.hinova import HINOVA
HINOVA_     = HINOVA()
CODIGO      = os.getenv('INFORNETCNPJ')
PAGINACAO   = os.getenv('INFORNETCNPJ')
QUANTIDADE  = os.getenv('INFORNETCNPJ')
INICIO      = os.getenv('INFORNETCNPJ')
FIM         = os.getenv('INFORNETCNPJ')
TOTAL       = os.getenv('INFORNETCNPJ')
##############------------------------>>>>>



######################### PEGANDO USUARIOS E BOLETOS HINOVA 
#########################
#########################
#########################
while True:
   
   time.sleep(10)
   now   = datetime.now()
   date  = now.strftime("%Y-%m-%d")


   times         = now.replace(hour = int(14),  minute = int(6))
   print(times)
   print(now)
   if times == now:
            print("RODANDO VERIFICAÇÃO DE BOLETOS")
            try:
                  ## DADOS PARA RESGATAR BOLETOS
                  codigo_situacao       = "1"
                  inicio_paginacao      = "0"
                  quantidade_por_pagina = "1000"
                  data_inicio           = "2016-01-01" ## DATA DE TODOS OS USUARIOS CADASTRADOS NA PLATAFORMA HINOVA
                  data_fim              =  date  
                  total                 = "100"
                  ## DADOS PARA RESGATAR BOLETOS

                  HINOVA_.boletos(codigo_situacao, inicio_paginacao, quantidade_por_pagina, total, data_inicio, data_fim)
                  time.sleep(166400)
            except:
                  print("ERROR BOLETOS")
                  pass


  #########################
  #########################
  #########################
  #########################
  #########################