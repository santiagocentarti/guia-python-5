def mayor(edad):
    if edad >= 18:
        print("Usted es mayor de edad")
    else:
        print("Usted es menor de edad")

edad = int(input("Ingrese su edad para validar si es mayor de edad o no: "))

mayor(edad)