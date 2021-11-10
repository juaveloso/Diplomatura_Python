import mysql.connector
from mysql.connector import connection
import hashlib
from hashlib import md5

conexion=""

def conecto():
    global conexion
    conexion = mysql.connector.connect(
    user='root', 
    password='',
    host='127.0.0.1',
    database='billetera')

def consulta_ingreso(usuario,contrasenia):
    cadena=""
    
    cursor=conexion.cursor()
    sentencia="select contraseña from usuarios where usuario= ('{}')".format (usuario)
    cursor.execute(sentencia)
    respuesta=cursor.fetchall()
    
    for elemento in respuesta:
        i=0
        cadena=str(elemento[i])
        i=i+1
    
    if (cadena==contrasenia):
        return True
    else:
        print("Usuario o contraseña incorrectos, intente nuevamente")
        print("")
        return False
    
def consulta_disponibilidad(usuario):
    cursor=conexion.cursor()
    sentencia="select usuario from usuarios where usuario= ('{}')".format (usuario)
    cursor.execute(sentencia)
    respuesta=cursor.fetchall()
    cadena=""
    for elemento in respuesta:
        i=0
        cadena=str(elemento[i])
        i=i+1
    if (cadena==usuario):
        print("Usuario no disponible")
        return False
    else:
        print("Usuario disponible")
        print("")
        return True

def nuevo_usuario(usuario,contrasenia):
    contrasenia=(md5(contrasenia.encode("utf-8")).hexdigest())
    cursor=conexion.cursor()
    sentencia="insert into usuarios (usuario,contraseña) values( ('{}') , ('{}') )".format (usuario,contrasenia)
    cursor.execute(sentencia)
    conexion.commit() 
    print("Usuario creado exitosamente")

def agrego_saldo(usuario,saldo):
    cursor=conexion.cursor()
    sentencia="select dinero from usuarios where usuario= ('{}')".format (usuario)
    cursor.execute(sentencia)
    respuesta=cursor.fetchall()
    cadena=""
    for elemento in respuesta:
        i=0
        cadena=int(elemento[i])
        i=i+1
    nuevo_saldo=cadena+saldo
    cursor=conexion.cursor()
    sentencia="update usuarios set dinero=('{}') where usuario=('{}')".format (nuevo_saldo,usuario)
    cursor.execute(sentencia)
    conexion.commit() 

def retiro_saldo(usuario,saldo):
    cursor=conexion.cursor()
    sentencia="select dinero from usuarios where usuario= ('{}')".format (usuario)
    cursor.execute(sentencia)
    respuesta=cursor.fetchall()
    cadena=0
    for elemento in respuesta:
        i=0
        cadena=int(elemento[i])
        i=i+1
    nuevo_saldo=cadena-saldo
    cursor=conexion.cursor()
    sentencia="update usuarios set dinero=('{}') where usuario=('{}')".format (nuevo_saldo,usuario)
    cursor.execute(sentencia)
    conexion.commit() 

def consulto_saldo(usuario):
    cursor=conexion.cursor()
    sentencia="select dinero from usuarios where usuario= ('{}')".format (usuario)
    cursor.execute(sentencia)
    respuesta=cursor.fetchall()
    cadena=""
    for elemento in respuesta:
        i=0
        cadena=str(elemento[i])
        i=i+1
    return cadena

def borrando_saldo(usuario):
    cursor=conexion.cursor()
    sentencia="update usuarios set dinero=0 where usuario=('{}')".format (usuario)
    cursor.execute(sentencia)
    conexion.commit() 

def cambiar_contraseña(usuario):
    print("Cambiando contraseña")

def borro_usuario(usuario):
    cursor=conexion.cursor()
    sentencia="delete from usuarios where usuario=('{}')".format (usuario)
    cursor.execute(sentencia)
    conexion.commit() 
    print("Usuario eliminado exitosamente")