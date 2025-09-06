# Ejercicio 1

for i in range(0,101):
    print(f"{i}\n")


# Ejercicio 2

numero = input("Ingrese un numero entero: ")
contador = 0
for digito in numero:
    if digito.isdigit():
        contador += 1
print(f"El numero tiene {contador} digitos")


# Ejercicio 3

n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese otro numero: "))
suma = 0

for i in range(n1 + 1, n2):
    print(f"valor de i: {i}")
    suma = suma +i

print(suma)


# Ejercicio 4

suma = 0
i = 1
while i != 0:
    i = int(input("Ingrese un numero entero o 0 para salir: "))
    suma += i
print(f"Total {suma}")


# Ejercicio 5

import random
r = random.randint(1, 9)
i = 11
intentos = 0
while i != r:
    i = int(input("Adivina cual es el numero entre 0 y 9: "))
    intentos += 1

print(f"Intentaste {intentos} veces")


# Ejercicio 6

for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)


# Ejercicio 7

num = int(input("Ingrese un numero entero: "))
suma = 0
for i in range(0, num + 1):
    suma += i
print(f"Resultado: {suma}")


# Ejercicio 8

pares = 0
negativos = 0
positivos = 0
for i in range(0, 100):
    num = int(input("Ingrese un numero entero: "))
    if num < 0:
        negativos += 1
    else:
        positivos += 1
    if num % 2 == 0:
        pares += 1
print(f"Pares: {pares} - Positivos: {positivos} - Negativos: {negativos}")


# Ejercicio 9

contador = 0
suma = 0
for i in range(0, 100):
    num = int(input("Ingrese un numero entero: "))
    suma += num
    contador += 1
print(f"Media: {suma/contador}")


# Ejercicio 10

num = int(input("Ingrese un numero entero: "))
original = num
invertido = 0
while num > 0:
    ultimo = num % 10
    invertido = invertido * 10 + ultimo
    num //= 10
print (f"Original: {original} - Invertido: {invertido}")