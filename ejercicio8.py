def grilla():
    import random

    grilla = []
    for i in range(20):
        numero = random.randint(1, 100)
        grilla.append(numero)
    return grilla

grilla = grilla()
print("Grilla generada:", grilla)