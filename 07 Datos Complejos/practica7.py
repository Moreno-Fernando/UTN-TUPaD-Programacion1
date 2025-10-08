# Ejercicio 1

precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

# Ejercicio 2

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800

print(precios_frutas)


# Ejercicio 3

frutas = list(precios_frutas.keys())

print(frutas)


# Ejercicio 4

contactos = {}

print("# Carga de Contactos #")
print("Por favor, ingresa 5 contactos:")

# Cargar 5 contactos
for i in range(5):
    nombre = input(f"\nContacto {i+1} - Ingresa el nombre: ").strip()
    telefono = input(f"Contacto {i+1} - Ingresa el telefono: ").strip()
    
    # Almacenar en el diccionario
    contactos[nombre] = telefono

print(f"\nSe han cargado {len(contactos)} contactos correctamente")

# Consulta de contactos
print("\n" + "#"*40)
print("# Consulta de Contactos #")

while True:
    nombre_consulta = input("\nIngresa el nombre a consultar (o 'salir' para terminar): ").strip()
    
    if nombre_consulta.lower() == 'salir':
        print("Sistema cerrado.")
        break
    
    if nombre_consulta in contactos:
        print(f"Telefono de {nombre_consulta}: {contactos[nombre_consulta]}")
    else:
        print(f"El contacto '{nombre_consulta}' no existe en la agenda")


# Ejercicio 5

def vez_veces(frecuencia):
    if frecuencia == 1:
        return "vez"
    else:
        return "veces"
    
frase = input("Ingresa una frase: ")

palabras = frase.lower().split()

palabras_unicas = set(palabras)

frecuencia_palabras = {}

for palabra in palabras:
    frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1

print("\n" + "#"*50)
print("Resultado:")
print("#"*50)

print(f"\n1. Palabras Unicas ({len(palabras_unicas)} palabras):")
print(sorted(palabras_unicas))

print(f"\n2. Frecuencia de Palabras:")
for palabra, frecuencia in sorted(frecuencia_palabras.items()):
    print(f"   '{palabra}': {frecuencia} {vez_veces(frecuencia)}")


# Ejercicio 6

alumnos = {}

print("Sistema de Registro de Alumnos")
print("Ingresa los datos de 3 alumnos:")

