def generadorNombre():

    import random

    nombres = ["Ramiro","Fermin","Santiago","Nicolas","Guillermo","Mateo","Facundo","Joaquin","Salvador","Matias"]
    apellidos = ["Bravo","Martinez","Gonzales","chavarria","Salomon","Garcia","Villanueva","Mantilla","Prados","Santini","centarti"]
    listado_personas = []

    for _ in range(10):
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        edad = random.randint(18, 90)
        peso = random.randint(50, 130)
        persona = {'nombre': nombre, 'apellido': apellido, 'edad': edad, 'peso': peso}
        listado_personas.append(persona)

    listado_personas.sort(key=lambda x: x['apellido'])

    return listado_personas

listado = generadorNombre()

for persona in listado:
    print(persona)