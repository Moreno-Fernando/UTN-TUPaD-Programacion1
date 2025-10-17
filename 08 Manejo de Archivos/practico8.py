# Ejercicio 2

with open('productos.txt', 'r') as archivo:
        print("### Lista de Productos ###")
        for linea in archivo:
            datos = linea.strip().split(',')
            nombre = datos[0]
            precio = datos[1]
            cantidad = datos[2]
            print(f"Producto: {nombre.capitalize()} | Precio: ${precio} | Cantidad: {cantidad}")


# Ejercicio 3

# Mostrar productos existentes
with open('productos.txt', 'r') as archivo:
    print("### Lista de Productos ###")
    for linea in archivo:
        datos = linea.strip().split(',')
        nombre = datos[0]
        precio = datos[1]
        cantidad = datos[2]
        print(f"Producto: {nombre.capitalize()} | Precio: ${precio} | Cantidad: {cantidad}")

# Agregar nuevo producto
print("\n### Agregar Nuevo Producto ###")
nombre = input("Ingrese el nombre del producto: ").strip().lower()
precio = input("Ingrese el precio del producto: ").strip()
cantidad = input("Ingrese la cantidad del producto: ").strip()

# Agregar al archivo sin borrar el contenido existente
with open('productos.txt', 'a') as archivo:
    archivo.write(f"\n{nombre},{precio},{cantidad}")

print(f"Producto '{nombre.capitalize()}' agregado con exito!")



# Ejercicio 4

productos = []
nombre_archivo = 'productos.txt'
with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            if not linea.strip():
                continue

            nombre, precio_str, cantidad_str = linea.strip().split(',')
            
            producto_dic = {
                'nombre': nombre,
                'precio': float(precio_str),
                'cantidad': int(cantidad_str)
            }
            
            productos.append(producto_dic)

print(productos)



# Ejercicio 5

# Sintaxis de Ejercicio 4
busqueda_usuario = input("Ingrese el nombre del producto a buscar: ").lower()

producto_encontrado = False

for producto in productos:
    if producto['nombre'].lower() == busqueda_usuario:
        print("\nProducto:")
        print(f"Nombre:   {producto['nombre'].capitalize()}")
        print(f"Precio:   ${producto['precio']:.2f}")
        print(f"Cantidad: {producto['cantidad']}")
        producto_encontrado = True
        break

if not producto_encontrado:
    print(f"\nEl producto '{busqueda_usuario}' no se encuentra en el inventario.")



# Ejercicio 6

# Sintaxis de Ejercicio 5
with open(nombre_archivo, 'w') as archivo:
            for producto in productos:
                linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
                archivo.write(linea)
        
print(f"\nProductos guardados en '{nombre_archivo}'")