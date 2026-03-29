archivo = open("registro_finanzas.txt", "r")

lineas = archivo.readlines()
archivo.close()

print("📊 REGISTROS GUARDADOS:\n")

for linea in lineas:
    print(linea.strip())

ingresos_lista = []
gastos_lista = []
ahorros_lista = []

for linea in lineas:
    if "Ingresos" in linea:
        valor = float(linea.split(":")[1])
        ingresos_lista.append(valor)
    elif "Gastos" in linea:
        valor = float(linea.split(":")[1])
        gastos_lista.append(valor)
    elif "Ahorro" in linea:
        valor = float(linea.split(":")[1])
        ahorros_lista.append(valor)

if ingresos_lista:
    promedio_ingresos = sum(ingresos_lista) / len(ingresos_lista)
    promedio_gastos = sum(gastos_lista) / len(gastos_lista)
    promedio_ahorro = sum(ahorros_lista) / len(ahorros_lista)

    print("\n📈 PROMEDIOS:")
    print("Ingresos promedio:", promedio_ingresos)
    print("Gastos promedio:", promedio_gastos)
    print("Ahorro promedio:", promedio_ahorro)
