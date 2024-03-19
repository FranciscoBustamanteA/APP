import streamlit as st 
from home import nominacion
from Recurso_primario import recurso_primario
from STOCK import stock

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
            st.sidebar.success("¡Autenticación exitosa!")
            break

    # Barra lateral para la navegación
    st.sidebar.title("Navegación")
    if is_authenticated:
        seleccion = st.sidebar.radio(
            "Ir a",
            ("Inicio 🏠","Vectores GMetropolitana 📖"  "nominacion 📋", "Declaración Recurso Primario 📊","STOCK 💾")
        )
    else:
        seleccion = st.sidebar.radio(
            "Ir a",
            ("Inicio 🏠",)
        )

    if seleccion == "Inicio 🏠":
        pagina_inicio()
    elif seleccion == "nominacion 📋":
        nominacion()
    elif seleccion == "Declaración Recurso Primario 📊":
        recurso_primario()
    elif seleccion=="STOCK 💾":
        stock()
    elif seleccion=="Vectores GMetropolitana 📖":
        Vectores_GMetropolitana()

if __name__ == "__main__":
    main()
