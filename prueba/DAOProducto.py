from Producto import Producto;
import mysql.connector
from dataclasses import dataclass

@dataclass
class DAOProducto:
    def insertarProducto(self, producto:Producto):
        conector = mysql.connector.connect(user="root", database="s3_base_bodega", host="localhost",password="")
        cursor = conector.cursor()
        sql = "insert into Productos values(%s,%s,%s,%s)"
        cursor.execute(sql,(producto.nombre, producto.descripcion, producto.valor, producto.stock))
        conector.commit()
        conector.close()
    
    def actualizarProducto(self, producto:Producto):
        conector = mysql.connector.connect(user="root", database="s3_base_bodega", host="localhost",password="")
        cursor = conector.cursor()
        sql = "update Productos set valor = %s, descripcion = %s, cantidad = %s where nombre_producto = %s"
        cursor.execute(sql,(producto.valor, producto.descripcion, producto.stock, producto.nombre))
        conector.commit()
        conector.close()

    def eliminarProducto(self, producto:Producto):
        conector = mysql.connector.connect(user="root", database="s3_base_bodega", host="localhost",password="")
        cursor = conector.cursor()
        sql = f"delete from Productos where nombre_producto = '{producto.nombre}'"
        cursor.execute(sql)
        conector.commit()
        conector.close()
    

    def buscarProducto(self, numero_producto:str):
        conector = mysql.connector.connect(user="root", database="s3_base_bodega", host="localhost",password="")
        cursor = conector.cursor()
        sql = f"select * from Productos where nombre_producto like '{numero_producto}'"
        cursor.execute(sql)
        fila = cursor.fetchone()
        print(fila[0], (fila[1]), fila[2], fila[3])
        prod = Producto(fila[0], fila[2], fila[1], fila[3])
        conector.close()
        return prod

    def listaProductos(self):
        conector = mysql.connector.connect(user="root", database="s3_base_bodega", host="localhost",password="")
        cursor = conector.cursor()
        sql = "select * from Productos"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        listaProd = list()
        conector.close()
        for fila in resultados:
            print(fila[0],fila[1],fila[2],fila[3])
            prod = Producto(fila[0],fila[2],fila[1],fila[3])
            listaProd.append(prod)
        return listaProd