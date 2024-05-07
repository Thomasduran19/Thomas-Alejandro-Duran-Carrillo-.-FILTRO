#elabora un programa en python que permita leer la informacion de un usuario y la almacene
#en un diccionario.
import os
import json
import leer_informacion as LI
MY_DATBASE='data/productos'
print('ACONTINUACION RESPONDE LO SIGUIENTE')
id=int(input('Ingrese su identificaión: '))
nombres=input('Ingrese sus nombres: ')
apellidos=input('¿Cuáles son sus apellidos?: ')
print('REGISTRE SU UBICACION')
direccion=input('¿Cuál es su dirección? : ')
ciudad=input('Ingrese la ciudad en la que se encuentra: ')
longitud=str(input('¿Qué longitud esta la ciudad aproximadamente? : '))
latitud=str(input('¿Cuál es la latitud de la ciudad aproximadamente?: '))
email=input('Ingrese su correo electronico: ')
edad=int(input('¿Cuántos años tienes?: '))
ocupacion=input('¿A qué se dedica?: ')
os.system('cls')
print(
 'NUMERO DE IDENTIFICACION: ',id  ,
 'NOMBRES: ',nombres  ,
 'APELLIDOS:',apellidos  ,
 'DIRECCION: ',direccion  ,
 'CIUDAD:',ciudad  ,
 'LONGITUD: ',longitud  ,
 'LATITUD: ',latitud  ,
 'CORREO ELECTRONICO: ',email  ,
 'EDAD: ',edad  ,
 'OCUPACION: ',ocupacion
)
print('Gracias por su cooperacion vuelva pronto.........')


