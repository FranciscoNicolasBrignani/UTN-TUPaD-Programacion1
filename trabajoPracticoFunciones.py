#Trabajo practico Francisco Brignani

#1. Crear una función llamada imprimir_hola_mundo que imprima por
 #pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
 #programa principal.

def imprimir_hola_mundo():
    print("Hola mundo!")

#2. Crear una función llamada saludar_usuario(nombre) que reciba
 #como parámetro un nombre y devuelva un saludo personalizado.
 #Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
 #volver: “Hola Marcos!”. Llamar a esta función desde el programa
 #principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print(f"Hola {nombre}")


#3. Crear una función llamada informacion_personal(nombre, apellido,
 #edad, residencia) que reciba cuatro parámetros e imprima: “Soy
 #[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
 #dir los datos al usuario y llamar a esta función con los valores in
 #gresados

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
 #dio como parámetro y devuelva el área del círculo. calcular_peri
 #metro_circulo(radio) que reciba el radio como parámetro y devuel
 #va el perímetro del círculo. Solicitar el radio al usuario y llamar am
 #bas funciones para mostrar los resultados.

def caclular_area_circulo(radio):
    area = 3.1416 * radio ** 2
    print(f"El area del circulo es: {area:.2f}")

def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.1416 * radio
    print(f"El perimetro del circulo es {perimetro:.2f}")

#5. Crear una función llamada segundos_a_horas(segundos) que reciba
 #una cantidad de segundos como parámetro y devuelva la cantidad
 #de horas correspondientes. Solicitar al usuario los segundos y mostrar 
 #el resultado usando esta función.

def segundos_a_horas(segundos):
    horas = segundos/3600
    print(f"La cantidad de segundos equvale a {horas:.2f} hora/s")

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
 #número como parámetro y imprima la tabla de multiplicar de ese
 #número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1,11):
        total = i * numero
        print (f"{numero} x {i} = {total}")

#7. Crear una función llamada operaciones_basicas(a, b) que reciba
 #dos números como parámetros y devuelva una tupla con el resultado 
 #de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a // b
    return (suma,resta,multiplicacion,division)

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
 #peso en kilogramos y la altura en metros, y devuelva el índice de
 #masa corporal (IMC). Solicitar al usuario los datos y llamar a la función 
 #para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = peso/ (altura ** 2)
    return imc

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
 #una temperatura en grados Celsius y devuelva su equivalente en
 #Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
 #resultado usando la función.

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
 #tres números como parámetros y devuelva el promedio de ellos.
 #Solicitar los números al usuario y mostrar el resultado usando esta
 #función.

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

#Programa principal

#1)
imprimir_hola_mundo()

#2)
nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)

#3)
nombreI = input("Ingrese su nombre: ")
apellidoI = input("Ingrese su apellido: ")
edadI = int (input("Ingrese su edad: "))
residenciaI = input("Ingrese su residencia: ")

informacion_personal(nombreI,apellidoI,edadI,residenciaI)

#4)
radio = int(input("Ingrese el radio del circulo: "))
caclular_area_circulo(radio)
calcular_perimetro_circulo(radio)

#5)
segundos = int(input("Ingrese los segundos: "))
segundos_a_horas(segundos)

#6)
numero = int(input("Ingrese el numero para la tabla: "))
tabla_multiplicar(numero)

#7)
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

resultados = operaciones_basicas(a,b)

print(f"Suma {resultados[0]}")
print(f"Resta {resultados[1]}")
print(f"Multiplicacion {resultados[2]}")
print(f"Division {resultados[3]}")

#8)
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso,altura)

print(f"Tu IMC es: {imc:.2f}")

#9)
temp_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)
print(f"{temp_celsius}°C equivalen a {temp_fahrenheit:.2f}°F")

#10)
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio es: {promedio:.2f}")