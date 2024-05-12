def generadorContraseña():

    import random

    minusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    digitos = [0,1,2,3,4,5,6,7,8,9]

    elementoMinuscula = ""
    elementoMayuscula = ""
    elementoDigitos = ""

    contraseña = ""

    for i in range (3):
        contraseña = contraseña + random.choice(mayusculas)
    for i in range (3):
        contraseña = contraseña + random.choice(minusculas)
    for i in range (2):
        contraseña = contraseña + str(random.choice(digitos))

    return contraseña