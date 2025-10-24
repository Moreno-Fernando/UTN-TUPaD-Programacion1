# Ejercicio 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un numero entero positivo: "))
    
if numero < 1:
    print("Por favor, ingrese un numero positivo.")
else:
    print(f"\nFactoriales de los numeros del 1 al {numero}:")
    print("-" * 38)
    
    for i in range(1, numero + 1):
        resultado = factorial(i)
        print(f"{i}! = {resultado}")



# Ejercicio 2

def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)

n = int(input("Ingrese la posicion hasta la cual mostrar la serie de Fibonacci: "))
    
if n < 0:
    print("Por favor, ingrese un numero positivo.")
else:
    print(f"\nSerie de Fibonacci hasta la posicion {n}:")
    print("-" * 40)
    
    # Mostrar la serie completa
    for i in range(n + 1):
        valor = fibonacci(i)
        print(f"Posicion {i}: {valor}")



# Ejercicio 3

def potencia(n, m):
    if m == 0:
        return 1
    if m == 1:
        return n
    return n * potencia(n, m - 1)

base = int(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))

if exponente < 0:
    print("Esta funcion solo trabaja con exponentes positivos.")
else:
    resultado = potencia(base, exponente)
    print(f"Resultado: {base}^{exponente} = {resultado}")
    


# Ejercicio 4

def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingrese un numero entero positivo: "))
if numero < 0:
    print("Error: El numero debe ser positivo.")
else:
    binario = decimal_a_binario(numero)
    print(f"\n{numero} en decimal = {binario} en binario")



# Ejercicio 5

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False
    
palabra = input("Ingrese una palabra: ").lower()
if es_palindromo(palabra):
    print(f"'{palabra}' es un palindromo")
else:
    print(f"'{palabra}' no es un palindromo")



# Ejercicio 6

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

numero = int(input("Ingrese un numero entero positivo: "))        
if numero < 0:
    print("Error: El numero debe ser positivo.")
else:
    resultado = suma_digitos(numero)
    print(f"La suma de los digitos de {numero} es: {resultado}")



# Ejercicio 7

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

nivel_base = int(input("Ingrese el numero de bloques en el nivel base: "))
        
if nivel_base < 1:
    print("Error: El numero debe ser mayor o igual a 1.")
else:
    total = contar_bloques(nivel_base)
    print(f"Para una piramide con {nivel_base} bloques en la base:")
    print(f"Total de bloques necesarios: {total}")
    secuencia = ""
    for i in range(nivel_base, 0, -1):
        secuencia += str(i)
        if i != 1:
            secuencia += " + "
    print(f"Secuencia: {secuencia} = {total}")



# Ejercicio 8

def contar_digito(numero, digito):
    if numero < 10:
        return 1 if numero == digito else 0
    else:
        ultimo_digito = numero % 10
        resto_numero = numero // 10
        if ultimo_digito == digito:
            return 1 + contar_digito(resto_numero, digito)
        else:
            return contar_digito(resto_numero, digito)

numero = int(input("Ingrese un numero entero positivo: "))
digito = int(input("Ingrese un digito a buscar (0-9): "))

if numero < 0:
    print("Error: El numero debe ser positivo.")
elif digito < 0 or digito > 9:
    print("Error: El digito debe estar entre 0 y 9.")
else:
    resultado = contar_digito(numero, digito)
    print(f"El digito {digito} aparece {resultado} veces en el numero {numero}")