#Ejercicio 1

nombre = input("Ingresar nombre del cliente: ")
while nombre == "" or not nombre.isalpha():
    print("El nombre no puede estar vacio y solo contener letras.")
    nombre = input("Ingresar nombre del cliente nuevamente: ")

cant_a_comprar = input("Ingresar cantidad de productos a comprar: ")
while not cant_a_comprar.isdigit() or int(cant_a_comprar) <= 0:
    print("No ingresar 0 y solo numeros enteros.")
    cant_a_comprar = input("Ingresar cantidad de productos a comprar nuevamente: ")

cantidad = int(cant_a_comprar)

total_con_descuento = 0
total_sin_descuento = 0
for i in range(1, cantidad + 1):
    precio = input(f"Producto {i}. Precio: ")

    while not precio.isdigit():
        print("El precio debe ser un numero entero.")
        precio = input(f"Producto {i}. Precio: ")

    precio = int(precio)

    descuento = input("Descuento S/N: ").lower()

    total_sin_descuento += precio

    while descuento != "s" and descuento != "n":
        print("Debe ingresar S o N.")
        descuento = input("Descuentop S/N: ").lower()

    if descuento == "s":
        precio_descuento = precio * 0.90
        total_con_descuento += precio_descuento
    else:
        total_con_descuento += precio


ahorro = total_sin_descuento - total_con_descuento
promedio = float(total_con_descuento / cantidad)

print()
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento}")
print(f"Ahorro: ${ahorro}")
print(f"Promedio por producto: ${promedio:.2f}")
