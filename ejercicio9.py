def distancia_entre_puntos():
    distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distancia

x1 = float(input("Ingrese la coordenada x de la primera persona: "))
y1 = float(input("Ingrese la coordenada y de la primera persona: "))
x2 = float(input("Ingrese la coordenada x de la segunda persona: "))
y2 = float(input("Ingrese la coordenada y de la tercera persona: "))

distancia = distancia_entre_puntos()
print("La distancia entre las dos personas es:", distancia)