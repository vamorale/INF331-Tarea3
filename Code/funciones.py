def listOptions(options,init_message):

    message = init_message

    for index, item in enumerate(options):
        message += f'{index+1}) {item}\n'

    print(message + "Escribe tu opción: ")

    while True:
        user_input = input()
        if user_input not in map(str, range(1, len(options) + 1)):
            print("Selecciona una opción válida: ")
        else:
            print('Has seleccionado: ' + options[int(user_input) - 1])
            return user_input
        
def validarJuego(datos):
    #titulo,precioC,precioV,Genero,Plataforma,cant
    if datos[0]=="" or datos[0]==" ":
        return False
    if datos[1]=="" or not(isinstance(datos[1],int)) or datos[1]=="0":
        return False
    if datos[2]=="" or not(isinstance(datos[2],int)) or datos[2]=="0":
        return False
    if datos[3]=="" or datos[3]==" ":
        return False
    if datos[4]=="" or datos[4]==" ":
        return False
    if datos[5]=="" or not(isinstance(datos[5],int)) or datos[5]=="0":
        return False
    return True

def validarCompra(datos):
    #titulo,cant
    if datos[0]=="" or datos[0]==" ":
        return False
    if datos[2]=="" or not(datos[2].isdigit()) or int(datos[2])<=0:
        return False
    return True