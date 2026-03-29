import streamlit as st
import matplotlib.pyplot as plt
import os

ARCHIVO = "registro_finanzas.txt"


def guardar_datos(ingresos, gastos):
    ahorro = ingresos - gastos
    porcentaje = (ahorro / ingresos) * 100 if ingresos != 0 else 0

    if porcentaje > 30:
        clasificacion = "Excelente"
    elif porcentaje >= 10:
        clasificacion = "Normal"
    elif porcentaje > 0:
        clasificacion = "Bajo"
    else:
        clasificacion = "Negativo"

    archivo = open(ARCHIVO, "a")
    archivo.write(f"Ingresos: {ingresos}\n")
    archivo.write(f"Gastos: {gastos}\n")
    archivo.write(f"Ahorro: {ahorro}\n")
    archivo.write(f"Porcentaje: {porcentaje}%\n")
    archivo.write(f"Clasificacion: {clasificacion}\n")
    archivo.write("------------------------\n")
    archivo.close()

    return ahorro, porcentaje, clasificacion


def leer_datos():
    ingresos_lista = []
    gastos_lista = []
    ahorros_lista = []

    if not os.path.exists(ARCHIVO):
        return ingresos_lista, gastos_lista, ahorros_lista

    archivo = open(ARCHIVO, "r")
    lineas = archivo.readlines()
    archivo.close()

    for linea in lineas:
        if "Ingresos" in linea:
            ingresos_lista.append(float(linea.split(":")[1]))
        elif "Gastos" in linea:
            gastos_lista.append(float(linea.split(":")[1]))
        elif "Ahorro" in linea:
            ahorros_lista.append(float(linea.split(":")[1]))

    return ingresos_lista, gastos_lista, ahorros_lista


def leer_historial():
    if not os.path.exists(ARCHIVO):
        return "Todavía no hay registros guardados."

    archivo = open(ARCHIVO, "r")
    contenido = archivo.read()
    archivo.close()
    return contenido


def borrar_registros():
    archivo = open(ARCHIVO, "w")
    archivo.close()


st.set_page_config(page_title="Finanzas Personales", page_icon="💰", layout="centered")

st.title("💰 App de Finanzas Personales")
st.caption("Registro, análisis y visualización de ingresos, gastos y ahorro")

tab1, tab2, tab3 = st.tabs(["Registrar", "Análisis", "Historial"])

with tab1:
    st.subheader("Registrar datos")

    col1, col2 = st.columns(2)

    with col1:
        ingresos = st.number_input("Ingresa tus ingresos", min_value=0.0, step=1.0)

    with col2:
        gastos = st.number_input("Ingresa tus gastos", min_value=0.0, step=1.0)

    if st.button("Guardar datos"):
        if ingresos == 0:
            st.error("Los ingresos no pueden ser 0")
        else:
            ahorro, porcentaje, clasificacion = guardar_datos(ingresos, gastos)
            st.success("Datos guardados correctamente")

            m1, m2, m3 = st.columns(3)
            m1.metric("Ahorro", round(ahorro, 2))
            m2.metric("Porcentaje", f"{round(porcentaje, 2)}%")
            m3.metric("Clasificación", clasificacion)

with tab2:
    st.subheader("Análisis")

    ingresos_lista, gastos_lista, ahorros_lista = leer_datos()

    if ingresos_lista:
        promedio_ingresos = sum(ingresos_lista) / len(ingresos_lista)
        promedio_gastos = sum(gastos_lista) / len(gastos_lista)
        promedio_ahorro = sum(ahorros_lista) / len(ahorros_lista)

        a1, a2, a3, a4 = st.columns(4)
        a1.metric("Registros", len(ingresos_lista))
        a2.metric("Ingreso promedio", round(promedio_ingresos, 2))
        a3.metric("Gasto promedio", round(promedio_gastos, 2))
        a4.metric("Ahorro promedio", round(promedio_ahorro, 2))

        st.subheader("Gráfico financiero")

        fig, ax = plt.subplots()
        x = range(1, len(ingresos_lista) + 1)

        ax.plot(x, ingresos_lista, marker="o", label="Ingresos")
        ax.plot(x, gastos_lista, marker="o", label="Gastos")
        ax.plot(x, ahorros_lista, marker="o", label="Ahorro")

        ax.set_xlabel("Registro")
        ax.set_ylabel("Monto")
        ax.set_title("Análisis Financiero")
        ax.legend()
        ax.grid()

        st.pyplot(fig)
    else:
        st.info("Todavía no hay datos guardados")

with tab3:
    st.subheader("Historial de registros")

    historial = leer_historial()
    st.text_area("Contenido del archivo", historial, height=250)

    st.subheader("Acciones")

    confirmar = st.checkbox("Confirmo que quiero borrar todos los registros")

    if st.button("Borrar todos los registros"):
        if confirmar:
            borrar_registros()
            st.warning("Se borraron todos los registros. Recarga la app.")
        else:
            st.error("Debes marcar la confirmación antes de borrar")

    if os.path.exists(ARCHIVO):
        archivo = open(ARCHIVO, "r")
        contenido = archivo.read()
        archivo.close()

        st.download_button(
            label="Descargar registros",
            data=contenido,
            file_name="registro_finanzas.txt",
            mime="text/plain"
        )
