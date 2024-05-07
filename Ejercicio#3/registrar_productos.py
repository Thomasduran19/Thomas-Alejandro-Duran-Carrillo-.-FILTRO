#Elabore un programa en Python que permita registrar los productos de una
#Tienda de viveres. La información se debe almacenar en un archivo JSON

import json

MY_DATABASE="data/producto"
print('**REALICE LO SIGUIENTE POR FAVOR***')
ID= int(input('Ingrese su numero de identificación: '))
NOMBRE=input('¿Cómo te llamas?: ')
print('Hola',NOMBRE,'acontinuacion te mostrare el menu de los siguientes articulos')
title="REGISTRAR PRODUCTO"
MENU= ' 1.ARROZ... 2.PASTA.... 3.AZUCAR....4.salir'
salida='gracias por cooperar'
opcion=int(input('ingrese cualquier numero para acceder... '))
while (opcion):
    print(title)
    print(MENU)
    opcion=int(input('ingrese opcion:'))
    if opcion==1:
        print('Haz elegido ARROZ')
        cantidad=int(input('ingrese cantidad de producto: '))
        precio=2000
        stockmax=20000
        precioTotal=cantidad*precio
        if precioTotal<20000:
            print('el precio a pagar es:',precioTotal)
            print('gracias por tu compra')
        else:
            print('lo siento no se pude exceder en su compra ya que el stockmax es de:',stockmax)
            
            print(MENU(0))

    elif opcion==2:
        print('Haz elegido PASTA')
        cantidad1=int(input('Ingrese cantidad qu deseas llevar:'))
        precio1=2500
        stockmax1=20000
        precioTotal1=cantidad1*precio1
        if precioTotal1<20000:
            print('el precio a pagar es:',precioTotal1)
            print('gracias por tu compra')
        else:
            print('lo siento no se pude exceder en su compra ya que el stockmax es de:',stockmax1)
            print(MENU)
        
    elif opcion==3:
        print('Haz elegido AZUCAR')
        cantidad2=int(input('Ingresa la cantidad que deseas llevar: '))
        precio2=3000
        stockmax2=20000
        precioTotal2=cantidad2*precio2
        if precioTotal2<20000:
            print('el precio a pagar es:',precioTotal2)
            print('gracias por tu compra')
        else:
            print('lo siento no se pude exceder en su compra ya que el stockmax es de:',stockmax2)
            print(MENU)
    else:
       print(salida)
print('OPCION INVALIDA')
MENU(0)
print('gracias por su compra..........')




















