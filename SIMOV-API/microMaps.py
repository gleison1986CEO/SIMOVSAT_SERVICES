import os
from datetime import datetime
import pytz
import time


##############------------------------>>>>>
from classes_jobs.data import DATA
DATA_ = DATA()
##############------------------------>>>>>


while True:

   time.sleep(15)
   now   = datetime.now()

   ###############//////////////////////////// ATIVOS

   ## TEMPO PARA RODAR ATUALIZAÇÃO DOS MAPAS
   maps          = now.replace(hour = int(7),  minute = int(00))
   maps1         = now.replace(hour = int(12), minute = int(00))
   maps2         = now.replace(hour = int(17), minute = int(00))
   maps3         = now.replace(hour = int(21), minute = int(00))
   maps4         = now.replace(hour = int(3),  minute = int(00))
   ## TEMPO PARA RODAR ATUALIZAÇÃO DOS MAPAS

   if maps == now:
      try:
        DATA_.dataEXECUTEGET()
      except:
        DATA_.dataEXECUTEGET()   


   elif maps1 == now:
      try:
        DATA_.dataEXECUTEGET()
      except:
        DATA_.dataEXECUTEGET()  


   elif maps2 == now:
      try:
        DATA_.dataEXECUTEGET()
      except:
        DATA_.dataEXECUTEGET()  


   elif maps3 == now:
      try:
        DATA_.dataEXECUTEGET()
      except:
        DATA_.dataEXECUTEGET()      


   elif maps4 == now:
      try:
        DATA_.dataEXECUTEGET()
      except:
        DATA_.dataEXECUTEGET()      


##################### JESUS E SENHOR
#########################################################################################################