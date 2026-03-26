# Trabajo Practico Estructuras Repetitivas
# Alvaro Salla

# # # EJERCICIO 1 # # #
# # # CAJA DE KIOSCO # # #
# # # Objetivo: Simular una compra con validaciones y cálculo de total # # #

nombre_cliente = input("Ingrese su nombre: ")
nombre_cliente = nombre_cliente.title()
resumen = ""
precio_total = 0
precio_total_descuento = 0
ahorro = 0

while not nombre_cliente.replace(" ","").isalpha():
    nombre_cliente = input("Porfavor, ingrese un nombre valido: ")
    nombre_cliente = nombre_cliente.title()

cantidad_productos = input("Ingrese la cantidad de productos a comprar: ")

while not cantidad_productos.isdigit():
    cantidad_productos = input("Por favor, ingrese un numero entero positivo: ")

cantidad_productos = int(cantidad_productos)

while cantidad_productos <= 0:
    cantidad_productos = input("No se puede ingresar un numero negativo o cero, intete nuevamente: ")
    while not cantidad_productos.isdigit():
        cantidad_productos = input("Por favor, ingrese un numero entero positivo: ")
    cantidad_productos = int(cantidad_productos)  


for i in range(cantidad_productos):
    precio = input(F"Ingrese el valor del producto {i + 1}: ")
    while not precio.isdigit():
        print("Por favor, ingrese un numero entero positivo: ")
        precio = input(F"Ingrese el valor del producto {i + 1}: ")

    precio = int(precio)

    while precio <= 0:
        print("No se puede ingresar un numero negativo o creo, intente nuevamente: ")
        precio = input(F"Ingrese el valor del producto {i + 1}: ")
        precio = int(precio)

    precio_total += precio
    preguntar_descuento = input(f"El producto {i + 1} tiene descuento? (S/N): ").capitalize()

    while preguntar_descuento != "S" and preguntar_descuento != "N":
        preguntar_descuento = input("Por favor, Ingrese S o N: ").capitalize()
        
    if preguntar_descuento == "S":
        descuento = precio * 10 / 100
        precio_final = precio - descuento
        ahorro += descuento
        precio_total_descuento += precio_final
    elif preguntar_descuento == "N":
        precio_total_descuento += precio
        pass   

    resumen += f"Producto {i + 1} - Precio: {precio} - Descuento: {preguntar_descuento}\n"

promedio = precio_total_descuento / cantidad_productos

print(f"Cliente: {nombre_cliente}")
print(f"Cantidad de productos: {cantidad_productos}")

print(resumen)

print(F"Total sin descuento: {precio_total}")
print(f"Total con descuento: {precio_total_descuento}")
print(f"Ahorro: {ahorro}")
print(f"Promedio por producto: {promedio:.2f}")