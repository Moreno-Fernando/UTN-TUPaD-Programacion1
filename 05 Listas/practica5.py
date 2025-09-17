# Ejercicio 1

notas = [6, 7, 8, 9, 10, 8, 7, 2, 4, 6]
c = 0
suma = 0
nota_alta = 0
nota_baja = 10
for i in notas:
    print(f"Nota Estudiante: {i}")
    c += 1
    suma += i
    if i > nota_alta:
        nota_alta = i
    if i < nota_baja:
        nota_baja = i
print(f"Promedio: {suma/c} - Nota más alta: {nota_alta} - Nota mas baja: {nota_baja}")


# Ejercicio 2

productos = []
print("Ingrese 5 productos:")
for i in range(5):
    producto = input (f"Producto {i + 1}: ")
    productos.append(producto)

productos.sort()

for i, producto in enumerate(productos, 1):
    print(f"{i}- {producto}")

while True:
    producto_eliminar = input("Que producto desea eliminar? ")

    if producto_eliminar in productos:
        productos.remove(producto_eliminar)
        break
    else:
        print("Escribe un producto que figure en la lista.")

productos.sort()

for i, producto in enumerate(productos, 1):
    print(f"{i}- {producto}")


# Ejercicio 3

import random
pares = []
impares = []
lista = []
for i in range(1, 101):
    num = random.randint(1, 100)
    lista.append(num)

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f"lista completo: {lista}")
print("-------------------------")
print(f"Lista de pares ({len(pares)}): {pares}")
print("-------------------------")
print(f"Lista de impares ({len(impares)}): {impares}")


# Ejercicio 4

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_repetidos = []
for i in datos:
    if not (i in sin_repetidos):
        sin_repetidos.append(i)
print(sin_repetidos)


# Ejercicio 5

estudiantes = ["Fernando", "Luis", "Elian", "Daiana", "Noemi", "Tomas", "Moreno", "Soto"]
print(f"Lista de Estudiantes:")
print(estudiantes)
print("-------------")
opcion = int(input("Elija una opcion:\n1- Agregar estudiante\n2- Borrar estudiante\n"))
if opcion == 1:
    nuevo = input("Agregue el estudiante: ")
    estudiantes.append(nuevo)
else:
    eliminar = input("Nombre a eliminar: ")
    estudiantes.remove(eliminar)

print(estudiantes)


# Ejercicio 6

numeros = [1, 2, 3, 4, 5, 6, 7]
rotados = [numeros[-1]] + numeros[:-1]
print(f"Lista original: {numeros}")
print(f"Lista rotada: {rotados}")


# Ejercicio 7

temperaturas = [
    [30, 32, 31, 33, 34, 29, 28],
    [20, 21, 19, 22, 24, 20, 23]
]

prom_min = 0
prom_max = 0
suma = 0
temp_max = 0
temp_min = 99

for i in temperaturas[0]:
    suma += i
    if i > temp_max:
        temp_max = i

prom_max = suma / 7

suma = 0
for i in temperaturas[1]:
    suma += i
    if i < temp_min:
        temp_min = i

prom_min = suma / 7

print(f"Temperatura maxima de la semana {temp_max}ºC y el promedio es: {prom_max:.2f}ºC")
print(f"Temperatura minima de la semana {temp_min}ºC y el promedio es: {prom_min:.2f}ºC")


# Ejercicio 8

notas_estudiantes = [
    [7, 8, 9],
    [8, 6, 6],
    [9, 8, 9],
    [10, 9, 9],
    [6, 7, 8]
]

promedio_estudiante = 0
promedio_materia = 0


for materia in range(3):
    suma_materia = 0
    for nota in range(5):
        suma_materia += notas_estudiantes[nota][materia]
    promedio_materia = suma_materia / 5
    print(f"promedio materia {materia}: {promedio_materia:.2f}")

for i in range(5):
    suma = 0
    for nota in notas_estudiantes[i]:
        suma += nota
    prom = suma / 3
    suma = 0
    print(f"promedio estudiante {i} es {prom:.2f}")


# Ejercicio 9

tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
print("Juego Ta-Te-Ti\n---------------")
for i in tablero:
    print(i)

intentos = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]

for i in intentos:
    print(f"seleccione donde colocar '{i}', primero fila y luego columna")
    fila = int(input("ingrese posicion fila (de 1 a 3): "))
    columna = int(input("Ingrese posicion columna (de 1 a 3): "))

    while tablero[fila - 1][columna - 1] == "X" or tablero[fila - 1][columna - 1] == "O":
        print("debes elegir una posicion correcta, intenta nuevamente")
        print(f"seleccione donde colocar '{i}', primero fila y luego columna")
        fila = int(input("ingrese posicion fila (de 1 a 3): "))
        columna = int(input("Ingrese posicion columna (de 1 a 3): "))
    
    tablero[fila - 1][columna - 1] = i

    print("Juego Ta-Te-Ti\n---------------")
    for i in tablero:
        print(i)



# Ejercicio 10

ventas = [
    [11, 82, 73, 64, 45, 36, 17],
    [3, 22, 5, 4, 15, 26, 37],
    [12, 23, 33, 14, 5, 64, 7],
    [14, 22, 3, 54, 85, 66, 57],
]

dias = ["domingo", "lunes", "martes", "miercoles", "jueves", "viernes", "sabado"]
contador = 0
contador_producto = 0

dias_mayores_ventas = 0
monto_dia_mayores_ventas = 0
producto_mas_vendido = 0
posicion_prod_mas_vendido = 0
suma_producto_mas_vendido = 0
total_por_dia = []

for i in ventas:
    suma_producto = 0
    for producto in i:
        suma_producto += producto
    if suma_producto > producto_mas_vendido:
        producto_mas_vendido = suma_producto
        posicion_prod_mas_vendido += 1
    contador_producto += 1
    print(f"Total vendido por producto Nº{contador_producto}: {suma_producto}")

for dia in range(7):
    suma_del_dia = 0
    for producto in range(4):
        suma_del_dia += ventas[producto][dia]
    total_por_dia.append(suma_del_dia)

for i in total_por_dia:
    print(f"Total por dia {dias[contador]}: {i}")
    if monto_dia_mayores_ventas < i:
        monto_dia_mayores_ventas = i
        dias_mayores_ventas = contador
    contador += 1

print(f"dia que se vendio mas: {dias[dias_mayores_ventas]}")
print(f"producto mas vendido de la semana fue producto Nº{posicion_prod_mas_vendido}: {producto_mas_vendido}")