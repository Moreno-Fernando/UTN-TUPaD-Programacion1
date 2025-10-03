# Ejercicio 1

def imprimir_hola_mundo():
    return print("Hola Mundo!")

imprimir_hola_mundo()


# Ejercicio 2

def saludar_usuario(nombre):
    return print(f"Hola {nombre}!")

saludar_usuario("Marcos")


# Ejercicio 3

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu ciudad de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)


# Ejercicio 4

import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingresa el radio del circulo: "))
    
if radio <= 0:
    print("Error: El radio debe ser un numero positivo.")
else:
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"Area: {area:.2f}")
    print(f"Perimetro: {perimetro:.2f}")


# Ejercicio 5

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = float(input("Ingresa la cantidad de segundos: "))
    
if segundos < 0:
    print("Error: La cantidad de segundos no puede ser negativo.")
else:
    horas = segundos_a_horas(segundos)
    print(f"{segundos} segundos equivalen a {horas:.2f} horas")


# Ejercicio 6

def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} × {i} = {resultado}")

numero = int(input("Ingresa un numero para generar su tabla de multiplicar: "))
tabla_multiplicar(numero)



# Ejercicio 7

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir por 0"
    
    return suma, resta, multiplicacion, division

num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))

resultados = operaciones_basicas(num1, num2)

print(f"Resultados para {num1} y {num2}")
print(f"Suma: {num1} + {num2} = {resultados[0]}")
print(f"Resta: {num1} - {num2} = {resultados[1]}")
print(f"Multiplicacion: {num1} × {num2} = {resultados[2]}")
print(f"Division: {num1} ÷ {num2} = {resultados[3]}")



# Ejercicio 8

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingresa tu peso en kgs: "))
altura = float(input("Ingresa tu altura en metros: "))

if peso <= 0 or altura <= 0:
    print("Error: El peso y la altura deben ser valores positivos.")
else:
    imc = calcular_imc(peso, altura)
    print(f"Tu indice de Masa Corporal (IMC) es: {imc:.2f}")



# Ejercicio 9

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingresa la temperatura en grados Celsius: "))

fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")



# Ejercicio 10

def calcular_promedio(num1, num2, num3):
    return (num1 + num2 + num3) / 3

num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))
num3 = float(input("Ingresa el tercer numero: "))

promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")