import funciones
import inventory

def AdminMode():
    opciones= ["Ver catálogo","Comprar juego", "Vender juego", "Generar reporte de desempeño", "Cerrar sesión"]
    while True:
        opcion = funciones.listOptions(opciones,"Selecciona una opción:\n")
        if opcion == "1":
            inventory.catalog()
        elif opcion == "2":
            inventory.buy()
        elif opcion == "3":
            inventory.sale()
        elif opcion == "4":
            inventory.guardar()
            inventory.reporte()
        elif opcion == "5":
            break

def ClientMode():
    opciones= ["Ver catálogo","Comprar juego", "Cerrar sesión"]
    while True:
        opcion = funciones.listOptions(opciones,"Selecciona una opción:\n")
        if opcion == "1":
            inventory.catalog()
        elif opcion == "2":
            inventory.sale()
        elif opcion == "3":
            break

inventory.cargar()

print("""
-------------------------------------
            ¡Bienvenido!
-------------------------------------
""")

typeUser=["Iniciar sesión como administrador","Iniciar sesión como cliente","Salir"]

while True:
    user = funciones.listOptions(typeUser,"Elige una opción:\n")
    if user == "1":
        AdminMode()
    elif user == "2":
        ClientMode()
    elif user == "3":
        inventory.guardar()
        print("¡Hasta luego!")
        exit(0)