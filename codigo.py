# -*- coding: utf-8 -*-
import math

def cifrar():      
    
    mensajeACifrar = input('Ingresa tu mensaje a cifrar')
    
    llave = input('Ingresa un numero entero para la llave')
    lallave = int(llave)
    
    if len(mensajeACifrar)>lallave:
        
        mensajeCifrado = encriptando(lallave, mensajeACifrar)
        print("")
        print("")
        print(f'Su mensaje descifrado es:\n {mensajeCifrado}')
    
    else:
        
        print("")
        print("La llave es mayor que el numero de caracteres que tiene tu mensaje que quieres cifrar")
        print("porfavor introduce una llave que sea menor a el numero de caracteres que tiene el mensaje que quieres cifrar")
        print("")
        print("")
        
        cifrar()
    print("")
    print("")
    print("Si deseas volver al menu principal escribe si")
    volver=input("Si deseas repetir la programa escribe cualquier otra cosa")
    vol=volver.upper()
    print("")
    print("")
    
    if vol=="SI":
        menu()
    else:
        cifrar()
        

def encriptando(llave, mensaje):
    
    mensajeCifrado = [''] * llave
    
    for columnas in range(llave):
        puntero = columnas
        
        while puntero < len(mensaje):
            
            mensajeCifrado[columnas] += mensaje[puntero]
            
            puntero += llave
            
    return ''.join(mensajeCifrado)

if __name__ == '__cifrar__':
    cifrar()


def descifrar():
    mensajaDescifrar = input('Ingresa tu mensaje a descifrar')
    llave = input('Ingresa el numero de la llave')

    laLlave = int(llave)
    
    if len(mensajaDescifrar)>laLlave:
        
        texto = desencriptar(laLlave, mensajaDescifrar)  
        print("")
        print("") 
        print(f'Su mensaje descifrado es:\n {texto}')
    
    else:
        
        print("")
        print("")
        print("La llave que escribiste es mayor a el numero de caracteres que tiene tu mensaje que quieres descifrar")
        print("Si deseas continuar con esa llave tu mensaje no sera desencriptado")
        respuesta=input('Escribe "si" si quieres continuar o "no" si quieres volver al menu principal')
        res=respuesta.upper()

        if res=="SI":
                
            print("")
            print("")
            texto = desencriptar(laLlave, mensajaDescifrar)    
            print(f'Su mensaje descifrado es:\n {texto}')
                
        else:
            print("")
            print("")
            menu()    
            
    print("")
    print("")
    print("Si deseas volver al menu principal escribe si")
    volver=input("Si deseas repetir la programa escribe cualquier otra cosa")
    vol=volver.upper()
    print("")
    print("")
    
    if vol=="SI":
        menu()
    else:
        descifrar()                
                

def desencriptar(llave, mensaje):
    
    numColumnas = math.ceil(len(mensaje) / llave)
    
    numFilas = llave
    
    cajas = (numColumnas * numFilas) - len(mensaje)
    
    caracteres = [''] * numColumnas
    
    columnas = 0
    filas = 0

    for symbol in mensaje:
        caracteres[columnas] += symbol
        columnas += 1
        
        if (columnas == numColumnas) or (columnas == numColumnas - 1 and filas >= numFilas - cajas):
            columnas = 0
            filas += 1

    return ''.join(caracteres)

if __name__ == '__descifrar__':
    descifrar()
    

def menu():
    try:
        print("Hola que tal aqui podras cifrar o descifrar un codigo con el metodo de transpocision")
        print("Escribe 1 si quieres cifrar o 2 si quieres descifrar\n1. Cifrar\n2. Descifrar")
        opc=int(input())
        
        if opc==1:
            cifrar()        
        elif opc ==2:
            descifrar()
            
    except:
        
        print("")        
        print("")
        #print("Vaya parece que a sucedido un error por favor lee las indicaciones")                
        print("Porfavor escribe un valor valido")        
        print("")
        print("")
        menu()
        
        
menu()
   

    