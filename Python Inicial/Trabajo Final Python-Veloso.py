#Trabajo Final Python-Juan Ignacio Veloso

import mysql.connector
from mysql.connector import connection
import re

#Conecto con la base de datos
conexion = mysql.connector.connect(
 user='root', 
 password='',
 host='127.0.0.1',
 database='corralon')
 

print("")
print("Bienvenido a Corralón")
print("")

#Declaración variables globales

total=0
respuesta="si"
calculoSemanal={}
i=0

bolsasCal=0
precioBolsasCal=0
totalCal=0
totalCalDiario=0

bolsasCemento=0
precioBolsasCemento=0
totalCemento=0
totalCementoDiario=0

bolsasArena=0
precioBolsasArena=0
totalArena=0
totalArenaDiario=0

total=0

#Declaración funciones

def login():
    palabraClave=re.compile("micontraseña")
    ingreso=input("Ingrese contraseña para acceder al programa: ")
    if (palabraClave.match(ingreso)==None):
        login()

def altaCal():
    global precioBolsasCal
    global bolsasCal
    global totalCal
    global totalCalDiario
    precioBolsasCal=int(input("Ingrese el precio de las bolsas de Cal: "))
    bolsasCal=int(input("Ingrese cantidad de bolsas: "))
    subtotal=bolsasCal*precioBolsasCal
    totalCalDiario=totalCalDiario+subtotal
    totalCal=totalCal+subtotal

def altaCemento():
    global precioBolsasCemento
    global bolsasCemento
    global totalCemento
    global totalCementoDiario
    precioBolsasCemento=int(input("Ingrese el precio de las bolsas de Cemento: "))
    bolsasCemento=int(input("Ingrese cantidad de bolsas: "))
    subtotal=bolsasCemento*precioBolsasCemento
    totalCementoDiario=totalCementoDiario+subtotal
    totalCemento=totalCemento+subtotal

def altaArena():
    global precioBolsasArena
    global bolsasArena
    global totalArena
    global totalArenaDiario
    precioBolsasArena=int(input("Ingrese el precio de las bolsas de Arena: "))
    bolsasArena=int(input("Ingrese cantidad de bolsas: "))
    subtotal=bolsasArena*precioBolsasArena
    totalArenaDiario= totalArenaDiario+subtotal
    totalArena=totalArena+subtotal

def baja():
    semana=int(input("Ingrese semana a dar de baja: "))
    cursor=conexion.cursor()
    sentencia="delete from agendaganancias where semana=('{}')".format (semana)
    cursor.execute(sentencia)
    conexion.commit()

def modificacion():
    global total
    semana=int(input("Ingrese semana a modificar: "))
    alta()
    cursor=conexion.cursor()
    sentencia="update agendaganancias set gananciaSemanal=('{}') where semana=('{}')".format (total,semana)
    cursor.execute(sentencia)
    conexion.commit() 

def bajaTodo():
    cursor=conexion.cursor()
    sentencia="truncate table agendaganancias"
    cursor.execute(sentencia)
    conexion.commit() 

def altaBase():
    global total
    cursor=conexion.cursor()
    sentencia="insert into agendaganancias (gananciaSemanal) values ('{}')".format (total)
    cursor.execute(sentencia)
    conexion.commit()

def consulta():
    cursor=conexion.cursor()
    sentencia="select * from agendaganancias"
    cursor.execute(sentencia)
    respuesta=cursor.fetchall()
    print(respuesta)
   

def alta():
    global respuesta
    global totalDiario
    global calculoSemanal
    global totalArenaDiario
    global totalCementoDiario
    global totalCalDiario
    global i
    global total

    #Entrada de datos

    bandera=True
    while(bandera):
        jornadaLaboral=int(input("Ingrese cuántos dias tiene la jornada laboral semanal(1-7): "))
        print("")
        if (jornadaLaboral>=1 and jornadaLaboral<=7):
            break
        
    while(i<jornadaLaboral):

        print("Dia: "+ str(i+1))
        print("")

        while(respuesta=="si"):
        
            producto=input("Ingrese producto a dar de alta (Cal,Cemento,Arena): ")
            if (producto=="Cal"):
                altaCal()
            elif (producto=="Cemento"):
                altaCemento()
            elif(producto=="Arena"):
                altaArena()
            else:
                print("Producto inválido, intente nuevamente")
                continue
            respuesta=input("Desea seguir dando de alta productos? (si,no): ")
            print("")
        
        totalDiario=totalCalDiario+totalCementoDiario+totalArenaDiario
        calculoSemanal[i]={"Dia " + str(i+1):totalDiario}
        i=i+1
        respuesta="si"
        totalCalDiario=0
        totalCementoDiario=0
        totalArenaDiario=0

    #Salida de datos

    print("Resumen de la semana:")
    print("")
    print(calculoSemanal)
    total=totalArena+totalCal+totalCemento
    print("Total recaudado en la semana: "+ str(total))

def main():
    global i
    global total
    global totalArena
    global totalCal
    global totalCemento

    print("")
    choice=input("Ingrese operación a realizar (Alta,Baja,Modificacion,Consulta,Limpiar todo): ")
    if(choice=="Alta"):
        i=0
        total=0
        totalCemento=0
        totalCal=0
        totalArena=0
        alta()
        altaBase()
    elif(choice=="Baja"):
        baja()
    elif(choice=="Modificacion"):
        i=0
        total=0
        totalCemento=0
        totalCal=0
        totalArena=0
        modificacion()
    elif(choice=="Limpiar todo"):
        bajaTodo()
    elif (choice=="Consulta"):
        consulta()
    choice=input("Desea realizar mas operaciones? (si,no): ")
    if (choice=="si"):
        main()
    else:
        print("Hasta luego")

login()
main()
    
