import funciones

def AdminMode():
    opciones= ["Comprar juego", "Vender juego", "Generar reporte de desempeño", "Cerrar sesión"]
    opcion = funciones.listOptions(opciones,"Selecciona una opción:\n")
    if opcion == "1":
        print("compra")
    elif opcion == "2":
        print("venta")
    elif opcion == "3":
        print("reporte")
    elif opcion == "4":
        print(funciones.lista)
        exit(0)

def ClientMode():
    opciones= ["Comprar juego", "Cerrar sesión"]
    opcion = funciones.listOptions(opciones,"Selecciona una opción:\n")
    if opcion == "1":
        print("compra")
    elif opcion == "2":
        exit(0)

print("""
-------------------------------------
            ¡Bienvenido!
-------------------------------------
""")

typeUser=["Administrador","Cliente"]

while True:
    user = funciones.listOptions(typeUser,"Iniciar sesión como:\n")
    if user == "1":
        AdminMode()
    elif user == "2":
        ClientMode()