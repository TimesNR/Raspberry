# -*- coding: utf-8 -*-
"""
Created on Sat May  1 17:56:05 2021

@author: alanu
"""
#Es TOTALMENTE necesario instalar la base de datos, al menos en esta programación. También espero que funcione bien,
#teoricamente usa los componentes •	SCT-031 600A/100mA como sensor y el adaptador a raspberry RPICT7V1 v2.0

#CREATE TABLE `corriente` (
#`general` FLOAT NULL DEFAULT NULL,
#`estufas` FLOAT NULL DEFAULT NULL,
#`lavavajillas_lavadora` FLOAT NULL DEFAULT NULL,
#`alumbrado` FLOAT NULL DEFAULT NULL,
#`horno_vitro` FLOAT NULL DEFAULT NULL,
#`enchufes` FLOAT NULL DEFAULT NULL,
#`fecha` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
#)
#COLLATE='latin1_swedish_ci'
#ENGINE=InnoDB
#;
#Los comandos anteriores en lqa base de datos MySQL, que teoricamente te deja dos gratis

#pip install wheel y pip install MySQL en la terminal, en el segundo caos también puede ser pip install MySQL-python
#pip install urllib3 y 
#!/usr/bin/python
import serial
#import urllib
#import json
import MySQLdb
 
ser = serial.Serial('/dev/ttyAMA0', 38400)
response = ser.readline()
z = response.split(",")
if len(z)>=7:
    print ("Corriente" % z[1])
 
Corriente_Carro=z[1]

 
db = MySQLdb.connect("localhost","root","xxxxxx","NOMBRE_BASE_DATOS")
cursor = db.cursor()
 
cursor.execute("""INSERT INTO corriente (Corriente) VALUES (%s) """, (Corriente_Carro))
db.commit()
