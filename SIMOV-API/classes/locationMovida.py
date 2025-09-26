
  
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
import mysql.connector


class STA():
  def batery(self, init5):
    
    if '"batterylevel":' in init5:
     
      ch1 = '"batterylevel":'
      batterylevel = init5.split(ch1, 1)[1]
      result_batterylevel = batterylevel.split(ch1, 1)[0]

      result = result_batterylevel

      return result
  
    else:
      return "data null"




  def totaldistance(self, init5):
    
    if '"totaldistance":' in init5:
  
   
      ch2 = '"totaldistance":'
      totaldistance = init5.split(ch2, 1)[1]
      result_totaldistance = totaldistance.split(ch2, 1)[0]

      result = result_totaldistance
      
      return  result
    else:
      return "data null"     




  def motion(self, init5):
    
    if '"motion":' in init5:
  
      ch3 = '"motion":'
      motion = init5.split(ch3, 1)[1]
      result_motion = motion.split(ch3, 1)[0]

      result = result_motion

      return  result





  def ignition(self, init5):
    
    if '"ignition":' in init5:

   
      ch4 = '"ignition":'
      ignition = init5.split(ch4, 1)[1]
      result_ignition = ignition.split(ch4, 1)[0]

      result = result_ignition
 
      return result

    else:
      return "data null"  





  def charge(self, init5):
    
    if '"charge":' in init5:

      ch5 = '"charge":'
      charge = init5.split(ch5, 1)[1]
      result_charge = charge.split(ch5, 1)[0]

      result =  result_charge

      return result

    else:
      return "data null"    

  




  def blocked(self, init5):
    
    if '"blocked":' in init5:
   
      ch6 = '"blocked":'
      blocked = init5.split(ch6, 1)[1]
      result_blocked = blocked.split(ch6, 1)[0]

      result = result_blocked

      return result

    else:
      return "data null"                 