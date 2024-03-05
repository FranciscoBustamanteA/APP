import streamlit as st 
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
    # Variable de estado para controlar si se ha autenticado
    is_authenticated = False

    # Autenticación
    username_input = st.sidebar.text_input("Usuario")
    password_input = st.sidebar.text_input("Contraseña", type="password")

    # Verificar credenciales
    for username, password in credenciales.items():
        if username_input == username and password_input == password:
            is_authenticated = True
            break

    if is_authenticated:
        st.sidebar.success("¡Autenticación exitosa!")
        st.experimental_rerun()  # Reiniciar la aplicación para actualizar el estado de autenticación
        return  # Salir de la función principal después de reiniciar la aplicación

    # Barra lateral para la navegación
    st.sidebar.title("Navegación")
    if is_authenticated:
        seleccion = st.sidebar.radio(
            "Ir a",
            ("Inicio 🏠", "Nominación 📋", "Declaración Recurso Primario 📊", "Logout")
        )
    else:
        seleccion = st.sidebar.radio(
            "Ir a",
            ("Inicio 🏠",)
        )

    if seleccion == "Inicio 🏠":
        pagina_inicio()
    elif seleccion == "Nominación 📋":
        nominacion()
    elif seleccion == "Declaración Recurso Primario 📊":
        recurso_primario()
    elif seleccion == "Logout":
        pass  # No hacer nada, ya que la aplicación se reiniciará automáticamente después de autenticarse

if __name__ == "__main__":
    main()
