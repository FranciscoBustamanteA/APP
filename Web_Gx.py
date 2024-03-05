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
        # Restablecer usuario y contraseña después de la autenticación
        username_input = ""
        password_input = ""

    # Barra lateral para la navegación
    if is_authenticated:
        st.sidebar.title("Navegación")
        seleccion = st.sidebar.radio(
            "Ir a",
            ("Inicio 🏠", "Nominación 📋", "Declaración Recurso Primario 📊", "Logout🏃‍♂️")
        )

        if seleccion == "Nominación 📋":
            nominacion()
        elif seleccion == "Declaración Recurso Primario 📊":
            recurso_primario()
        elif seleccion == "Logout":
            # Restablecer la autenticación y mostrar la página de inicio nuevamente
            mostrar_inicio = True

if __name__ == "__main__":
    main()
