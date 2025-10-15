#Francisco Brignani - Tp archivos

#1)
with open("productos.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Lapicera,3.99,100\n")
    archivo.write("Sacapuntas,1.50,50\n")
    archivo.write("Tijera,1.90,30\n")

#2)
with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

#3)
with open("productos.txt", "r", encoding="utf-8") as archivo:
    print("Lista de productos actuales:\n")
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")


print("\nIngrese un nuevo producto para agregar:")
nuevo_nombre = input("Nombre: ")
nuevo_precio = input("Precio: ")
nueva_cantidad = input("Cantidad: ")


with open("productos.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"\n{nuevo_nombre},{nuevo_precio},{nueva_cantidad}")

print("\nProducto agregado correctamente.")


#4)

productos = []

with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        linea = linea.strip()
        if not linea:
            continue
        
        partes = linea.split(",")
        if len(partes) != 3:
            print(f"Línea inválida omitida: {linea}")
            continue

        nombre, precio, cantidad = partes
        productos.append({
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        })

print("Lista de productos cargada:")
for p in productos:
    print(p)

#5)
nombre_buscar = input("Ingrese el nombre del producto a buscar: ")

encontrado = False
for p in productos:
    if p["nombre"].lower() == nombre_buscar.lower():  
        print(f"\nProducto encontrado:")
        print(f"Nombre: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("\nError: Producto no encontrado.")

#6)
with open("productos.txt", "w", encoding="utf-8") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("\nArchivo 'productos.txt' actualizado correctamente.")