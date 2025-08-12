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


from repository.insert import SQLSERVER
database_    =    SQLSERVER()


###############LOAD ENV
load_dotenv()

BEARTOKEN      = os.getenv('BEARTOKEN')
USERHINOVA     = os.getenv('USERHINOVA')
PASSWORDHINOVA = os.getenv('PASSWORDHINOVA')
ENDPOINTAUTH   = os.getenv('ENDPOINTAUTH')
COOKIE         = os.getenv('COOKIE')
MSGDATA        = os.getenv('MSGDATA')
###############LOAD ENV


class key_acess():
  def key_hinova():

    payload = {

      "usuario": USERHINOVA,
      "senha": PASSWORDHINOVA 

    } 
  
    headers = {

      "cookie": COOKIE,
      "Content-Type": "application/json",
      "Authorization": "Bearer " + BEARTOKEN
    
    }


    response = requests.request("POST", ENDPOINTAUTH, json=payload, headers=headers)
    key = response.text
    key_remove = re.sub('[^A-Za-z0-9]+', '', key)
    ch_remove = MSGDATA
    out       = key_remove.split(ch_remove, 1)[1]
    database_.KEY(out)
    return out

 
