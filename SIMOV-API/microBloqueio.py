import os
from datetime import datetime
import pytz
import time


##############------------------------>>>>>
from classes_jobs.bloqueios import BLOCK
JOBS_ = BLOCK()
##############------------------------>>>>>




while True:
   
   time.sleep(1)
   now   = datetime.now()
   print("VERIFICANDO JOBS")
   time.sleep(10)

   # ########################## COOPERATIVAS
   


   # ASSOCAR           = "1"
   # DANIELE_COMERCIAL = "25"
   # GILBERTO_BISPO    = "13"
   # IASMIN_NASCIMENTO = "42"
   # ISMAEL_AUTOMOVEIS = "24"
   # HOSMAN               = "14"
   # KEITH_ROSANA         = "40"
   # KEITH_MONSORES       = "44"
   # LEADS_INTERIOR       = "58"
   # ARCOS_FERREIRA       = "6"
   # NATASHA_TUANE        = "27" 
   # PABLO_ANJOS          = "17"
   # QUIVIA_FEITOSA       = "47"
   # SERGIO_ROCHA         = "10"
   # TANIA_MARA           = "18"
   # THIAGO_ANJOS         = "15"
   # VALERIA              = "48"
   
   
   # ########################## COOPERATIVAS

   # #########################REGIONAIS
   # SOMATTO_BENEFICIOS  = "1"
   # SOMATTO_RESENDE     = "9"
   # SOMATTO_REDONDA     = "8"
   # #########################REGIONAIS
   
   
   
   ##############################################
   ##############################################

   def execute_function_cooperativas(regionais):
            
         try: 

               list = [47, 48, 25, 27, 13, 42, 15, 24, 14, 40, 44, 6, 58, 17, 47, 10, 18, 1]
               for coop in list:

                  codigo_situacao = "4"
                  regional        = str(regionais)
                  cooperativa     = str(coop)
                  fipe            = "1.0000"
                  ######## caso nao funciona alterar FIPE
                  
                  print("EXEC INADINPLEMENTES:::: " + "  COOPERATIVA::" + str(coop) + "  REGIONAL::" +  str(regionais))
                  JOBS_.inadimplentes_(codigo_situacao, regional, cooperativa, fipe)
                  time.sleep(18000)

                  ##############################

                  codigo_situacao = "2"
                  regional        = str(regionais)
                  cooperativa     = str(coop)
                  fipe            = "1.0000"
                  ######## caso nao funciona alterar FIPE
                  
                  print("EXEC INATIVOS:::: " + "  COOPERATIVA::" + str(coop) + "  REGIONAL::" +  str(regionais))
                  JOBS_.inativos_(codigo_situacao, regional, cooperativa, fipe)
                  time.sleep(18000)

                  ##############################
                  codigo_situacao = "1"
                  regional        = str(regionais)
                  cooperativa     = str(coop)
                  fipe            = "1.0000"
                  ######## caso nao funciona alterar FIPE
                  
                  print("EXEC ATIVOS:::: " + "  COOPERATIVA::" + str(coop) + "  REGIONAL::"  + str(regionais))
                  JOBS_.ativos_(codigo_situacao, regional, cooperativa, fipe)
                  time.sleep(18000)

                  ##############################
         except:
            print("ERROR LIST COOPERTAIVAS E REGIONAIS")
   

   ##############################################
   ##############################################


   #########NUMERO DE REGIONAIS
   list = [9, 8, 1]
   #########NUMERO DE REGIONAIS

   #####EXCUTANDO FUNÇÃO REGIONAIS E COOPERATIVAS
   i = 0
   #####EXCUTANDO FUNÇÃO REGIONAIS E COOPERATIVAS

   while i < len(list):
      regionais = list[i]
      execute_function_cooperativas(regionais)
      i += 1
      print("REINICIANDPO PROCESO AGUARDE...")
      time.sleep(60)
   
   #####EXCUTANDO FUNÇÃO REGIONAIS E COOPERATIVAS



# Kys3647
# Knr5252
# Kpk9948
# RJY6D93
# PXJ5A40
# KOR4J13
# RJD8E83
# 👆🏼 veículos capital que não está inativos no SIMOVSAT
# RJI5J30
# RJY6D93
# 👆🏼 motos acima de $5.000