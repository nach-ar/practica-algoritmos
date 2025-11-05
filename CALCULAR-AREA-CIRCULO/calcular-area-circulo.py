import math

# Paso 1: Pedir al usuario que ingrese el radio del circulo
radio = float(input("Ingrese el radio del círculo: "))

# Paso 2: Calcular el area del circulo utilizando la formula area = pi * radio^2
area = math.pi * radio ** 2

# Paso 3: Mostrar al usuario el area calculada
print("El area del circulo es con radio", radio, "es:", area)