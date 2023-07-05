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