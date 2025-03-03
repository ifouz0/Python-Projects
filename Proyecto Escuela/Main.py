from Clases import *
from Menu import Menu

class __init__():

    print ("-"*50)
    print ("Bienvenido a la gestión de proyectos TO-DO")
    print ("-"*50)
    usuario = input("Por favor, ingrese su nombre de usuario: ")
    menu = Menu(usuario)
    salir = False
    while salir == False:
        salir = menu.menu_principal()
#        print("Salir: ", salir)
    print ("*"*50)
    print ("Gracias por utilizar la gestión de proyectos TO-DO")
    

