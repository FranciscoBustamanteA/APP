import streamlit as st 
import pandas as pd
from home import nominacion
from Recurso_primario import recurso_primario

# Definir credenciales
credenciales = {
    "fba": "fba",
    "mag": "mag",
    "ads": "ads",
    "ctc": "ctc"
}

def pagina_inicio():
    st.subheader("Bienvenido,  👋")
    st.title("Esta es la página de Planificación, Operación y Performance Gas & Fuel")
    st.write(
        "Aquí puedes encontrar información general, reportes, gráficos y aplicaciones en las tareas del área."
    )
    st.write("")
    st.write("consultas a francisco.bustamante@enel.com")

def main():
    # Variable de estado para controlar la autenticación
    is_authenticated = False

    # Página de inicio
    pagina_inicio()

    # Autenticación
    if not is_authenticated:
        username_input_placeholder = st.sidebar.empty()
        password_input_placeholder = st.sidebar.empty()
        username_input = username_input_placeholder.text_input("Usuario")
        password_input = password_input_placeholder.text_input("Contraseña", type="password")
        if st.sidebar.button("Iniciar sesión"):
            for username, password in credenciales.items():
                if username_input == username and password_input == password:
                    is_authenticated = True
                    st.sidebar.success("¡Autenticación exitosa!")
                    # Limpiar texto de campos de entrada
                    username_input_placeholder.empty()
                    password_input_placeholder.empty()
                    break

    # Barra lateral para la navegación
    if is_authenticated:
        st.sidebar.title("Navegación")
        seleccion = st.sidebar.radio(
            "Ir a",
            ("Inicio 🏠", "Nominación 📋", "Declaración Recurso Primario 📊", "Logout")
        )

        if seleccion == "Nominación 📋":
            nominacion()
        elif seleccion == "Declaración Recurso Primario 📊":
            recurso_primario()
        elif seleccion == "Logout":
            is_authenticated = False
            st.experimental_rerun()  # Reiniciar la aplicación

if __name__ == "__main__":
    main()

