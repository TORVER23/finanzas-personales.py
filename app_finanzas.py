import matplotlib.pyplot as plt

def registrar():
    ingresos = float(input("Ingresa tus ingresos: "))
    gastos = float(input("Ingresa tus gastos: "))

    if ingresos == 0:
        print("Los ingresos no pueden ser 0")
        return

    ahorro = ingresos - gastos
    porcentaje = (ahorro / ingresos) * 100

    if porcentaje > 30:
        clasificacion = "Excelente"
    elif porcentaje >= 10:
        clasificacion = "Normal"
    elif porcentaje > 0:
        clasificacion = "Bajo"
    else:
        clasificacion = "Negativo"

    archivo = open("registro_finanzas.txt", "a")
    archivo.write("Ingresos: " + str(ingresos) + "\n")
    archivo.write("Gastos: " + str(gastos) + "\n")
    archivo.write("Ahorro: " + str(ahorro) + "\n")
    archivo.write("Porcentaje: " + str(porcentaje) + "%\n")
    archivo.write("Clasificacion: " + clasificacion + "\n")
    archivo.write("------------------------\n")
    archivo.close()

    print("\nDatos guardados correctamente")
    print("Ahorro:", ahorro)
    print("Porcentaje:", round(porcentaje, 2), "%")
    print("Clasificación:", clasificacion)


def analizar():
    try:
        archivo = open("registro_finanzas.txt", "r")
        lineas = archivo.readlines()
        archivo.close()
    except FileNotFoundError:
        print("No hay archivo de registros todavía")
        return

    ingresos_lista = []
    gastos_lista = []
    ahorros_lista = []

    for linea in lineas:
        if "Ingresos" in linea:
            ingresos_lista.append(float(linea.split(":")[1]))
        elif "Gastos" in linea:
            gastos_lista.append(float(linea.split(":")[1]))
        elif "Ahorro" in linea:
            ahorros_lista.append(float(linea.split(":")[1]))

    if ingresos_lista:
        promedio_ingresos = sum(ingresos_lista) / len(ingresos_lista)
        promedio_gastos = sum(gastos_lista) / len(gastos_lista)
        promedio_ahorro = sum(ahorros_lista) / len(ahorros_lista)

        print("\n--- ANALISIS ---")
        print("Cantidad de registros:", len(ingresos_lista))
        print("Ingresos promedio:", round(promedio_ingresos, 2))
        print("Gastos promedio:", round(promedio_gastos, 2))
        print("Ahorro promedio:", round(promedio_ahorro, 2))
    else:
        print("No hay datos aún")


def graficar():
    try:
        archivo = open("registro_finanzas.txt", "r")
        lineas = archivo.readlines()
        archivo.close()
    except FileNotFoundError:
        print("No hay archivo de registros todavía")
        return

    ingresos = []
    gastos = []
    ahorros = []

    for linea in lineas:
        if "Ingresos" in linea:
            ingresos.append(float(linea.split(":")[1]))
        elif "Gastos" in linea:
            gastos.append(float(linea.split(":")[1]))
        elif "Ahorro" in linea:
            ahorros.append(float(linea.split(":")[1]))

    if not ingresos:
        print("No hay datos para graficar")
        return

    x = range(1, len(ingresos) + 1)

    plt.plot(x, ingresos, marker="o", label="Ingresos")
    plt.plot(x, gastos, marker="o", label="Gastos")
    plt.plot(x, ahorros, marker="o", label="Ahorro")

    plt.xlabel("Registro")
    plt.ylabel("Monto")
    plt.title("Analisis Financiero")
    plt.legend()
    plt.grid()
    plt.savefig("grafico_finanzas.png")
    plt.show()


def ver_registros():
    try:
        archivo = open("registro_finanzas.txt", "r")
        contenido = archivo.read()
        archivo.close()

        print("\n--- REGISTROS GUARDADOS ---")
        print(contenido)

    except FileNotFoundError:
        print("No existe todavía el archivo de registros")


def borrar_registros():
    confirmacion = input("¿Seguro que quieres borrar todos los registros? (si/no): ")

    if confirmacion.lower() == "si":
        archivo = open("registro_finanzas.txt", "w")
        archivo.close()
        print("Todos los registros fueron borrados")
    else:
        print("Operación cancelada")


while True:
    print("\n--- MENU ---")
    print("1. Registrar datos")
    print("2. Ver analisis")
    print("3. Ver grafico")
    print("4. Ver todos los registros")
    print("5. Borrar registros")
    print("6. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        registrar()
    elif opcion == "2":
        analizar()
    elif opcion == "3":
        graficar()
    elif opcion == "4":
        ver_registros()
    elif opcion == "5":
        borrar_registros()
    elif opcion == "6":
        print("Saliendo...")
        break
    else:
        print("Opcion invalida")

