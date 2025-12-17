productos = {
    1: ("Hamburguesa", 8.50),
    2: ("Pizza", 10.00),
    3: ("Hot Dog", 5.00),
    4: ("Papas Fritas", 3.50),
    5: ("Ensalada", 6.00),
    6: ("Pollo Asado", 12.00),
    7: ("Tacos", 7.00),
    8: ("Sopa", 4.50),
    9: ("Refresco", 2.00),
    10: ("Postre", 4.00)
}

factura = []
total = 0

while True:
    print("\n===== MENÚ DEL RESTAURANTE =====")
    for clave, valor in productos.items():
        print(f"{clave}. {valor[0]} - ${valor[1]:.2f}")
    print("0. Salir y mostrar factura")
    opcion = int(input("Seleccione un producto: "))

    if opcion == 0:
        break
    elif opcion in productos:
        cantidad = int(input("Ingrese la cantidad: "))
        nombre, precio = productos[opcion]
        subtotal = precio * cantidad
        factura.append((nombre, cantidad, precio, subtotal))
        total += subtotal
        print(f"Producto agregado: {nombre}")
    else:
        print("Opción inválida, intente de nuevo.")

print("\n===== FACTURA =====")

for item in factura:
    print(f"{item[0]} x{item[1]} - ${item[3]:.2f}")

print(f"\nTOTAL A PAGAR: ${total:.2f}")
print("Gracias por su compra")