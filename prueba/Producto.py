from dataclasses import dataclass
from datetime import datetime

@dataclass
class Producto:
    nombre:str
    valor:int
    descripcion:str
    stock:int

    def __init__(self, nombre:str, valor:int, descripcion:str, stock:int):
        if len(nombre) > 5:
            self.nombre = nombre
        if valor > 0:
            self.valor = valor
        if len(descripcion) <= 40:
            self.descripcion = descripcion
        if stock >= 0:
            self.stock = stock
    
    def __repr__(self):
        imprimir = "==============================================\n"
        imprimir = imprimir + f"Nombre Producto = {self.nombre}\n" 
        imprimir = imprimir + f"Valor = {self.valor}\n"
        imprimir = imprimir + f"Descripcion = {self.descripcion}\n"
        imprimir = imprimir + f"Cantidad = {self.stock}\n"
        return imprimir 



