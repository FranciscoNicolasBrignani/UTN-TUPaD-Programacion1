#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print("hola mundo")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.

nombre = input("Ingrese su nombre: ")

print(f"Hola, {Nombre}")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

radio = int(input("Ingrese el radio del circulo: "))

area = radio * radio * 3.14159
perimetro = 2 * radio * 3.14159

print(f"El area es: {area} y su perimetro es {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

segundos = int(input("Ingrese la cantidad de segundos: "))

horas = segundos / 60

print(f"La cantidad de horas son: {horas}")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

numero = int(input("Ingrese un numero: "))

resultado1 = numero * 1
resultado2 = numero * 2
resultado3 = numero * 3
resultado4 = numero * 4
resultado5 = numero * 5
resultado6 = numero * 6
resultado7 = numero * 7
resultado8 = numero * 8
resultado9 = numero * 9
resultado10 = numero * 10

print (f"{numero} x 1 = {resultado1}")
print (f"{numero} x 2 = {resultado2}")
print (f"{numero} x 3 = {resultado3}")
print (f"{numero} x 4 = {resultado4}")
print (f"{numero} x 5 = {resultado5}")
print (f"{numero} x 6 = {resultado6}")
print (f"{numero} x 7 = {resultado7}")
print (f"{numero} x 8 = {resultado8}")
print (f"{numero} x 9 = {resultado9}")
print (f"{numero} x 10 = {resultado10}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

suma = numero1 + numero2
resta = numero1 - numero2
division = numero1 / numero2
multiplicacion = numero1 * numero2

print(f"La suma de ambos numeros es: {suma}")
print(f"La resta de ambos numeros es: {resta}")
print(f"La division de ambos numeros es: {division}")
print(f"La multiplicacion de ambos numeros es: {multiplicacion}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal.

peso = int(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura en m: "))



imc = peso / (altura * altura)

print(f"Su IMC es: {imc}")


#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

temperatura_celsius = float(input("Ingrese la temperatura en celsius: "))

fahrenheit = (temperatura_celsius * 9/5) + 32

print(f"La temperatura en fahrenheit es: {fahrenheit}")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

primer_numero = float(input("Ingrese el 1er numero: "))
segundo_numero = float(input("Ingrese el 2do numero: "))
tercer_numero  = float(input("Ingrese el 3er numero: "))

resultadoo = (primer_numero + segundo_numero + tercer_numero) / 3

print(f"El resultado es: {resultadoo}")