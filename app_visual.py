import tkinter as tk
from tkinter import messagebox

def guardar_datos():
    try:
        ingresos = float(entry_ingresos.get())
        gastos = float(entry_gastos.get())

        if ingresos == 0:
            messagebox.showerror("Error", "Los ingresos no pueden ser 0")
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

        resultado.config(
            text=(
                f"Ahorro: {ahorro}\n"
                f"Porcentaje: {porcentaje:.2f}%\n"
                f"Clasificación: {clasificacion}"
            )
        )

        entry_ingresos.delete(0, tk.END)
        entry_gastos.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Ingresa solo números válidos")


def ver_analisis():
    try:
        archivo = open("registro_finanzas.txt", "r")
        lineas = archivo.readlines()
        archivo.close()

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

            messagebox.showinfo(
                "Análisis",
                f"Ingresos promedio: {promedio_ingresos:.2f}\n"
                f"Gastos promedio: {promedio_gastos:.2f}\n"
                f"Ahorro promedio: {promedio_ahorro:.2f}"
            )
        else:
            messagebox.showinfo("Análisis", "No hay datos guardados todavía")

    except FileNotFoundError:
        messagebox.showinfo("Análisis", "Aún no existe registro_finanzas.txt")


ventana = tk.Tk()
ventana.title("App de Finanzas - Héctor")
ventana.geometry("400x320")

titulo = tk.Label(ventana, text="Control Financiero", font=("Arial", 16))
titulo.pack(pady=10)

label_ingresos = tk.Label(ventana, text="Ingresos:")
label_ingresos.pack()

entry_ingresos = tk.Entry(ventana)
entry_ingresos.pack(pady=5)

label_gastos = tk.Label(ventana, text="Gastos:")
label_gastos.pack()

entry_gastos = tk.Entry(ventana)
entry_gastos.pack(pady=5)

boton_guardar = tk.Button(ventana, text="Calcular y Guardar", command=guardar_datos)
boton_guardar.pack(pady=10)

boton_analisis = tk.Button(ventana, text="Ver Análisis", command=ver_analisis)
boton_analisis.pack(pady=5)

resultado = tk.Label(ventana, text="", font=("Arial", 12), justify="left")
resultado.pack(pady=15)

ventana.mainloop()

