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

## CLASSES

from classes.conn import CONN
connection_mysql =  CONN()

from classes.data import DATA
dataTables =  DATA()

from classes.redis import redis_server
r = redis_server
redis = r.URI()

from classes.key import key_acess
generate_key = key_acess

## CLASSES


class DATA_SAVE:

  
  def get_traccar_id(self,placa):
       
       CONNECT = connection_mysql.gpwrox() ## GET INTO GPWROX
       cursor = CONNECT.cursor()

       ## GPWROX
       result = "SELECT traccar_device_id FROM devices WHERE plate_number LIKE %s"
       data = (str(placa), )
   
       ## INSERT DATA FROM DATA MODELS
       cursor.execute(result, data)
       ## INSERT DATA FROM DATA MODELS

       by_id = cursor.fetchall()
       for id in by_id:

          received = str(id).replace(",)", "")
          received_data = received.replace("(","")
          return received_data

  
  def get_email(self,email,user):
       
       CONNECT = connection_mysql.gpwrox() ## GET INTO GPWROX
       cursor = CONNECT.cursor()

       ## GPWROX
       result = "SELECT email FROM users WHERE email = %s or nome  = %s"
       data = (str(email), str(user))
   
       ## INSERT DATA FROM DATA MODELS
       cursor.execute(result, data)
       ## INSERT DATA FROM DATA MODELS

       by_id = cursor.fetchall()
       for id in by_id:

          received      = str(id).replace(",)", "")
          received_data = received.replace("(","")
          email_        = received_data.replace("'","")
          return email_

 

  def active_vehicles(self,traccar_id, codigo):
       CONNECT = connection_mysql.gpwrox() 
       cursor = CONNECT.cursor()

       ## TRACCAR
       result = "UPDATE devices SET active = %s WHERE traccar_device_id LIKE %s"
       data = (int(codigo), int(traccar_id))
   
       ## INSERT DATA FROM DATA MODELS
       cursor.execute(result, data)
       ## INSERT DATA FROM DATA MODELS
       CONNECT.commit()
       
       row = cursor.rowcount, "veiculo ativo"
       return "OK"





   ##############SESSÃO VEICULOS E USUÁRIOS
   ##############SESSÃO VEICULOS E USUÁRIOS
   ##############SESSÃO VEICULOS E USUÁRIOS


  def usuarios(self,codigo_associado, rg_associado, data_expedicao_rg, orgao_expedidor_rg, data_nascimento, sexo, cnh, categoria_cnh, logradouro, numero, complemento, bairro, cidade, estado, cep, email, email_auxiliar, user, telefone, whastapp, cpf, data_cadastro_associado, data_contrato_associado, hora_contrato_associado):
   
       CONNECT = connection_mysql.gpworx() ## insert into gpwroxWEB

       cursor  = CONNECT.cursor()

       result = "INSERT INTO users (active,group_id,manager_id,billing_plan_id,map_id,devices_limit,nome,email,password,phone_number,remember_token,subscription_expiration,loged_at,api_hash,api_hash_expire,available_maps,sms_gateway_app_date,sms_gateway_params,open_geofence_groups,open_device_groups, week_start_day,top_toolbar_open,map_controls,created_at,updated_at,unit_of_altitude,lang,unit_of_distance,unit_of_capacity,timezone_id,sms_gateway,sms_gateway_url,settings,email_verified_at) VALUES  ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s) on duplicate key update email = VALUES(email)"
       data   =  dataTables.usersData(codigo_associado, rg_associado, data_expedicao_rg, orgao_expedidor_rg, data_nascimento, sexo, cnh, categoria_cnh, logradouro, numero, complemento, bairro, cidade, estado, cep, email, email_auxiliar, user, telefone, whastapp, cpf, data_cadastro_associado, data_contrato_associado, hora_contrato_associado)

       cursor.execute(result, data)

       CONNECT.commit()
       
       row = cursor.rowcount, "user saved."

       id = cursor.lastrowid

       return id


  
  def traccar(self,codigo_veiculo, placa, chassi, renavam, codigo_associado, codigo_tipo, codigo_categoria, tipo, categoria, marca, modelo, cpf_associado, rg_associado, nome_associado, codigo_situacao, codigo_voluntario, whatsapp, email):

       print("SALVANDO DADOS NO TRACCAR:::: E PEGANDO ID")
       CONNECT = connection_mysql.traccar() ## insert into TRACCAR
       cursor  = CONNECT.cursor()

       ## TRACCAR
       result = "INSERT INTO devices (name, uniqueId, latestPosition_id, lastValidLatitude, lastValidLongitude, other, speed, time, device_time, server_time,ack_time,altitude,course, power,address,protocol,latest_positions, moved_at,stoped_at,engine_on_at,engine_off_at,engine_changed_at,database_id) VALUES  (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key update uniqueId = VALUES(uniqueId)"
       data   =  dataTables.traccarDesvicesData(codigo_veiculo, placa, chassi, renavam, codigo_associado, codigo_tipo, codigo_categoria, tipo, categoria, marca, modelo, cpf_associado, rg_associado, nome_associado, codigo_situacao, codigo_voluntario, whatsapp, email)
   
       ## INSERT DATA FROM DATA MODELS
       cursor.execute(result, data)
       ## INSERT DATA FROM DATA MODELS
       CONNECT.commit()
     
       row = cursor.rowcount, "traccar save"

       id = cursor.lastrowid

       return id


  def veiculos(self,codigo_veiculo, id, placa, chassi, renavam, codigo_associado, codigo_tipo, codigo_categoria, tipo, categoria, marca, modelo, cpf_associado, rg_associado, nome_associado, codigo_situacao, codigo_voluntario, whatsapp, email):
       print("SAVED GPWROX:::: no GPWROX WEB")

       
       CONNECT = connection_mysql.gpwrox_WEB() ## insert into gpwroxWEB

       cursor = CONNECT.cursor()
       
       print("SALVANDO DADOS")
       result = "INSERT INTO devices (user_id, current_driver_id, timezone_id, traccar_device_id, icon_id , icon_colors , active , deleted ,name ,  imei , fuel_measurement_id , fuel_quantity , fuel_price , fuel_per_km , sim_number , msisdn , device_model , plate_number , vin ,  registration_number , object_owner , tabela_fipe , additional_notes , expiration_date , sim_expiration_date , sim_activation_date , installation_date , tail_color , tail_length , engine_hours , detect_engine , min_moving_speed , min_fuel_fillings , min_fuel_thefts , snap_to_road  , gprs_templates_only , valid_by_avg_speed , parameters , currents , created_at , updated_at , forward , device_type_id , app_uuid , app_tracker_login ) VALUES  (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) on duplicate key update imei = VALUES(imei)"
       data   =  dataTables.vehiclesData(codigo_veiculo, id, placa, chassi, renavam, codigo_associado, codigo_tipo, codigo_categoria, tipo, categoria, marca, modelo, cpf_associado, rg_associado, nome_associado, codigo_situacao, codigo_voluntario, whatsapp, email)
       
       print(data)
       ## INSERT DATA FROM DATA MODELS
       cursor.execute(result, data)
       ## INSERT DATA FROM DATA MODELS
       CONNECT.commit()
       
       row = cursor.rowcount, "gpworx save"

       id = cursor.lastrowid
   
       return id 


   ##############SESSÃO VEICULOS E USUÁRIOS
   ##############SESSÃO VEICULOS E USUÁRIOS
   ##############SESSÃO VEICULOS E USUÁRIOS