from datetime import datetime

class Proyecto:
    nombre :str
    fecha_inicio: datetime
    fecha_fin: datetime    
    estado: str
    tareas: list = []
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.fecha_inicio = datetime.today()
        self.fecha_fin = datetime.today()
        self.estado = "Planificado"
        

    def agregar_tarea(self, nom_tarea: str, fecha_inicio: datetime, fecha_fin: datetime) -> None:
        self.tareas.append(Tarea(descr_tarea=nom_tarea,fecha_inicio=fecha_inicio,fecha_fin=fecha_fin))
        for tarea in self.tareas:
            if tarea.fecha_inicio < self.fecha_inicio:
                self.fecha_inicio = tarea.fecha_inicio
            if tarea.fecha_fin > self.fecha_fin:
                self.fecha_fin = tarea.fecha_fin
        if self.fecha_inicio < datetime.today():
            self.estado = "En curso"
        if self.fecha_fin < datetime.today():
            self.estado = "Finalizado"

    def eliminar_tarea(self, nombre_proyecto, tarea) -> None:
        for tarea in self.tareas:
            if tarea.descr_tarea == tarea:
                self.tareas.remove(tarea)
        for tarea in self.tareas:
            if tarea.fecha_inicio < self.fecha_inicio:
                self.fecha_inicio = tarea.fecha_inicio
            if tarea.fecha_fin > self.fecha_fin:
                self.fecha_fin = tarea.fecha_fin
        if self.fecha_inicio < datetime.today():
            self.estado = "En curso"
        if self.fecha_fin < datetime.today():
            self.estado = "Finalizado"

    def modificar_proyecto(self, nombre_proyecto: str) -> None:
        self.nombre = nombre_proyecto

    def listar_proyectos(self) -> list:
        pass

    def listar_tareas(self, nombre_proyecto: str) -> list:
        pass


class Tarea:

    def __init__(self, descr_tarea: str, fecha_inicio: datetime, fecha_fin: datetime):
        self.descr_tarea = descr_tarea
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def to_dict(self):
        return {
            "descripcion": self.descripcion,
            "estado": self.estado,
            "fecha_inicio": self.fecha_inicio.isoformat(),
            "fecha_fin": self.fecha_fin.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            descripcion=data["descripcion"],
            estado=data["estado"],
            fecha_inicio=datetime.fromisoformat(data["fecha_inicio"]),
            fecha_fin=datetime.fromisoformat(data["fecha_fin"])
        )