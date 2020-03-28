##Cortes Rodriguez Francisco Gerardo
import datetime
from time import ctime
import ntplib
import os

x = datetime.datetime.now()
print ("Hora de inicio de peticion = %s" % x)

servidor_de_tiempo = "time-e-g.nist.gov"
cliente_ntp = ntplib.NTPClient()
respuesta = cliente_ntp.request(servidor_de_tiempo)
hora_actual = datetime.datetime.strptime(ctime(respuesta.tx_time), "%a %b %d %H:%M:%S %Y")
hora_llegada = datetime.datetime.now()
print("Hora de llegada de la peticion = %s" % hora_llegada) 
print("Fecha/Hora que se recibio del servidor " + servidor_de_tiempo +  ": " + str(hora_actual) + "\n")
print("Ajuste(retraso): "+str(((hora_llegada-x)/2)))
hora_ajustada = hora_actual + ((hora_llegada-x)/2)
print("Hora a cambiar: "+str(hora_ajustada))
f = 'date -u "'+str(hora_ajustada.strftime("%m%d%H%M%Y.%S"))+'"'
os.system(f)