for i in range(3):
    print(f"\n# Alumno {i+1} #")
    nombre = input("Nombre del alumno: ").strip()
    
    # Solicitar las 3 notas
    notas = []
    for j in range(3):
        while True:
            nota = float(input(f"Nota {j+1}: "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("Error: La nota debe estar entre 0 y 10")
    
    # almacenar como tupla en el diccionario
    alumnos[nombre] = tuple(notas)

# calcular y mostrar promedios
print("\n" + "#"*40)
print("Alumnos")
print("#"*40)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"\n{nombre}:")
    print(f"- Notas: {notas}")
    print(f"- Promedio: {promedio:.2f}")



# Ejercicio 7

parcial1 = {1, 2, 3, 4, 5, 6, 7}
parcial2 = {3, 4, 5, 8, 9, 10}

# Mostrar los sets originales
print("\nEstudiantes que aprobaron Parcial 1:")
print(sorted(parcial1))

print("\nEstudiantes que aprobaron Parcial 2:")
print(sorted(parcial2))

# Estudiantes que aprobaron ambos parciales
ambos = parcial1 & parcial2
print("\nEstudiantes que aprobaron ambos parciales:")
print(sorted(ambos))
print(f"Total: {len(ambos)} estudiantes")

# Estudiantes que aprobaron solo uno de los dos
solo_uno = parcial1 ^ parcial2
print("\nEstudiantes que aprobaron solo uno de los dos:")
print(sorted(solo_uno))
print(f"Total: {len(solo_uno)} estudiantes")

# Detalle de quienes aprobaron solo cada parcial
solo_parcial1 = parcial1 - parcial2
solo_parcial2 = parcial2 - parcial1
print(f"- Solo Parcial 1: {sorted(solo_parcial1)}")
print(f"- Solo Parcial 2: {sorted(solo_parcial2)}")

# Lista total de estudiantes que aprobaron al menos un parcial
al_menos_uno = parcial1 | parcial2
print("\nLista total de estudiantes con al menos un parcial:")
print(sorted(al_menos_uno))
print(f"Total: {len(al_menos_uno)} estudiantes")



# Ejercicio 8

stock_productos = {
    "Cafe": 50,
    "Leche": 30,
    "Pan": 25,
    "Yerba": 40,
    "Azucar": 60
}

print("# Sistema de Gestion de Stock #")

def mostrar_stock():
    print(f"\n# Stock ({len(stock_productos)} productos):")
    for producto, cantidad in sorted(stock_productos.items()):
        print(f" - {producto}: {cantidad} unidades")

while True:
    print("\n" + "#"*50)
    print("Opciones:")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades a producto existente")
    print("3. Agregar nuevo producto")
    print("4. Ver todo el stock")
    print("5. Salir")
    
    opcion = input("\nSelecciona una opcion (1-5): ").strip()
    
    if opcion == "1":
        # Consultar stock
        producto = input("Ingresa el nombre del producto a consultar: ").strip()
        if producto in stock_productos:
            print(f"Stock de {producto}: {stock_productos[producto]} unidades")
        else:
            print(f"El producto '{producto}' no existe en el inventario")
    
    elif opcion == "2":
        # Agregar unidades a producto existente
        producto = input("Ingresa el nombre del producto: ").strip()
        if producto in stock_productos:
            unidades = int(input(f"Cuantas unidades agregar a {producto}? "))
            if unidades > 0:
                stock_productos[producto] += unidades
                print(f"Se agregaron {unidades} unidades a {producto}")
                print(f"# Nuevo stock: {stock_productos[producto]} unidades")
            else:
                print("Debes ingresar un numero positivo")
        else:
            print(f"El producto '{producto}' no existe. Usa la opción 3 para agregarlo.")
    
    elif opcion == "3":
        # Agregar nuevo producto
        producto = input("Ingresa el nombre del nuevo producto: ").strip()
        if producto in stock_productos:
            print(f"El producto '{producto}' ya existe en el inventario")
        else:
            stock_inicial = int(input(f"Stock inicial para {producto}: "))
            if stock_inicial >= 0:
                stock_productos[producto] = stock_inicial
                print(f"Producto '{producto}' agregado con {stock_inicial} unidades")
            else:
                print("El stock no puede ser negativo")
    
    elif opcion == "4":
        # Ver todo el stock
        mostrar_stock()
    
    elif opcion == "5":
        # Salir
        print("\nResumen:")
        mostrar_stock()
        print("\nSistema cerrado")
        break
    
    else:
        print("Error. Opcion no valida. Selecciona 1-5")


    
# Ejercicio 9

agenda = {
    ("lunes", "10:00"): "Reunion",
    ("martes", "15:00"): "Clase de ingles",
    ("miercoles", "09:30"): "Cena en familia",
    ("jueves", "14:00"): "Almuerzo con compañeros",
    ("viernes", "11:00"): "Presentacion proyecto"
}

def mostrar_agenda_completa():
    print("\nAgenda Completa:")
    if not agenda:
        print(" - La agenda esta vacia")
        return
    
    for (dia, hora), evento in sorted(agenda.items()):
        print(f"- {dia:10} {hora:5} -> {evento}")

def consultar_evento(dia, hora):
    clave = (dia.lower(), hora)
    if clave in agenda:
        return f"{dia} a las {hora}: {agenda[clave]}"
    else:
        return f"No hay eventos programados para {dia} a las {hora}"

def agregar_evento(dia, hora, evento):
    clave = (dia.lower(), hora)
    if clave in agenda:
        return f"Ya existe un evento para {dia} a las {hora}: {agenda[clave]}"
    else:
        agenda[clave] = evento
        return f"Evento agregado: {dia} a las {hora} -> {evento}"

def eliminar_evento(dia, hora):
    clave = (dia.lower(), hora)
    if clave in agenda:
        evento_eliminado = agenda.pop(clave)
        return f"Evento eliminado: {dia} a las {hora} -> {evento_eliminado}"
    else:
        return f"No existe evento para {dia} a las {hora}"

# Programa principal
print("# AGENDA PERSONAL #")
print("Dias validos: lunes, martes, miercoles, jueves, viernes, sabado, domingo")
print("Formato de hora: HH:mm (ej: 09:30, 14:00, 16:45)")

while True:
    print("\n" + "#"*50)
    print("Opciones:")
    print("1. Consultar evento")
    print("2. Agregar evento")
    print("3. Eliminar evento")
    print("4. Ver agenda completa")
    print("5. Salir")
    
    opcion = input("\nSelecciona una opcion (1-5): ").strip()
    
    if opcion == "1":
        # Consultar evento
        dia = input("Ingresa el dia: ").strip()
        hora = input("Ingresa la hora (HH:mm): ").strip()
        print(consultar_evento(dia, hora))
    
    elif opcion == "2":
        # Agregar evento
        dia = input("Ingresa el dia: ").strip()
        hora = input("Ingresa la hora (HH:mm): ").strip()
        evento = input("Ingresa el evento: ").strip()
        print(agregar_evento(dia, hora, evento))
    
    elif opcion == "3":
        # Eliminar evento
        dia = input("Ingresa el dia: ").strip()
        hora = input("Ingresa la hora (HH:mm): ").strip()
        print(eliminar_evento(dia, hora))
    
    elif opcion == "4":
        # Ver agenda completa
        mostrar_agenda_completa()
    
    elif opcion == "5":
        # Salir
        print("\nResumen:")
        mostrar_agenda_completa()
        print("\nSistema cerrado")
        break
    
    else:
        print("Opcion no valida. Selecciona 1-5")



# Ejercicio 10

original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo",
    "Perú": "Lima"
}

# Invertir diccionario
invertido = {capital: pais for pais, capital in original.items()}

print("Diccionario original:")
print(original)
print("\nDiccionario invertido:")
print(invertido)