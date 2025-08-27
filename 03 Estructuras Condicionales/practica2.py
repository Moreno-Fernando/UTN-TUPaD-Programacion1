# Ejercicio 1

age = int(input("Ingrese su edad: "))
if age >= 18:
    print("Es mayor de edad")

# Ejercicio 2

note = int(input("Ingrese su nota: "))
if note >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Ejercicio 3

num = int(input("Ingrese un numero par: "))
if num % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

# Ejercicio 4

age = int(input("Ingrese su edad: "))
if age < 12:
    print("Niño/a")
elif age >= 12 and age < 18:
    print("Adolescente")
elif age >= 18 and age < 30:
    print("Adulto joven")
elif age >= 30:
    print("Adulto")
else:
    print("edad invalida")


# Ejercicio 5
password = len(input("Ingrese una contraseña entre 8 y 14 caracteres: "))
if password >= 8 and password <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6

from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
if media > mediana:
    print("Sesgo positivo")
elif media < mediana:
    print("sesgo negativo")
else:
    print("Sin sesgo")

# Ejercicio 7

frase = input("Ingrese una frase o palabra: ")
vocales = ["a", "e", "i", "o", "u"]
ultimo_caracter = frase[-1].lower()
if frase and ultimo_caracter in vocales:
    print(f"{frase}!")
else:
    print(frase)

# Ejercicio 8

nombre = input("Ingrese su nombre: ")
eleccion = int(input("ingrese una opcion:\n1. Si quiere su nombre en mayusculas\n2. Si quiere su nombre en minusculas\n3. Si quiere su nombre con la primer letra en mayusculas\n"))
if eleccion == 1:
    print(nombre.upper())
elif eleccion == 2:
    print(nombre.lower())
elif eleccion == 3:
    print(nombre.title())
else:
    print("error en opcion")

# Ejercicio 9

magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
        print("muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
        print("leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
        print("moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
        print("fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
        print("muy Fuerte (puede causar daños significativos)")
elif magnitud >= 7:
        print("extremo (puede causar graves daños a gran escala)")
else:
        print("valor desconocido")
    
# Ejercicio 10

emisferio = input("En cual emisferio se encuentra? N/S ").upper()
mes = input("Que mes del año es: ").lower()
dia = int(input("Que dia es: "))
if (mes == "diciembre" and dia >= 21) or (mes == "enero") or (mes == "febrero") or (mes == "marzo" and dia <= 21):
     if emisferio == "N":
          print("invierno")
     elif emisferio == "S":
          print("verano")
elif (mes == "marzo" and dia >= 21) or (mes == "abril") or (mes == "mayo") or (mes == "junio" and dia <= 20):
     if emisferio == "N":
          print("primavera")
     elif emisferio == "S":
          print("otoño")
elif (mes == "junio" and dia >= 21) or (mes == "julio") or (mes == "agosto") or (mes == "septiembre" and dia <= 20):
        if emisferio == "N":
            print("verano")
        elif emisferio == "S":
            print("invierno")
elif (mes == "septiembre" and dia >= 21) or (mes == "octubre") or (mes == "noviembre") or (mes == "diciembre" and dia <= 20):
        if emisferio == "N":
            print("otoño")
        elif emisferio == "S":
            print("primavera")
