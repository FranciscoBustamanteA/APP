import streamlit as st 

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Enel", page_icon=":tada:", layout="wide")

# Definir credenciales
USERNAME = "fba"
PASSWORD = "fba"

# Autenticación
username_input = st.sidebar.text_input("Usuario")
password_input = st.sidebar.text_input("Contraseña", type="password")
is_authenticated = False

# Verificar credenciales
if username_input == USERNAME and password_input == PASSWORD:
    is_authenticated = True

# Página inicial
st.subheader("Bienvenido,  :wave:")
st.title("Esta es la página repositorio de Planificación, Operación y Performance Gas and Fuels")
st.write(
    "Aquí irán las aplicaciones web desarrolladas para las tareas del área, buscando optimizar las tareas diarias"
)
st.write("Cualquier problema contactar con francisco.bustamante@enel.com")

# Mostrar páginas adicionales si la autenticación es exitosa
if is_authenticated:
    # ---- Otras Páginas ----
    page = st.sidebar.selectbox("Navegación", ["Inicio", "Opción 1", "Opción 2"])

    if page == "Opción 1":
        st.title("Opción 1")
        st.write("Contenido de la opción 1")

    elif page == "Opción 2":
        st.title("Opción 2")
        st.write("Contenido de la opción 2")
