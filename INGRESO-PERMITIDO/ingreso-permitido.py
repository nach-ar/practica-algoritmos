# Paso 1: Pedir al usuario que ingrese la edad del cliente
edad = int(input("Ingrese la edad del cliente: "))

# Paso 2: Verificar si la edad cumple con el requisito para entrar
permitido = True if edad >= 18 else False

# Paso 3: Mostrar si el cliente puede o no ingresar
if permitido:
    print("El cliente puede entrar a la discoteca")
else:
    print("El cliente no puede entrar a la discoteca")
    