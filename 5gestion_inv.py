""" Diseña un sistema para gestionar el inventario de una tienda. El inventario se almacenará en una lista de diccionarios. Cada diccionario representará un producto con "nombre", "precio" y "cantidad". El programa debe:
• Usar funciones para cada operación: agregar_producto(), realizar_venta(),
mostrar_inventario().
• La función realizar_venta() debe actualizar la cantidad del producto vendido.
• Mostrar un menú interactivo para el usuario.
• Conceptos integrados: Listas, diccionarios, funciones, bucles,
condicionales. """

# Ejercicio 5 : mini sistema de gestion de inventario
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))