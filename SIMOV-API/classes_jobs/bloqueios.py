import requests
from dotenv import load_dotenv
import os
from retry import retry
import logging
import datetime

#######################---------->>>>>
from classes.logs        import log_api
#######################---------->>>>>

####################/////////////////////////-------->>>
LOGS_BY_SYSTEM  =  log_api()
####################/////////////////////////-------->>>

######################
data_now        = f"{datetime.datetime.now():%Y-%m-%d}"
######################




###############LOAD ENV
load_dotenv()
ENDPOINTBLOQUEIOS         = os.getenv('ENDPOINTBLOQUEIOS')
ENDPOINTVEICULOS          = os.getenv('ENDPOINTVEICULOS')
BEARTOKEN      = os.getenv('BEARTOKEN')
USERHINOVA     = os.getenv('USERHINOVA')
PASSWORDHINOVA = os.getenv('PASSWORDHINOVA')
COOKIE         = os.getenv('COOKIE')
MSGDATA        = os.getenv('MSGDATA')
###############LOAD ENV

class BLOCK:
	
	def ativos(self):

		res = requests.post(ENDPOINTBLOQUEIOS, json=

		{
			"usuario": USERHINOVA,
			"senha"  : PASSWORDHINOVA,
			"codigo_situacao" : "1",
			"inicio_paginacao" : "0",
			"quantidade_por_pagina" : "5000"
		}
		)
		if res.ok:
			print(res.json())

			#######LOGS//////////////////
			formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
			LOGS_BY_SYSTEM.LOGSYS("logs/ativos.log", formatLOG , str(res.json()), logging.INFO)
			#######LOGS//////////////////
		
		return "NONE"	

			
	
	def inativos(self):

		res = requests.post(ENDPOINTBLOQUEIOS, json=
		{
			"usuario": USERHINOVA,
			"senha"  : PASSWORDHINOVA,
			"codigo_situacao" : "2",
			"inicio_paginacao" : "0",
			"quantidade_por_pagina" : "5000"
		}
		)
		if res.ok:
			print(res.json())

			#######LOGS//////////////////
			formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
			LOGS_BY_SYSTEM.LOGSYS("logs/inativos.log", formatLOG , str(res.json()), logging.INFO)
			#######LOGS//////////////////

		return "NONE"	

			

	
	def inadimplementes(self):

		res = requests.post(ENDPOINTBLOQUEIOS, json=
		{
			"usuario": USERHINOVA,
			"senha"  : PASSWORDHINOVA,
			"codigo_situacao" : "4",
			"inicio_paginacao" : "0",
			"quantidade_por_pagina" : "5000"
		}
		)
		if res.ok:
			print(res.json())

			#######LOGS//////////////////
			formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
			LOGS_BY_SYSTEM.LOGSYS("logs/inadimplementes.log", formatLOG , str(res.json()), logging.INFO)
			#######LOGS//////////////////
		
		return "NONE"	

			

	def inadimplentes_(self, codigo_situacao, regional, cooperativa, fipe):
		res = requests.post(ENDPOINTVEICULOS, json=

		{
				"usuario": USERHINOVA,
				"senha"  : PASSWORDHINOVA,
				"codigo_situacao" : str(codigo_situacao),
				"inicio_paginacao" : "0",
				"quantidade_por_pagina" : "5000",
				"data_inicio":"2021-01-01",
				"data_fim":str(data_now),
				"codigo_regional":str(regional),
				"codigo_cooperativa":str(cooperativa),
				"codigo_tipo_veiculo":"9",
				"valor_fipe":str(fipe),
				"cilindrada":"0"
				
		}

		)
		if res.ok:
			print(res.json())
		
		return "NONE"	

		

	def inativos_(self, codigo_situacao, regional, cooperativa, fipe):
		res = requests.post(ENDPOINTVEICULOS, json=

		{
				"usuario": USERHINOVA,
				"senha"  : PASSWORDHINOVA,
				"codigo_situacao" : str(codigo_situacao),
				"inicio_paginacao" : "0",
				"quantidade_por_pagina" : "5000",
				"data_inicio":"2021-01-01",
				"data_fim":str(data_now),
				"codigo_regional":str(regional),
				"codigo_cooperativa":str(cooperativa),
				"codigo_tipo_veiculo":"9",
				"valor_fipe":str(fipe),
				"cilindrada":"0"
				
		}

		)
		if res.ok:
			print(res.json())
		
		return "NONE"	

	

	def ativos_(self, codigo_situacao, regional, cooperativa, fipe):


		res = requests.post(ENDPOINTVEICULOS, json=

		{
				"usuario": USERHINOVA,
				"senha"  : PASSWORDHINOVA,
				"codigo_situacao" : str(codigo_situacao),
				"inicio_paginacao" : "0",
				"quantidade_por_pagina" : "5000",
				"data_inicio":"2022-01-01",
				"data_fim":str(data_now),
				"codigo_regional":str(regional),
				"codigo_cooperativa":str(cooperativa),
				"codigo_tipo_veiculo":"9",
				"valor_fipe":str(fipe),
				"cilindrada":"0"
		}
		)
		if res.ok:
			print(res.json())
		
		return "NONE"	


