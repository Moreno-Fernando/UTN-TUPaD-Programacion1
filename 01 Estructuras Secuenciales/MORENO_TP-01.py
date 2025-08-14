# Ejercicio 1

print("Hola Mundo!")

# Ejercicio 2

name = input("Cual es tu nombre? ")
print(f"Hola {name}!")

# Ejercico 3

name = input("Ingrese su nombre: ")
surname = input("Ingrese su apellido: ")
age = int(input("Ingrese su edad: "))
print(f"Soy {name} {surname}, tengo {age} años y vivo en Argentina.")

#Ejercicio 4

radius = float(input("Ingrese el radio del circulo: "))
perimeter = (radius * 2) * 3.14
area = 3.14 * (radius**2)
print(f"El perimetro del circulo es: {perimeter:.2f} - El area del circulo es: {area:.2f}")

# Ejercicio 5

seconds = int(input("Ingrese una cantidad de segundos: "))
minutes = seconds / 60
hours = minutes / 60
print(f"{seconds} segundos son equivalentes a {hours} horas.")

# Ejercicio 6

num = int(input("Ingrese un numero: "))
print(f"Tabla de multiplicar del {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Ejercicio 7

num1 = int(input("Ingrese el primer numero distinto de cero: "))
num2 = int(input("Ingrese el segundo numero distinto de cero: "))
print(f"La suma de {num1} + {num2} = {num1 + num2}.")
print(f"La resta de {num1} - {num2} = {num1 - num2}.")
print(f"La multiplicacion de {num1} * {num2} = {num1 * num2}.")
print(f"La division de {num1} / {num2} = {num1 / num2}.")

# Ejercicio 8

height = float(input("Ingrese su altura en metros: "))
weight = float(input("Ingrese su peso en kilos: "))
imc = weight / (height ** 2)
print(f"Su indice de masa corporal es: {imc:.2f}")

 # Ejercicio 9

tempCelcius = float(input("Ingrese temperatura en Celsius: "))
tempFahrenheit = (tempCelcius * 9/5) + 32
print(f"El equivalente de {tempCelcius}ºC a Fahrenheit es {tempFahrenheit:.2f}ºF")

# Ejercicio 10

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
prom = (num1 + num2 + num3) / 3
print(f"El promedio es: {prom}")
