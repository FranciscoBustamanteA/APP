import streamlit as st 

# Definir credenciales
USERNAME = "fba"
PASSWORD = "fba"

# Autenticación
username_input = st.sidebar.text_input("Usuario")
password_input = st.sidebar.text_input("Contraseña", type="password")

# Verificar credenciales
if username_input == USERNAME and password_input == PASSWORD:
    st.sidebar.success("¡Autenticación exitosa!")
    
    # ---- HEADER SECTION ----
    st.subheader("Bienvenido,  :wave:")
    st.title("Esta es la pagina repositorio de Planificación, Operación y Performance Gas and Fuels")
    st.write(
        "Aquí irán las aplicaciones web desarrolladas para las tareas del área, buscando optimizar las tareas diarias"
    )
    st.write("Cualquier problema contactar con francisco.bustamante@enel.com")

else:
    st.sidebar.error("Nombre de usuario o contraseña incorrectos.")
