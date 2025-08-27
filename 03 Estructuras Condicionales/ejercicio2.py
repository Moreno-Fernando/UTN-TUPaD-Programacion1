# calcular la nota final de un alumno
# promedio de parciales = 40%
# trabajo integrador = 60%

parcial1 = float(input("Ingrese la nota del primer parcial: "))
parcial2 = float(input("Ingrese la nota del segundo parcial: "))
trabajo_integrador = float(input("Ingrese la nota del trabajo integrador: "))

# promedio de los parciales
promedio_parciales = (parcial1 + parcial2) / 2
# nota final
nota_final = (promedio_parciales * 0.4) + (trabajo_integrador * 0.6)

print(f"La nota final del alumno es: {nota_final:.2f}")

if nota_final >= 6:
    print("El alumno ha aprobado.")
else:
    print("El alumno ha reprobado.")
