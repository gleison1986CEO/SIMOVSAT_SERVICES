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

class DATA:
    def usersData(self,codigo_associado, rg_associado, data_expedicao_rg, orgao_expedidor_rg, data_nascimento, sexo, cnh, categoria_cnh, logradouro, numero, complemento, bairro, cidade, estado, cep, email, email_auxiliar, user, telefone, whastapp, cpf, data_cadastro_associado, data_contrato_associado, hora_contrato_associado):
        
        active =  1
        group_id = 2
        manager_id = "0"
        billing_plan_id = "0"
        map_id = "0"
        devices_limit = 5
        nome = str(user)
        email = str(email)
        password = str(cpf)
        phone_number = str(whastapp)
        remember_token = "$2y$04$X1q6E.3vhKJKREGTNU3cQOrgmGpiQH45ECLrJK7fpyohBi8YQ83ji"
        subscription_expiration = "0000-00-00"
        loged_at = "0000-00-00"
        api_hash = str(cpf)
        api_hash_expire = "0000-00-00"
        available_maps = 'a:3:{i:0;s:1:"2";i:1;s:2:"18";i:2;s:2:"19";}'
        sms_gateway_app_date =  "0000-00-00"
        sms_gateway_params = "1"
        open_geofence_groups = "1"
        open_device_groups = "1"
        week_start_day = 1
        top_toolbar_open = 1
        map_controls = "{}"
        created_at = "0000-00-00"
        updated_at = "0000-00-00"
        unit_of_altitude = "mt"
        lang = "en"
        unit_of_distance = "km"
        unit_of_capacity = "lt"
        timezone_id = 57
        sms_gateway = 0
        sms_gateway_url = "1"
        settings = "0"
        email_verified_at = "0000-00-00"

        time.sleep(1)
        
        data = (
               active,
               group_id,
               manager_id,
               billing_plan_id,
               map_id,
               devices_limit,
               nome,
               email,
               password,
               phone_number,
               remember_token,
               subscription_expiration,
               loged_at,
               api_hash,
               api_hash_expire,
               available_maps,
               sms_gateway_app_date,
               sms_gateway_params,
               open_geofence_groups,
               open_device_groups, 
               week_start_day,
               top_toolbar_open,
               map_controls,
               created_at,
               updated_at,
               unit_of_altitude,
               lang,
               unit_of_distance,
               unit_of_capacity,
               timezone_id,
               sms_gateway,
               sms_gateway_url,
               settings,
               email_verified_at)
               
        time.sleep(1)

        return data 




    def traccarDesvicesData(self,codigo_veiculo, placa, chassi, renavam, codigo_associado, codigo_tipo, codigo_categoria, tipo, categoria, marca, modelo, cpf_associado, rg_associado, nome_associado, codigo_situacao, codigo_voluntario, whatsapp, email):
        
        name = str(nome_associado)
        uniqueId = codigo_associado
        latestPosition_id = 179309
        lastValidLatitude = -22.886327833333333
        lastValidLongitude = -43.57927316666667
        other = "<info></info>"
        speed = 0.00
        time = "2023-08-09"
        device_time = "2023-08-09"
        server_time = "2023-08-09"
        ack_time = "2023-08-09"
        altitude =  0
        course = 0
        power = "1"
        address = "1"
        protocol = "gps103"
        latest_positions = "1"
        moved_at = "2023-08-09"
        stoped_at = "2023-08-09"
        engine_on_at = "2023-08-09"
        engine_off_at = "2023-08-09"
        engine_changed_at = "2023-08-09"
        database_id = "1"

    
        data = ( 
                 name, 
                 uniqueId,
                 latestPosition_id,
                 lastValidLatitude,
                 lastValidLongitude,
                 other,
                 speed, 
                 time, 
                 device_time, 
                 server_time,
                 ack_time,
                 altitude,
                 course, 
                 power,
                 address,
                 protocol,
                 latest_positions, 
                 moved_at,
                 stoped_at,
                 engine_on_at,
                 engine_off_at,
                 engine_changed_at,
                 database_id

                 )
                 
        return data 


    def vehiclesData(self,codigo_veiculo, id, placa, chassi, renavam, codigo_associado, codigo_tipo, codigo_categoria, tipo, categoria, marca, modelo, cpf_associado, rg_associado, nome_associado, codigo_situacao, codigo_voluntario, whatsapp, email):
       
        user_id = int(codigo_associado)
        current_driver_id = 2
        timezone_id = 179309
        traccar_device_id = int(id)
        icon_id = '34234'
        icon_colors = '{"moving":"green","stopped":"yellow","offline":"red","engine":"yellow"}'
        active = 0
        deleted = 0
        name =  str(nome_associado)
        imei =  int(codigo_associado)
        fuel_measurement_id = 1
        fuel_quantity = 0.00
        fuel_price = 0.00
        fuel_per_km = 0.0000
        sim_number = whatsapp
        msisdn = ''
        device_model = 'WJ14'
        plate_number = str(placa)
        vin = int(cpf_associado)
        registration_number = int(rg_associado)
        object_owner = str(nome_associado)
        tabela_fipe = 0
        additional_notes = str(marca)
        expiration_date = "0000-00-00"
        sim_expiration_date = "0000-00-00"
        sim_activation_date = "0000-00-00"
        installation_date = "0000-00-00"
        tail_color = '#33cc33'
        tail_length = 5
        engine_hours = 'gps'
        detect_engine = 'gps'
        min_moving_speed = 6
        min_fuel_fillings = 10
        min_fuel_thefts = 10
        snap_to_road  =  0
        gprs_templates_only = 0
        valid_by_avg_speed = 1
        parameters = '["status","ignition","charge","blocked","batterylevel","rssi","sequence","distance","totaldistance","motion","valid","enginehours","mcc","mnc","lac","cid","sat","alarm"]'
        currents = ''
        created_at = "2023-06-29"
        updated_at = "2023-06-29"
        forward = ''
        device_type_id = 0
        app_uuid = ''
        app_tracker_login = 0

        time.sleep(1)
    
        data = ( user_id, 
                current_driver_id , 
                timezone_id , 
                traccar_device_id , 
                icon_id , 
                icon_colors , 
                active , 
                deleted ,
                name ,  
                imei , 
                fuel_measurement_id , 
                fuel_quantity , 
                fuel_price , 
                fuel_per_km , 
                sim_number , 
                msisdn , 
                device_model , 
                plate_number , 
                vin ,  
                registration_number , 
                object_owner , 
                tabela_fipe , 
                additional_notes , 
                expiration_date , 
                sim_expiration_date , 
                sim_activation_date , 
                installation_date , 
                tail_color , 
                tail_length , 
                engine_hours , 
                detect_engine , 
                min_moving_speed , 
                min_fuel_fillings , 
                min_fuel_thefts , 
                snap_to_road  , 
                gprs_templates_only , 
                valid_by_avg_speed , 
                parameters , 
                currents , 
                created_at , 
                updated_at , 
                forward , 
                device_type_id , 
                app_uuid , 
                app_tracker_login
                )

        return data 
