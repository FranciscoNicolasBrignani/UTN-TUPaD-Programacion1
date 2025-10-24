#Francisco Brignani
#Trabajo Practico recursividad

#1)   Crea una función recursiva que calcule el factorial de un número. Luego, 
# utiliza esa función para calcular y mostrar en pantalla el factorial de todos 
# los números enteros entre 1 y el número que indique el usuario

num = int(input("Ingrese un numero: "))

def factorialNum(num):
    
    if num == 0: 
        return 1 
    else:
        return num * factorialNum(num-1)
        
        
resultado = print(factorialNum(num))

#2)Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

nU = int(input("Ingrese la posicion: "))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def serie(n, actual = 0):
    if actual <= n:
        print(fibonacci(actual))
        serie(n,actual + 1)

serie(nU)

#3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente,
# utilizando la fórmula. Prueba esta función en un algoritmo general

numero = float(input("Ingrese el numero: "))
exponente = int(input("Ingrese el exponenete: "))

def potenciaDeUnNumero(numero, exponente):
    if exponente == 0:
        return 1
    else:
        return numero * potenciaDeUnNumero(numero, exponente-1)
    

potenciaF = print(potenciaDeUnNumero(numero, exponente))

#4)   Crear una función recursiva en Python que reciba un número entero positivo en base decimal 
# y devuelva su representación en binario como una cadena de texto.

numeroEntero = int(input("Ingrese un numero entero: "))

def enteroaBinario(numeroEntero):
    if numeroEntero == 0:
        return 0
    else:
        return numeroEntero % 2 + 10 * enteroaBinario(numeroEntero // 2)

print(enteroaBinario(numeroEntero))

#5)Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto
# sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.

palabra = input("Ingrese una palabra: ")

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])
                

resultadoPalindromo = es_palindromo(palabra)
print(resultadoPalindromo)

#6)   Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero 
# positivo y devuelva la suma de todos sus dígitos.

input_num = int(input("Ingrese un numero entero positivo: "))

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)
    
resultadoSuma = suma_digitos(input_num)
print(resultadoSuma)


#7)   Un niño está construyendo una pirámide con bloques. 
# En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), 
# y así sucesivamente hasta llegar al último nivel con un solo bloque.

niveles = int(input("Ingrese la cantidad de niveles de la piramide: "))

def bloques_piramide(niveles):
    if niveles == 1:
        return 1
    else:
        return niveles + bloques_piramide(niveles - 1)
total_bloques = bloques_piramide(niveles)
print(total_bloques)

#8)   Escribí una función recursiva llamada contar_digito(numero, digito) 
# que reciba un número entero positivo (numero) y un dígito (entre 0 y 9),
#  y devuelva cuántas veces aparece ese dígito dentro del número

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)
num_input = int(input("Ingrese un numero entero positivo: "))
digito_input = int(input("Ingrese un digito entre 0 y 9: "))    
resultadoContar = contar_digito(num_input, digito_input)
print(resultadoContar)