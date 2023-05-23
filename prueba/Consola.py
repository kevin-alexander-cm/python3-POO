from Funcionario import Funcionario
from Producto import Producto
from DAOFuncionario import DAOFuncionario
from DAOProducto import DAOProducto
from datetime import datetime


fun1 = Funcionario("Jaime Domingo", datetime(2000,12,1), "Su casa 1", datetime(2000,12,1), "22455241-7")
fun2 = Funcionario("Jaime Domingo", datetime(2000,12,1), "Su casa 2", datetime(2000,12,1), "22455242-7")
fun3 = Funcionario("Jaime Domingo", datetime(2000,12,1), "Su casa 3", datetime(2000,12,1), "22455243-7")
fun4 = Funcionario("Jaime Domingo", datetime(2000,12,1), "Su casa 4", datetime(2000,12,1), "22455244-7")
fun5 = Funcionario("Jaime Domingo", datetime(2000,12,1), "Su casa 5", datetime(2000,12,1), "22455245-7")
daoFun = DAOFuncionario()

prod1 = Producto("Play 5", 700000, "Una consola", 3)
prod2 = Producto("Play 3", 700000, "Una consola", 3)
prod3 = Producto("Play 2", 700000, "Una consola", 3)
prod4 = Producto("Play 1", 700000, "Una consola", 3)
prod5 = Producto("Play 4", 700000, "Una consola", 3)

daoProd = DAOProducto()


listaFun = [fun1,fun2, fun3, fun4, fun5]
for funcionario in listaFun:
   daoFun.insertarFuncionario(funcionario)

listaProd = [prod1,prod2, prod3, prod4, prod5]
for producto in listaProd:
   daoProd.insertarProducto(producto)


fun5.direccion = "Vicuña Mackenna 5673"
fun5.nombre = "Juan Gonzales"

fun3.direccion = "Santa Rosa 401"
fun3.nombre = "Juan Perez"

daoFun.actualizarFuncionario(fun5)
daoFun.actualizarFuncionario(fun3)

prod1.valor = 1000000
daoProd.actualizarProducto(prod1)

fun6 = daoFun.buscarFuncionario("22455244-7")

print(fun6)

prod6 = daoProd.buscarProducto("Play 5")

print(prod6)


funElimiar = daoFun.eliminarFuncionario(fun2)
prodEliminar = daoProd.eliminarProducto(prod3)

listarFun = daoFun.listaFuncionarios()

for fun in listarFun:
    print(fun)

listarProd = daoProd.listaProductos()

for prod in listarProd:
    print(prod)



