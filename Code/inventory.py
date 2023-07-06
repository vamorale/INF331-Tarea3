import funciones
from datetime import datetime
import os

games = dict()
sales = []
purchases = []

platforms = ["PC", "Switch", "Xbox Series", "PS5"]
genres = ["Acción","Aventura","Arcade","Deportes","Estrategia","Simulación","Juegos de mesa","Juegos musicales"]

#Mostrar el catálogo en consola

def catalog():
    if len(games.keys())!=0:
        for game in games.values():
            print("Título: "+game[0]+
                ". Precio compra: "+game[1]+
                ". Precio venta: "+game[2]+
                ". Género: "+game[3]+
                ". Plataforma: "+game[4]+
                ". Cantidad disponible: "+game[-1]+
                ".")
    else:
        print("No hay juegos en catálogo.")

#Listar los juegos al momento de comprar por parte del cliente

def show():
    juegos = games.values()
    lista = []
    for i in juegos:
        lista.append(i[0]+", Precio: "+i[3]+", Cantidad disponible: "+i[-1])
    print(lista,games)
    return lista

# Compra que realiza el administrador

def buy():
    id = len(games.keys()) if len(games.keys())!=0 else 0
    title = input("Ingresa el título del juego: ")
    Bprice = input("Ingresa el precio de compra: ")
    Sprice = input("Ingresa el precio de venta: ")
    Genre = funciones.listOptions(genres,"Escoge el género del juego:\n")
    Platform = funciones.listOptions(platforms,"Escoge la plataforma del juego:\n")
    cant = input("Ingresa la cantidad a comprar: ")
    print(genres[int(Genre)-1],platforms[int(Platform)-1])
    games[id] = [title,Bprice,Sprice,genres[int(Genre)-1],platforms[int(Platform)-1],cant]
    purchases.append([id,title,Bprice,cant])
    print("Juego registrado en el inventario exitosamente")

# Ventas del admin y compras del cliente

def sale():
    game = 0

    while True:
        game = funciones.listOptions(list(show()),"Selecciona un juego:\n")
        if int(games[int(game)-1][-1]) == 0:
            print("Este juego está agotado")
        else:
            break

    while True:
        cant = 0
        cant = int(input("Ingresa la cantidad: "))
        if cant>int(games[int(game)-1][-1]) or cant<=0:
            print("Esa cantidad no es válida")
            print(cant)
        else:
            games[int(game)-1][-1] = str(int(games[int(game)-1][-1]) - cant)
            print("Juego comprado exitosamente.")
            break
    sales.append([int(game)-1,games[int(game)-1][0],games[int(game)-1][2],cant])

# Guardar los datos en los archivos

def guardar():
    f = open("inventario.txt","w")
    for i,valor in games.items():
        f.write(str(i)+","+",".join(valor)+"\n")
    f.close()
    f = open("ventas.txt","w")
    for valor in sales:
        f.write(",".join([str(i) for i in valor])+"\n")
    f.close()
    f = open("compras.txt","w")
    for valor in purchases:
        f.write(",".join([str(i) for i in valor])+"\n")
    f.close()

# Carga los datos de los archivos en las estructuras de datos

def cargar():
    if os.stat("inventario.txt").st_size != 0:
        f=open("inventario.txt","r")
        for linea in f:    
            games[int(linea[0])] = linea[2:].strip().split(",")
        f.close()
    if os.stat("ventas.txt").st_size != 0:
        f=open("ventas.txt","r")
        for linea in f:
            sales.append(linea.strip().split(","))
        f.close()
    if os.stat("compras.txt").st_size != 0:
        f=open("compras.txt","r")
        for linea in f:
            purchases.append(linea.strip().split(","))
        f.close()

# Genera reporte de desempeño

def reporte():
    n_compras=0
    n_juegos_c=0
    total_compras=0
    n_ventas=0
    n_juegos_v=0
    total_ventas=0
    f=open("reporte_"+str(datetime.now().strftime('%Y-%m-%d_%H.%M.%S'))+".txt","w")
    v=open("ventas.txt","r")
    c=open("compras.txt","r")
    f.write("Reporte de ventas\n---------------------\nCompras:\n")
    for i in c:
        linea=i.strip().split(",")
        total_compras+=int(linea[2])*int(linea[3])
        n_compras+=1
        n_juegos_c+=int(linea[3])
        f.write("- Juego: "+linea[1]+", precio: "+linea[2]+", cantidad: "+linea[3]+"\n")
    f.write("---------------------\nVentas:\n")
    for i in v:
        linea=i.strip().split(",")
        total_ventas+=int(linea[2])*int(linea[3])
        n_ventas+=1
        n_juegos_v+=int(linea[3])
        f.write("- Juego: "+linea[1]+", precio: "+linea[2]+", cantidad: "+linea[3]+"\n")
    f.write("---------------------\nResultados:\n")
    f.write("Cantidad total de compras: "+str(n_compras)+". Cantidad total de ventas: "+str(n_ventas)+".\n")
    f.write("Cantidad total de juegos comprados: "+str(n_juegos_c)+". Cantidad total de juegos vendidos: "+str(n_juegos_v)+".\n")
    f.write("Egresos: "+str(total_compras)+". Ingresos: "+str(total_ventas)+". Ganancia total: "+ str(total_ventas-total_compras)+".")
    c.close()
    v.close()
    f.close()
    print("Reporte generado exitosamente.")