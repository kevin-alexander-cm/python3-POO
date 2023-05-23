from dataclasses import dataclass
from datetime import datetime

@dataclass
class Funcionario:
    nombre:str
    fecha_nacimiento:datetime
    direccion:str
    fecha_ingreso:datetime
    rut:str

    def __init__(self, nombre:str, fecha_nacimiento:datetime, direccion:str, fecha_ingreso:datetime, rut:str):
        if 10 <= len(rut) <= 12: 
            self.rut = rut
        if 6 < len(nombre) < 20:
            self.nombre = nombre
        if datetime(1930, 1, 1) < fecha_nacimiento < datetime(2005, 1, 1):
            self.fecha_nacimiento = fecha_nacimiento
        if 6 < len(direccion) < 50:
            self.direccion = direccion
        if fecha_ingreso < datetime.now():
            self.fecha_ingreso = fecha_ingreso
    
    def __repr__(self):
        imprimir = "==============================================\n"
        imprimir = imprimir + f"Rut = {self.rut}\n" 
        imprimir = imprimir + f"Nombre = {self.nombre}\n"
        imprimir = imprimir + f"Dirección = {self.direccion}\n"
        imprimir = imprimir + f"Fecha Nacimiento = {self.fecha_nacimiento}\n"
        imprimir = imprimir + f"Pais de ingreso = {self.fecha_ingreso}\n"
        return imprimir 