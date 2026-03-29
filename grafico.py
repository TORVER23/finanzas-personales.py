import matplotlib.pyplot as plt

archivo = open("registro_finanzas.txt", "r")
lineas = archivo.readlines()
archivo.close()

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

x = range(1, len(ingresos) + 1)

plt.plot(x, ingresos, label="Ingresos")
plt.plot(x, gastos, label="Gastos")
plt.plot(x, ahorros, label="Ahorro")

plt.xlabel("Registro")
plt.ylabel("Monto")
plt.title("Analisis Financiero")
plt.legend()

plt.show()
