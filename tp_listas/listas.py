import random

#1) Crear una lista con las notas de 10 estudiantes. 
#• Mostrar la lista completa. 
#• Calcular y mostrar el promedio. 
#• Indicar la nota más alta y la más baja.

notas = [10, 9, 7, 2, 8, 6, 5, 4, 3, 1]
print("Lista de notas:", notas)
promedio = sum(notas) / len(notas)
print("Promedio de notas:", promedio)
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))

#2) Pedir al usuario que cargue 5 productos en una lista. 
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista. 

productos = []

for i in range(5):
    producto = input("Ingrese el nombre del producto: ")
    productos.append(producto)
    i += 1
productos = sorted(productos)
print("Lista de productos ordenada alfabéticamente:", productos)

eliminar = input("Ingrese el nombre del producto que desea eliminar: ")

if eliminar in productos:
    productos.remove(eliminar)
    print("Producto eliminado. Lista actualizada:", productos)

#3) Generar una lista con 15 números enteros al azar entre 1 y 100. 
#• Crear una lista con los pares y otra con los impares. 
#• Mostrar cuántos números tiene cada lista. 

numeros = [random.randint(1, 100) for _ in range(15)]
pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]
print("Cantidad de números pares:", len(pares))
print("Cantidad de números impares:", len(impares))


#4) Dada una lista con valores repetidos: 
#• Crear una nueva lista sin elementos repetidos. 
#• Mostrar el resultado. 

datos = [1,3,5,3,7,1,9,5,3]
nueva_lista = list(set(datos))
print(nueva_lista)


#5) Crear una lista con los nombres de 8 estudiantes presentes en clase. 
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
#• Mostrar la lista final actualizada. 

nombres_estudiantes = ["ana", "luis", "carlos", "marta", "sofia", "jorge", "lucia", "pedro"]
print("Lista inicial de estudiantes:", nombres_estudiantes)

agregar = input("¿Quieres agregar un nuevo estudiante? (s/n): ").strip().lower()

if agregar == 's':
    nuevo_estudiante = input("Ingresa el nombre del nuevo estudiante: ").strip()
    nombres_estudiantes.append(nuevo_estudiante)
    print(f"{nuevo_estudiante} ha sido agregado a la lista.")
    print("Lista actualizada de estudiantes:", nombres_estudiantes)
else:
    eliminar = input("¿Quieres eliminar un estudiante existente? (s/n): ").strip().lower()
    if eliminar == 's':
        estudiante_a_eliminar = input("Ingresa el nombre del estudiante a eliminar: ").strip().lower()
        if estudiante_a_eliminar in nombres_estudiantes:
            nombres_estudiantes.remove(estudiante_a_eliminar)
            print(f"{estudiante_a_eliminar} ha sido eliminado de la lista.")
            print("Lista actualizada de estudiantes:", nombres_estudiantes)
        else:
            print(f"{estudiante_a_eliminar} no se encuentra en la lista.")



#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
#último pasa a ser el primero). 


numeros = [random.randint(1, 100) for _ in range(7)]
print("Lista original:", numeros)

rotar = numeros[-1:] + numeros[:-1]
print("Lista rotada:", rotar)



#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana. 
#• Calcular el promedio de las mínimas y el de las máximas. 
#• Mostrar en qué día se registró la mayor amplitud térmica.

matriz_temperaturas = []
for i in range(7):
    temp_min = random.randint(-10, 15)  
    temp_max = random.randint(16, 35)   
    matriz_temperaturas.append([temp_min, temp_max])
    print(f"Día {i+1}: Mínima = {temp_min}°C, Máxima = {temp_max}°C")

promedio_min = sum(f[0] for f in matriz_temperaturas) / 7
promedio_max = sum(f[1] for f in matriz_temperaturas) / 7

print(f"Promedio Mínimas: {promedio_min}°C")
print(f"Promedio Máximas: {promedio_max}°C")

mayor_amplitud = 0
dia_mayor_amplitud = -1

for i, (min_temp, max_temp) in enumerate(matriz_temperaturas):
    amplitud = max_temp - min_temp
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = i + 1

print(f"Día con mayor amplitud térmica: Día {dia_mayor_amplitud} ({mayor_amplitud}°C)")


#8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
#• Mostrar el promedio de cada estudiante. 
#• Mostrar el promedio de cada materia.

matriz_notas = []
for i in range(5):
    notas_estudiante = [random.randint(0, 10) for _ in range(3)]
    matriz_notas.append(notas_estudiante)
    print(f"Notas del Estudiante {i+1}: {notas_estudiante}")

for i, notas in enumerate(matriz_notas):
    promedio = sum(notas) / len(notas)
    print(f"Promedio del Estudiante {i+1}: {promedio}")

for j in range(3):
    promedio_materia = sum(matriz_notas[i][j] for i in range(5)) / 5
    print(f"Promedio de la Materia {j+1}: {promedio_materia}")


#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
#• Inicializarlo con guiones "-" representando casillas vacías. 
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
#• Mostrar el tablero después de cada jugada. 

ta_te_te = [["-" for _ in range(3)] for _ in range(3)]
print("Tablero inicial:")
for fila in ta_te_te:
    print(" ".join(fila))
turnos = ["X", "O"]
for turno in range(9):
    jugador = turno % 2
    fila = int(input(f"Jugador {turnos[jugador]}, ingresa fila (0-2): "))
    columna = int(input(f"Jugador {turnos[jugador]}, ingresa columna (0-2): "))
    if 0 <= fila < 3 and 0 <= columna < 3:
        if ta_te_te[fila][columna] == "-":
            ta_te_te[fila][columna] = turnos[jugador]
        else:
            print("Casilla ocupada, intenta de nuevo.")
    else:
        print("Posición inválida, intenta de nuevo.")
    for fila in ta_te_te:
        print(" ".join(fila))
    print()

#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
#• Mostrar el total vendido por cada producto. 
#• Mostrar el día con mayores ventas totales. 
#• Indicar cuál fue el producto más vendido en la semana. 

ventas = [[random.randint(0, 100) for _ in range(7)] for _ in range(4)]
print("Ventas diarias por producto:")
for i, producto in enumerate(ventas):
    print(f"Producto {i + 1}: {producto}")

totales_productos = [sum(producto) for producto in ventas]
for i, total in enumerate(totales_productos):
    print(f"Total vendido del Producto {i + 1}: {total}")

ventas_diarias = [sum(dia) for dia in zip(*ventas)]
dia_mayor_venta = ventas_diarias.index(max(ventas_diarias)) + 1
print(f"Día con mayores ventas totales: Día {dia_mayor_venta}")

producto_mas_vendido = totales_productos.index(max(totales_productos)) + 1
print(f"Producto más vendido en la semana: Producto {producto_mas_vendido}")
