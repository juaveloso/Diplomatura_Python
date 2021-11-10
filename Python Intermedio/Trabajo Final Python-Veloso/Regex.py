import re

def validacion(mensaje):
    palabra_clave=re.compile("[\w]")
    bandera=True
    while(bandera):
        bandera=False
        campo=input(mensaje)
        for i in campo:
            if (palabra_clave.match(i)==None):
                print("Solo se permiten caracteres alfanuméricos")
                bandera=True
                break  
    return campo 