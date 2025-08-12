import os
from datetime import datetime
import pytz
import time
from dotenv import load_dotenv
load_dotenv()

##############------------------------>>>>>
from classes.infornet import INFORNET
INFORNET_     = INFORNET()
INFORNETCNPJ  = os.getenv('INFORNETCNPJ')
##############------------------------>>>>>


############ CLUBE DE VANTAGENS
############ CONEXA

##########################INFORNET
while True:
   INFORNET_.infornet(INFORNETCNPJ)
   time.sleep(1800)  ### 30 minutos