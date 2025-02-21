import json
from datetime import datetime

class Tarea:
    def __init__(self, nombre, fecha_inicio, fecha_fin):
        self.nombre = nombre
        self.fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        self.fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'fecha_inicio': self.fecha_inicio.strftime('%Y-%m-%d'),
            'fecha_fin': self.fecha_fin.strftime('%Y-%m-%d')
        }

class Proyecto:
    def __init__(self, nombre, estado = "Nuevo"):
        self.nombre = nombre
        self.estado = estado
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        now = datetime.now()   
        if all(t.fecha_fin < now for t in self.tareas):
            self.estado = "Finalizado"
        elif any(t.fecha_inicio <= now <= t.fecha_fin for t in self.tareas):
            self.estado = "En progreso"
    
    def eliminar_tarea(self, tarea):
        self.tareas.remove(tarea)
        now = datetime.now()   
        if all(t.fecha_fin < now for t in self.tareas):
            self.estado = "Finalizado"
        elif any(t.fecha_inicio <= now <= t.fecha_fin for t in self.tareas):
            self.estado = "En progreso"

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'estado': self.estado,
            'tareas': [tarea.to_dict() for tarea in self.tareas]
        }

class GestionProyectos:
    def __init__(self, usuario):
        self.usuario = usuario
        self.proyectos = []
        self.archivo = 'TODO.json'

    def agregar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)

    def guardar_en_json(self):
        with open(self.archivo, 'w') as f:
            json.dump([proyecto.to_dict() for proyecto in self.proyectos], f, indent=4)

    def cargar_desde_json(self):
        with open(self.archivo, 'r') as f:
            proyectos_data = json.load(f)
            for proyecto_data in proyectos_data:
                proyecto = Proyecto(proyecto_data['nombre'], proyecto_data['estado'])
                try:
                    for tarea_data in proyecto_data['tareas']:
                        tarea = Tarea(tarea_data['nombre'], tarea_data['fecha_inicio'], tarea_data['fecha_fin'])
                        proyecto.agregar_tarea(tarea)
                    self.agregar_proyecto(proyecto)
                except(TypeError):
                    print("Error en la carga de datos")
                    continue