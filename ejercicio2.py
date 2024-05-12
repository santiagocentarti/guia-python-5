def saludo(hora):
    if hora >= 6 and hora <= 12:
        print("Buenos días!")
    elif hora <= 12 and hora <= 18:
        print("Buenas tardes!")
    else:
        print("Buenas noches!")

ingresoHora = int(input("Ingrese la hora del dia para ser saludado: "))

saludo(ingresoHora)