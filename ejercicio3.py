def validar(nombreyapellido):
    numeros = ["1","2","3","4","5","6","7","8","9","0"]
    bandera = 0

    for letra in nombreyapellido:
        if letra in numeros:
            print("El nombre y apellido son incorrectos porque tiene números")
            bandera = 1
            break 

    if bandera == 0:
        print("El nombre y el apellido son correctos")

verificacion = input("Ingrese su nombre y apellido para saber si son correctos: ")
validar(verificacion)

