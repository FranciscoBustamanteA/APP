import streamlit as st 

# Definir credenciales
USERNAME = "fba"
PASSWORD = "fba"

def pagina_inicio():
    st.subheader("Bienvenido,  👋")
    st.title("Esta es la página de inicio")
    st.write(
        "Aquí puedes encontrar información general sobre la aplicación."
    )

def pagina_opcion1():
    st.title("Página de Opción 1")
    st.write("Contenido de la opción 1")

def pagina_opcion2():
    st.title("Página de Opción 2")
    st.write("Contenido de la opción 2")

def main():
    # Autenticación
    username_input = st.sidebar.text_input("Usuario")
    password_input = st.sidebar.text_input("Contraseña", type="password")
    is_authenticated = False

    # Verificar credenciales
    if username_input == USERNAME and password_input == PASSWORD:
        is_authenticated = True

    if is_authenticated:
        st.sidebar.success("¡Autenticación exitosa!")

        # Barra lateral para la navegación
        st.sidebar.title("Navegación")
        seleccion = st.sidebar.radio("Ir a", ("Inicio", "Opción 1", "Opción 2"))

        if seleccion == "Inicio":
            pagina_inicio()
        elif seleccion == "Opción 1":
            pagina_opcion1()
        elif seleccion == "Opción 2":
            pagina_opcion2()
    elif username_input or password_input:  # Solo mostrar mensaje de error si se ingresó algo
        st.sidebar.error("Nombre de usuario o contraseña incorrectos.")

if __name__ == "__main__":
    main()
