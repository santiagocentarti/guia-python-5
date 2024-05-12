def contar_palabras():
    palabras = 1  
    frase = input("Ingrese una frase, para decir la cantidad de palabras que posee: ")
    for i in frase:
        if i == " ":
            palabras += 1
    return palabras

cantidad = contar_palabras()

print("La cantidad de palabras de la frase es: ",cantidad)