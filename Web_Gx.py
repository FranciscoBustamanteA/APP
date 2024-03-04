import streamlit as st 
import pandas as pd

# Definir credenciales
credenciales = {
    "fba": "fba",
    "mag": "mag",
    "ads": "ads",
    "ctc":"ctc"
}

def pagina_inicio():
    st.title("Bienvenido a la aplicación")
    st.write("Por favor, ingrese sus credenciales en la barra lateral para comenzar.")

def pagina_opcion1():
    st.title("Página de Opción 1")
    st.write("Por favor, introduce dos números para sumarlos:")
    numero1 = st.number_input("Primer número", value=0)
    numero2 = st.number_input("Segundo número", value=0)
    resultado = numero1 + numero2
    st.write(f"La suma de {numero1} y {numero2} es: {resultado}")

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
    # Página de inicio
    pagina_inicio()

    # Autenticación
    username_input = st.sidebar.text_input("Usuario")
    password_input = st.sidebar.text_input("Contraseña", type="password")
    is_authenticated = False

    # Verificar credenciales
    for username, password in credenciales.items():
        if username_input == username and password_input == password:
            is_authenticated = True
            break

    if is_authenticated:
        st.sidebar.success("¡Autenticación exitosa!")

        # Barra lateral para la navegación
        st.sidebar.title("Navegación")
        seleccion = st.sidebar.radio("Ir a", ("Inicio", "Opción 1", "Opción 2"))

        if seleccion == "Opción 1":
            pagina_opcion1()
        elif seleccion == "Opción 2":
            pagina_opcion2()

if __name__ == "__main__":
    main()
