import os
from datetime import datetime
import pytz
import time
from dotenv import load_dotenv
load_dotenv()

##############------------------------>>>>>
from classes.conexa import CONEXA
CONEXA_     = CONEXA()
##############------------------------>>>>>


############ CLUBE DE VANTAGENS
############ CONEXA

##########################INFORNET
while True:

   CONEXA_.pacientes()
   time.sleep(7200)  ### 2 HORAS 