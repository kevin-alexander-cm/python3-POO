from Funcionario import Funcionario;
import mysql.connector
from dataclasses import dataclass


@dataclass
class DAOFuncionario:
    def insertarFuncionario(self, funcionario:Funcionario):
        conector = mysql.connector.connect(user="root", database="s3_base_bodega", host="localhost",password="")
        cursor = conector.cursor()
        sql = "insert into funcionarios values(%s,%s,%s,%s,%s)"
        cursor.execute(sql,(funcionario.rut, funcionario.nombre, funcionario.direccion, funcionario.fecha_nacimiento, funcionario.fecha_ingreso))
        conector.commit()
        conector.close()
    
    def actualizarFuncionario(self, funcionario:Funcionario):
        conector = mysql.connector.connect(user="root", database="s3_base_bodega", host="localhost",password="")
        cursor = conector.cursor()
        sql = "update funcionarios set nombre = %s, direccion = %s, fecha_nacimiento = %s, fecha_ingreso = %s where rut = %s"
        cursor.execute(sql,(funcionario.nombre, funcionario.direccion, funcionario.fecha_nacimiento, funcionario.fecha_ingreso, funcionario.rut))
        conector.commit()
        conector.close()

    def eliminarFuncionario(self, funcionario:Funcionario):
        conector = mysql.connector.connect(user="root", database="s3_base_bodega", host="localhost",password="")
        cursor = conector.cursor()
        sql = f"delete from funcionarios where rut = '{funcionario.rut}'"
        cursor.execute(sql)
        conector.commit()
        conector.close()
    
    ### validar que el rut sea correcto (evitar una injección de sql)
    def buscarFuncionario(self, rut:str):
        conector = mysql.connector.connect(user="root", database="s3_base_bodega", host="localhost",password="")
        cursor = conector.cursor()
        sql = f"select * from funcionarios where rut like '{rut}'"
        cursor.execute(sql)
        fila = cursor.fetchone()
        fun = Funcionario(fila[1], fila[3], fila[2], fila[4], fila[0])
        conector.close()
        return fun

    def listaFuncionarios(self):
        conector = mysql.connector.connect(user="root", database="s3_base_bodega", host="localhost",password="")
        cursor = conector.cursor()
        sql = "select * from Funcionarios"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        listaFun = list()
        conector.close()
        for fila in resultados:
            print(fila[2], fila[3], fila[1], fila[4], fila[0])
            fun = Funcionario(fila[1], fila[3], fila[2], fila[4], fila[0])
            listaFun.append(fun)
        return listaFun