def calculadora():
    if dato == "suma":
            return num1 + num2
    if dato == "resta":
            return num1 - num2
    if dato == "multiplicacion":
            return num1 * num2
    if dato == "division":
            return num1 / num2
    
num1 = float(input("Ingrese un num: "))
num2 = float(input("Ingrese otro num: "))
dato = (input("Ingrese la operacion que quiera realizar (suma,resta,multiplicacion,division): "))

print("El resultado es: ",calculadora())
