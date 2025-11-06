# Paso 1: Definir el valor actual del euro y dolar contra el peso

tipo_cambio_eur_ars = 1666 #Realisticamente este valor deberia ser obtenido de una API externa
tipo_cambio_usd_ars = 1450


# Paso 2: Pedir al usuario a que quiere convertir sus pesos (Euro o Dolar)
tipo_conversion = input("Ingrese la moneda que origen para la conversion (EUR/USD): ").lower()

# Paso 3: Pedir monto a convertir
monto_a_convertir = float(input("Ingresar monto a convertir: "))

# Paso 4: Hacer la conversion utilizando los datos obtenidos
# Paso 5: Mostrar el resultado de la conversion
if tipo_conversion == "eur":
    resultado = monto_a_convertir * tipo_cambio_eur_ars
    print("El resultado de la conversion EUR a ARS es: ", resultado)
elif tipo_conversion == "usd":
    resultado = monto_a_convertir * tipo_cambio_usd_ars
    print("El resultado de la conversion USD a ARS es: ", resultado)
else:
    print("Error en la conversion")
