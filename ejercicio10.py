def calcular_iva(valor_total_pagado, tasa_iva):
    iva = valor_total_pagado / (1 + tasa_iva) * tasa_iva
    valor_sin_iva = valor_total_pagado - iva
    return iva, valor_sin_iva

valor_total_pagado = float(input("Ingrese el valor total pagado incluyendo el IVA: "))
tasa_iva = 0.21

iva, valor_sin_iva = calcular_iva(valor_total_pagado, tasa_iva)
print("Valor total pagado:", valor_total_pagado)
print("Valor del IVA:", iva)
print("Valor sin IVA:", valor_sin_iva)