ingresos = float(input("Ingresa tus ingresos: "))
gastos = float(input("Ingresa tus gastos: "))

ahorro = ingresos - gastos
porcentaje = (ahorro / ingresos) * 100

print("Tu ahorro es:", ahorro)
print("Tu porcentaje de ahorro es:", porcentaje, "%")

if porcentaje > 30:
    clasificacion = "Excelente"
elif porcentaje >= 10:
    clasificacion = "Normal"
elif porcentaje > 0:
    clasificacion = "Bajo"
else:
    clasificacion = "Negativo"

print("Clasificacion financiera:", clasificacion)

archivo = open("registro_finanzas.txt", "a")
archivo.write("Ingresos: " + str(ingresos) + "\n")
archivo.write("Gastos: " + str(gastos) + "\n")
archivo.write("Ahorro: " + str(ahorro) + "\n")
archivo.write("Porcentaje: " + str(porcentaje) + "%\n")
archivo.write("Clasificacion: " + clasificacion + "\n")
archivo.write("-----------------------------\n")
archivo.close()

print("Datos guardados en registro_finanzas.txt")


