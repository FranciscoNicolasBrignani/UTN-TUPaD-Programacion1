# Trabajo práctico: Datos complejos - Francisco Brignani

# 1)
# Dado el diccionario precios_frutas:
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas.update({'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300})

print(precios_frutas)

# 2)
# Actualizar los precios de algunas frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

# 3)
# Crear una lista que contenga únicamente las frutas (sin los precios).

frutas = precios_frutas.keys()
print(frutas)

# 4)
# Programa para almacenar y consultar números telefónicos.
# - Permitir cargar 5 contactos (nombre: número).
# - Consultar un nombre y mostrar su número.

contactos = {}

for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número del contacto: ")
    contactos[nombre] = numero

print(contactos)

buscar_nombre = input("Ingrese el nombre a buscar: ")

if buscar_nombre in contactos:
    print(f"El número del contacto de {buscar_nombre} es {contactos[buscar_nombre]}")
else:
    print("No existe ese contacto.")

# 5)
# Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")
print(f"La frase es: {frase}")

palabras = frase.split()
frase_sin_repetir = set(palabras)

print(f"Palabras únicas: {frase_sin_repetir}")

contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1

print("Cantidad de apariciones de cada palabra:")
for palabra, cantidad in contador.items():
    print(f"{palabra}: {cantidad}")

# 6)
# Ingresar los nombres de 3 alumnos y para cada uno una tupla de 3 notas.
# Mostrar el promedio de cada alumno.

alumnos = []

for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    nota1 = float(input("Ingrese la nota 1: "))
    nota2 = float(input("Ingrese la nota 2: "))
    nota3 = float(input("Ingrese la nota 3: "))

    notas = (nota1, nota2, nota3)
    alumnos.append((nombre, notas))

print("Datos cargados:")
print(alumnos)

print("Promedio de cada alumno:")
for nombre, notas in alumnos:
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

# 7)
# Dados dos sets con los números de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrar los que aprobaron ambos.
# • Mostrar los que aprobaron solo uno.
# • Mostrar la lista total de los que aprobaron al menos un parcial (sin repetir).

# francisco = 102
# roberto = 110
# joaquin = 108
# luquitas = 111
# pepe = 90

parcial1 = {102, 110, 108, 111}
parcial2 = {102, 111, 90, 110}

ambos_parciales = parcial1 & parcial2
solo_un_parcial = parcial1 ^ parcial2
al_menos_un_parcial = parcial1 | parcial2

print(f"Estudiantes que aprobaron ambos parciales: {ambos_parciales}")
print(f"Estudiantes que aprobaron un solo parcial: {solo_un_parcial}")
print(f"Estudiantes que aprobaron al menos un parcial (sin repetir): {al_menos_un_parcial}")

# 8)
# Diccionario con productos y su stock.
# Permitir:
# • Consultar el stock de un producto.
# • Agregar unidades si existe.
# • Agregar un nuevo producto si no existe.

productos = {'televisor': 10900, 'netbook': 20420, 'celular': 2891, 'reloj': 242}

while True:
    print("\nMenú:")
    print("1. Consultar stock")
    print("2. Agregar unidades a un producto existente")
    print("3. Agregar un nuevo producto")
    print("4. Salir")

    opcion = int(input("Ingrese su opción: "))

    if opcion == 1:
        print(f"Productos en stock: {productos}")

    elif opcion == 2:
        producto_mod = input("Ingrese el producto a modificar: ").lower()
        if producto_mod in productos:
            print("Producto encontrado.")
            nuevo_stock = int(input("Ingrese el nuevo stock del producto: "))
            productos[producto_mod] = nuevo_stock
        else:
            print("El producto no existe.")

    elif opcion == 3:
        producto_add = input("Ingrese el nuevo producto: ").lower()
        if producto_add not in productos:
            nuevo_stock = int(input("Ingrese el stock inicial del producto: "))
            productos[producto_add] = nuevo_stock
            print("Producto agregado correctamente.")
        else:
            print("El producto ya está en el stock.")

    elif opcion == 4:
        print("Saliendo del programa.")
        break

    else:
        print("Opción inválida. Intente nuevamente.")

# 9)
# Agenda con tuplas (día, hora) como claves.
# Permitir consultar qué actividad hay en cierto día y hora.

agenda = {
    ("lunes", "09:00"): "Estudiar inglés",
    ("lunes", "14:00"): "Entrenar",
    ("martes", "10:00"): "Descansar",
    ("martes", "16:00"): "Estudiar programación",
    ("miércoles", "08:00"): "Leer",
    ("miércoles", "15:00"): "Reunión con amigos",
    ("jueves", "11:00"): "Hacer la comida para la semana",
    ("jueves", "17:00"): "Clases de inglés",
    ("viernes", "09:30"): "Organizar la agenda",
    ("viernes", "13:00"): "Almuerzo"
}

def consultar_actividad(dia, hora):
    clave = (dia, hora)
    if clave in agenda:
        return f"En {dia} a las {hora}: {agenda[clave]}"
    else:
        return f"No hay actividad programada para {dia} a las {hora}"

dia = input("Ingresá el día que querés consultar: ").lower()
hora = input("Ingresá la hora (formato HH:MM): ")

print(consultar_actividad(dia, hora))

# 10)
# Dado un diccionario con países y capitales, construir otro donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

paises_y_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Colombia": "Bogotá",
    "Perú": "Lima",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción",
    "Bolivia": "La Paz",
    "Ecuador": "Quito",
    "Venezuela": "Caracas"
}

capitales_paises = {capital: pais for pais, capital in paises_y_capitales.items()}

print("**" * 10)
print("Diccionario original:")
for pais, capital in paises_y_capitales.items():
    print(f"{pais} : {capital}")
print("**" * 10)

print("Diccionario invertido:")
for capital, pais in capitales_paises.items():
    print(f"{capital} : {pais}")
print("**" * 10)
