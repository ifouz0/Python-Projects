from ProjectTODO import Tarea
from ProjectTODO import Proyecto
from ProjectTODO import GestionProyectos
from datetime import datetime
import json

def menu_ver_proyectos(gestion):
    print ("-"*50)
    print ("Proyectos existentes:")
    for i, proyecto in enumerate(gestion.proyectos):
        print(f"{i+1}. {proyecto.nombre} ({proyecto.estado})")
    print ("-"*50)
    print ("")
    print ("1. Ver tareas de un proyecto")
    print ("2. Volver al menú principal")
    opcion = input("Por favor, seleccione una opción: ")
    if opcion == "1":
        menu_ver_tareas_proyecto(gestion)
    else:
        return
    
def menu_crear_proyecto(gestion):
    print ("-"*50)
    nombre = input("Por favor, ingrese el nombre del proyecto: ")
    proyecto = Proyecto(nombre)
    gestion.agregar_proyecto(proyecto)
    print ("Proyecto creado con éxito!")
    print ("-"*50)
    print ("")
    opcion = input ("Quieres agregar una tarea a este proyecto? (S/N): ")
    menu_agregar_tarea_proyecto(gestion) if opcion == "S" else None
    return
    
def menu_modificar_proyecto(gestion):
    print ("-"*50)
    print ("Proyectos existentes:")
    for i, proyecto in enumerate(gestion.proyectos):
        print(f"{i+1}. {proyecto.nombre} ({proyecto.estado})")
    print ("-"*50)
    print ("")
    print ("1. Agregar tarea a un proyecto")
    print ("2. Eliminar tarea de un proyecto")
    print ("3. Volver al menú principal")
    opcion = input("Por favor, seleccione una opción: ")
    if opcion == "1":
        menu_agregar_tarea_proyecto(gestion)
    elif opcion == "2":
        menu_eliminar_tarea_proyecto(gestion)
    else:
        return
    
def menu_agregar_tarea_proyecto(gestion):
    print ("-"*50)
    print ("Proyectos existentes:")
    for i, proyecto in enumerate(gestion.proyectos):
        print(f"{i+1}. {proyecto.nombre} ({proyecto.estado})")
    print ("-"*50)
    print ("")
    proyecto = int(input("Por favor, seleccione el número de proyecto al que desea agregar una tarea: "))
    print ("-"*50)
    print ("")
    nombre = input("Por favor, ingrese el nombre de la tarea: ")
    fecha_inicio = input("Por favor, ingrese la fecha de inicio de la tarea (YYYY-MM-DD): ")
    fecha_fin = input("Por favor, ingrese la fecha de fin de la tarea (YYYY-MM-DD): ")
    tarea = Tarea(nombre, fecha_inicio, fecha_fin)
    gestion.proyectos[proyecto-1].agregar_tarea(tarea)
    print ("Tarea agregada con éxito!")
    print ("-"*50)
    print ("")
    return

def menu_eliminar_tarea_proyecto(gestion):
    print ("-"*50)
    print ("Proyectos existentes:")
    for i, proyecto in enumerate(gestion.proyectos):
        print(f"{i+1}. {proyecto.nombre} ({proyecto.estado})")
    print ("-"*50)
    print ("")
    proyecto = int(input("Por favor, seleccione el número de proyecto del que desea eliminar una tarea: "))
    print ("-"*50)
    print ("")
    print ("Tareas existentes:")
    for i, tarea in enumerate(gestion.proyectos[proyecto-1].tareas):
        print(f"{i+1}. {tarea.nombre} ({tarea.fecha_inicio.strftime('%Y-%m-%d')} - {tarea.fecha_fin.strftime('%Y-%m-%d')})")
    print ("-"*50)
    print ("")
    tarea = int(input("Por favor, seleccione el número de tarea que desea eliminar: "))
    gestion.proyectos[proyecto-1].eliminar_tarea(gestion.proyectos[proyecto-1].tareas[tarea-1])
    print ("Tarea eliminada con éxito!")
    print ("-"*50)
    print ("")
    return

def menu_ver_tareas_proyecto(gestion):
    print ("-"*50)
    print ("Proyectos existentes:")
    for i, proyecto in enumerate(gestion.proyectos):
        print(f"{i+1}. {proyecto.nombre} ({proyecto.estado})")
    print ("-"*50)
    print ("")
    proyecto = int(input("Por favor, seleccione el número de proyecto del que desea ver las tareas: "))
    print ("-"*50)
    print ("")
    print ("Tareas existentes:")
    for i, tarea in enumerate(gestion.proyectos[proyecto-1].tareas):
        print(f"{i+1}. {tarea.nombre} ({tarea.fecha_inicio.strftime('%Y-%m-%d')} - {tarea.fecha_fin.strftime('%Y-%m-%d')})")
    print ("-"*50)
    print ("")
    return



class __init__():
    print ("-"*50)
    print ("Bienvenido a la gestión de proyectos TO-DO")
    print ("-"*50)
    print ("")
    name = input("Por favor, ingrese su nombre de usuario: ")
    gest = GestionProyectos(name)
    gest.cargar_desde_json()
    print ("-"*50)
    print ("Hola, "+name+"!")
    while True:
        print("Bienvenido, este es el Menu Principal:")
        print("1. Ver proyectos existentes")
        print("2. Crear nuevo proyecto")
        print("3. Modificar proyecto")
        print("4. Salir")
        opcion = input("Por favor, seleccione una opción: ")
        if opcion == "1":
            menu_ver_proyectos(gest)
        elif opcion == "2":
            menu_crear_proyecto(gest)
        elif opcion == "3":
            menu_modificar_proyecto(gest)
        else:
            gest.guardar_en_json()
            print("Hasta luego!")
            exit()
