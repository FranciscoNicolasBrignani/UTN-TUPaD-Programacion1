import random

#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

numero1 = 0

for nummero1 in range (101):
    print(numero1)
    numero1+=1

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene. 

numero2 = int(input("Ingrese un numero: "))

digitos2 = len(str( numero2))

print("La cantidad de digitos es: ",digitos2)

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores.

numero3 = int(input("Ingrese el 1er numero: "))
numero33 = int(input("Ingrese el 2do numero: "))

numeroComprendido = 0

suma = 0
for i in range(numero3+1, numero33):
    suma +=i

print("La suma de los numeros comprendidos es: ",suma)



#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#un 0.

acumulador = 0
numero4 = 1

print("Ingrese un numero para sumar si no ingrese '0': ")

while numero4 != 0:
    numero4 = int(input("Numeros: "))
    if numero4 == 0:
        break
    acumulador += numero4

print("La suma de los numeros es: ", acumulador)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

intentos = 0
jugador = 0
numeroRandom = random.randint(0,9)

jugador = int(input("Ingrese un nuemero: "))

if jugador == numeroRandom:
    print("Ganaste!")
else:
    intentos+=1

while jugador != numeroRandom:
    print("Perdiste intenta de nuevo:")
    jugador = int(input("Ingrese un nuemero: "))
    intentos+=1

print("Ganaste!, la cantidad de intentos fue: ",intentos)


#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente.

numero6 = 0

while numero6 <= 100:
    numero6+=1
    if numero6 %2 == 0:
        print(numero6)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario.

numero7 = int(input("Ingrese un numero: "))
suma7 = 0

for i in range(numero7+1):
    suma7 = i + numero7
    print("La suma de los numeros: ", numero7, "+", i, "=", suma7)
    i=+1

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos.

numero8 = 0
contadorPar = 0
contadorImpar = 0
contadorP = 0
contadorN = 0

for i in range(100):
    numero8 = int(input(f"Ingrese el numero {i+1}:"))

    if numero8 % 2 == 0:
        contadorPar+=1
    else:
        contadorImpar+=1

    if numero8 > 0:
        contadorP+=1
    elif numero8 < 0:
        contadorN+=1
    else:
        print("Ingresaste un 0 no es positivo ni negativo")

print("Pares: ", contadorPar)
print("Impart: ", contadorImpar)
print("Positivos: ", contadorP)
print("Negativos: ", contadorN)

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores.

cantidad9 = 0
suma9 = 0

while cantidad9 < 100:
    numero9 = int(input("Ingrese un numero: "))
    suma9 = (suma9 + numero9)
    cantidad9+=1

print("La media es:",suma9/100)

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario.

numero10 = input("Ingrese un numero: ")
invertido = ""

for i in range(len(numero10)):
    invertido = numero10[i] + invertido

print("El numero original es:",numero10)
print("El numero invertido es:",invertido)
