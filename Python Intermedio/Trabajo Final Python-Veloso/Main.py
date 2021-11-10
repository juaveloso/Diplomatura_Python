#documentar el programa con pydoc
#utilizar el patron mvc
#utilizar el paradigma orientado a objetos
#el codigo debe cumplir con pep8 

#Módulos
from MySQL import conecto
from MySQL import consulta_ingreso
from MySQL import consulto_saldo
from MySQL import agrego_saldo
from MySQL import retiro_saldo
from MySQL import borrando_saldo
from MySQL import consulta_disponibilidad
from MySQL import nuevo_usuario
from MySQL import borro_usuario
from Regex import validacion
from hashlib import md5


#Declaración de funciones
def registrarse():
    usuario=""
    while (True):
        usuario=validacion("Ingrese nombre de usuario: ")  
        if(consulta_disponibilidad(usuario)):
            break
    contrasena=validacion("Ingrese una contraseña: ")
    nuevo_usuario(usuario,contrasena)
    setup()

def ingresar():
    bandera=True
    while (True):
        usuario=input("Ingrese nombre de usuario: ")
        contrasenia=input("Ingrese contraseña: ")
        contrasenia=md5(contrasenia.encode("utf-8")).hexdigest()
        if (consulta_ingreso(usuario,contrasenia)):
            break
        else:
            continue

    while (True):
        print("")
        if (bandera):
            print("Consultar billetera:'c' " + '\n' + "Agregar billetera:'a' " + '\n'
                + "Vaciar billetera: 'v' " + '\n' + "Retirar billetera:'r' " + '\n'
                + "Cambiar contraseña: 'cambio contraseña' " + '\n'+ "Borrar cuenta: 'borrar cuenta' " + '\n'
                + "Salir: 's' " + '\n')
            print("")
            bandera=False

        respuesta=input("Ingrese operación a realizar: ")

        if (respuesta== "c"):
            saldo=consulto_saldo(usuario)
            print("Usted tiene " + saldo + " pesos en su billetera")
            
        elif (respuesta=="a"):
            saldo=int(input("Ingrese dinero a agregar: "))
            agrego_saldo(usuario,saldo)
            print("")
            saldo=consulto_saldo(usuario)
            print("Usted tiene " + saldo + " pesos en su billetera")

        elif (respuesta=="r"):
            saldo=int(input("Ingrese dinero a retirar: "))
            retiro_saldo(usuario,saldo)
            print("")
            saldo=consulto_saldo(usuario)
            print("Usted tiene " + saldo + " pesos en su billetera")
            
        elif (respuesta=="v"):
            borrando_saldo(usuario)
            print("")
            saldo=consulto_saldo(usuario)
            print("Usted tiene " + saldo + " pesos en su billetera")
            
        elif (respuesta=="cambio contraseña"):
            print("Cambiando")
            
        elif (respuesta=="borrar cuenta"):
            borro_usuario(usuario)
            print("Usuario eliminado exitosamente")
            setup()
            
        elif (respuesta=="s"):
            setup()
            
        else:
            print("Esta operación no existe")
      
def setup():
    while (True):
        print("")
        print("Menú principal")
        print("")
        respuesta=input("Para ingresar ingrese:'ingresar' " + '\n' + "Para registrarse ingrese:'registrarse' " + '\n'
            + "Para salir del programa ingrese:'s' " + '\n')
        if (respuesta== "ingresar"):
            ingresar()
            break
        elif (respuesta=="registrarse"):
            registrarse()
            break
        elif (respuesta=="s"):
            print("Hasta luego!")
            exit()
        else:
            print("Esta operación no existe")
      
      
#Bloque principal
#Conecto con base de datos
try:
    conecto()

except:
    print ("Error al intentar conectar con la base de datos, intente más tarde")
    exit()
    
#despliego menú de opciones
setup()
