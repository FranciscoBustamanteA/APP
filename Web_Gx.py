import streamlit as st 
import pandas as pd
from home import nominacion

# Definir credenciales
credenciales = {
    "fba": "fba",
    "mag": "mag",
    "ads": "ads",
    "ctc":"ctc"
}

def pagina_inicio():
    st.subheader("Bienvenido,  👋")
    st.title("Esta es la página de Planificación, Operación y Performance Gas & Fuel")
    st.write(
        "Aquí puedes encontrar información general, reportes, gráficos y aplicaciones en las tareas del área."
    )
    st.write("")
    st.write("consultas a francisco.bustamante@enel.com")

def nominacion():
    st.title("Nominación")
    st.write("Por favor, introduce dos números para sumarlos:")
    

def pagina_opcion2():
    st.title("Página de Opción 2")
    st.write("Cargar archivo Excel:")
    uploaded_file = st.file_uploader("Seleccione un archivo Excel", type=["xlsx", "xls"])

    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            st.write(df)
        except Exception as e:
            st.error(f"Ocurrió un error al leer el archivo: {str(e)}")

def main():
    # Variable de estado para controlar la visibilidad de la página de inicio
    mostrar_inicio = True

    # Página de inicio
    if mostrar_inicio:
        pagina_inicio()

    # Autenticación
    username_input = st.sidebar.text_input("Usuario")
    password_input = st.sidebar.text_input("Contraseña", type="password")
    is_authenticated = False

    # Verificar credenciales
    for username, password in credenciales.items():
        if username_input == username and password_input == password:
            is_authenticated = True
            mostrar_inicio = False  # Ocultar la página de inicio cuando se autentifica
            break

    if is_authenticated:
        st.sidebar.success("¡Autenticación exitosa!")

    # Barra lateral para la navegación
    if is_authenticated:
        st.sidebar.title("Navegación")
        seleccion = st.sidebar.radio(
            "Ir a",
            ("Inicio 🏠", "Nominación 📋", "Opción 2 📊")
        )

        if seleccion == "Nominación 📋":
            Nominacion()
        elif seleccion == "Opción 2 📊":
            pagina_opcion2()

if __name__ == "__main__":
    main()
